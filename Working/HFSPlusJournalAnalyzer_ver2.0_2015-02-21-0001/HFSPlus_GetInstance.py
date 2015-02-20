from struct import *
import HFSPlus_sStructure as ss
from collections import namedtuple

parseInfo = namedtuple("parseInfo", ['sect_size', 'blockMag', 'sfLoc'])
bOffsetInfo = namedtuple("bOffsetInfo", ['start', 'end', 'contain', 'data', 'name', 'offset'])
# variable for storing a sector size 
# variable for storing a magnification of block from sect_size (blockSize/sect_size)
# dict for storing the location of special files

def getJournalHeader(jh_binary):
    endian = unpack_from(">I",jh_binary, 4)[0]
    eflag = [">","<"][endian == 0x78563412]
    vec = list(unpack_from(eflag + 'IIQQQIII',jh_binary))
    vec[1] = eflag  # replace 'endian' field as '>' or '<'. It represents endianess more clearly.
    return ss.JournalHeader(*vec)

def getBlockInfo(bi_binary):
    vec = unpack_from('<QII',bi_binary)
    return ss.BlockInfo(*vec)

def getBlockListHeader(blh_binary):
    blh_0 = blh_binary[:16]
    blh_1 = blh_binary[16:] 
    vec = list(unpack('<HHIII',blh_0))
    vec.append(getBlockInfo(blh_1))
    return ss.BlockListHeader(*vec)

def getNodeDescriptor(nd_binary):
    vec = unpack_from('>IIbBHH',nd_binary)
    return ss.NodeDescriptor(*vec)

def getBTHeaderRec(hr_binary):
    vec = unpack_from('>HIIIIHHIIHIBBI',hr_binary)  # reserved3 field omited
    return ss.BTHeaderRec(*vec)

def getExtentDescriptor(ed_binary):
    vec = unpack_from('>II',ed_binary)
    return ss.ExtentDescriptor(*vec)

def getForkData(fd_binary):
    fd_0 = fd_binary[:16]
    ext = []
    for i in range(8):
        temp = fd_binary[16+8*i:16+8*(i+1)]
        e = getExtentDescriptor(temp)
        ext.append(e)
    vec = list(unpack_from('>QII',fd_binary))
    vec.append(ss.ExtentsDataRec(*ext))
    return ss.ForkData(*vec)


def getBSDInfo(bsd_binary):
    vec = unpack_from(">IIBBHI", bsd_binary)
    return ss.BSDInfo(*vec)

def getFolderInfo(foi_binary):
    RectVec = unpack_from(">hhhh", foi_binary)
    Flag = unpack_from(">H", foi_binary, 8)[0]
    Location = unpack_from(">hh", foi_binary, 10)
    reserved = unpack_from(">H", foi_binary, 14)[0]
    vec = [ss.Rect(*RectVec), Flag, ss.Point(*Location), reserved]
    return ss.FolderInfo(*vec)

def getExtendedFolderInfo(efi_binary):
    scrPosVec = unpack_from(">hh", efi_binary)
    vec = list(unpack_from(">iHhi", efi_binary, 4))
    vec.insert(0, ss.Point(*scrPosVec))
    return ss.ExtendedFolderInfo(*vec)

def getFileInfo(fii_binary):
    vec = list(unpack_from(">IIH",fii_binary))
    Location = unpack_from(">hh", fii_binary, 10)
    res = unpack_from(">H", fii_binary, 14)[0]
    vec.extend([ss.Point(*Location), res])
    return ss.FileInfo(*vec)

def getExtendedFileInfo(efi_binary):
    res1 = unpack_from(">hhhh", efi_binary)
    vec = list(unpack_from(">Hhi", efi_binary, 8))
    vec.insert(0, res1)
    return ss.ExtendedFileInfo(*vec)

def getCatalogFolder(cfo_binary):
    cfo_0 = cfo_binary[:32]   
    cfo_1 = cfo_binary[32:48]  # BSDInfo
    cfo_2 = cfo_binary[48:64]  # userInfo
    cfo_3 = cfo_binary[64:80]  # finderInfo
    cfo_4 = cfo_binary[80:]  # textEncoding, reserved 
    
    vec0 = list(unpack('>hHIIIIIII',cfo_0))
    BSDInfo = getBSDInfo(cfo_1)
    userInfo = getFolderInfo(cfo_2)
    finderInfo = getExtendedFolderInfo(cfo_3)
    textEncoding, reserved = unpack_from(">II", cfo_4)
    vec1 = [BSDInfo, userInfo, finderInfo, textEncoding, reserved]
    
    vec0.extend(vec1)
    return ss.CatalogFolder(*vec0)
    
def getCatalogFile(cfi_binary):
    cfi_0 = cfi_binary[:32]
    cfi_1 = cfi_binary[32:48]  # BSDInfo
    cfi_2 = cfi_binary[48:64]  # userInfo
    cfi_3 = cfi_binary[64:80]  # finderInfo
    cfi_4 = cfi_binary[80:88]  # textEncoding, reserved 
    cfi_5 = cfi_binary[88:168] # dataFork
    cfi_6 = cfi_binary[168:]   # resourceFork
    
    vec0 = list(unpack('>hHIIIIIII',cfi_0))
    BSDInfo = getBSDInfo(cfi_1)
    userInfo = getFileInfo(cfi_2)
    finderInfo = getExtendedFileInfo(cfi_3)
    textEncoding, reserved2 = unpack(">II", cfi_4) 
    dataFork = getForkData(cfi_5)
    resourceFork = getForkData(cfi_6)
    vec1 = [BSDInfo, userInfo, finderInfo, textEncoding, reserved2, dataFork, resourceFork]
    
    vec0.extend(vec1)
    return ss.CatalogFile(*vec0)

def getCatalogThread(cth_binary):
    cth_0 = cth_binary[:10]
    cth_1 = cth_binary[10:]
    recordType, reserved, parID, nameLen = unpack(">hhIH",cth_0)
    nodeUnicode = "".join(map(unichr, unpack_from(">"+nameLen*"H", cth_1)))
    
    return ss.CatalogThread(recordType, reserved, parID, ss.UniChar(nameLen, nodeUnicode))
    
def getCatalogKey(ck_binary):
    rType, parID, nameLen = unpack_from(">HIH", ck_binary)
    nameStr = ck_binary[8:]
    nodeUnicode = "".join(map(unichr, unpack_from(">"+nameLen*"H", nameStr)))
    return ss.CatalogKey(rType, parID, ss.UniChar(nameLen, nodeUnicode))

def getCatalogLeafRec(clk_binary):
    keyLen = unpack_from(">H", clk_binary)[0]
    catalKey = getCatalogKey(clk_binary[:2+keyLen])
    rec_binary = clk_binary[2+keyLen:]
    recordType = unpack_from(">H", rec_binary)[0]
    typeList = [0, getCatalogFolder, getCatalogFile, getCatalogThread, getCatalogThread]
    Record = typeList[recordType](rec_binary)
    return ss.BTRecord(catalKey, Record)

def getCatalogLeaf(cl_binary):
    cl_buf = memoryview(cl_binary)
    nd = getNodeDescriptor(cl_binary)
    leafRecList = []
    
    cl_buf = cl_buf[14:]
    for i in range(nd.numRecords):
        lr = getCatalogLeafRec(cl_buf)
        leafRecList.append(lr)
        cl_buf = cl_buf[len(lr):]
        
    return ss.LeafNode(nd, leafRecList)

def getCatalogPointerRec(cpr_binary):
    keyLen = unpack_from(">H", cpr_binary)[0]
    catalKey = getCatalogKey(cpr_binary[:2+keyLen])
    nodeNum = unpack_from(">I", cpr_binary[2+keyLen:])[0]
    
    return ss.BTRecord(catalKey, ss.BTPointer(nodeNum))

def getCatalogIndex(ci_binary):
    ci_buf = memoryview(ci_binary)
    nd = getNodeDescriptor(ci_buf)
    offsetList = [14]
    PointerRecList = []
    for i in range(nd.numRecords):
        offset = unpack(">H", ci_buf[-2*i-4:-2*i-2])[0]
        offsetList.append(offset)
    for i in range(len(offsetList)-1):
        temp = ci_buf[offsetList[i]:offsetList[i+1]]
        cpr = getCatalogPointerRec(temp)
        PointerRecList.append(cpr)
    return ss.IndexNode(nd,PointerRecList)

'''
Extents
'''
def getExtentsKey(ek_binary):
    vec = unpack_from(">HBBII", ek_binary)
    return ss.ExtentsKey(*vec)

def getExtentsLeafRec(elf_binary):
    extKey = getExtentsKey(elf_binary[:12])
    rec_binary = elf_binary[12:]
    ext = []
    for i in range(8):
        temp = rec_binary[16+8*i:16+8*(i+1)]
        e = getExtentDescriptor(temp)
        ext.append(e)
    
    return ss.BTRecord(extKey, ss.ExtentsDataRec(*ext))

def getExtentsLeaf(el_binary):
    el_buf = memoryview(el_binary)
    nd = getNodeDescriptor(el_binary)
    leafRecList = []
    el_buf = el_buf[14:]
    for i in range(nd.numRecords):
        lr = getExtentsLeafRec(el_buf)
        leafRecList.append(lr)
        el_buf = el_buf[len(lr):]
    return ss.LeafNode(nd, leafRecList)

def getExtentsPointerRec(epr_binary):
    extKey = getExtentsKey(epr_binary[:12])
    nodeNum = unpack_from(">I", epr_binary[12:])[0]
    return ss.BTRecord(extKey, ss.BTPointer(nodeNum))

def getExtentsIndex(ei_binary):
    ei_buf = memoryview(ei_binary)
    nd = getNodeDescriptor(ei_buf)
    offsetList = [14]
    PointerRecList = []
    for i in range(nd.numRecords):
        offset = unpack(">H", ei_buf[-2*i-4:-2*i-2])[0]
        offsetList.append(offset)
    for i in range(len(offsetList)-1):
        temp = ei_buf[offsetList[i]:offsetList[i+1]]
        epr = getExtentsPointerRec(temp)
        PointerRecList.append(epr)
    return ss.IndexNode(nd,PointerRecList)

'''
Attribute
'''

def getAttributesKey(ak_binary):
    vec = list(unpack_from(">HHIIH", ak_binary))
    nameLen = vec[-1]
    nameUni = "".join(map(unichr, unpack_from(">"+nameLen*"H", ak_binary[14:])))
    vec.append(nameUni)
    return ss.AttrKey(*vec)

def getAttributesData(ad_binary):
    vec = list(unpack_from(">IQI", ad_binary))
    attrSize = vec[-1]
    attrData = ''.join(ad_binary[16:16+attrSize+(attrSize%2)])
    vec.append(attrData)
    return ss.AttrData(*vec)

def getAttributesForkData(af_binary):
    recordType, res = unpack_from(">II", ad_binary)
    fd = getForkData(af_binary[8:])
    return ss.AttrForkData(recordType, res, fd)

def getAttributesExtents(ae_binary):
    recordType, res = unpack_from(">II", ad_binary)
    rec_binary = ad_binary[8:]
    ext = []
    for i in range(8):
        temp = rec_binary[16+8*i:16+8*(i+1)]
        e = getExtentDescriptor(temp)
        ext.append(e)
    return ss.AttrExtents(recordType, res, ss.ExtentsDataRec(*ext))

def getAttributesLeafRec(alr_binary):
    keyLen = unpack_from(">H", alr_binary)[0]
    attKey = getAttributesKey(alr_binary[:2+keyLen])
    rec_binary = alr_binary[2+keyLen:]
    recordType = unpack_from(">I", rec_binary)[0]
    typeList = [0, getAttributesData, getAttributesForkData, getAttributesExtents]
    Record = typeList[recordType/0x10](rec_binary)
    return ss.BTRecord(attKey, Record)

def getAttributesLeaf(al_binary):
    al_buf = memoryview(al_binary)
    nd = getNodeDescriptor(al_binary)
    leafRecList = []
    
    al_buf = al_buf[14:]
    for i in range(nd.numRecords):
        lr = getAttributesLeafRec(al_buf)
        leafRecList.append(lr)
        al_buf = al_buf[len(lr):]
    
    return ss.LeafNode(nd, leafRecList)

def getAttributesPointerRec(apr_binary):
    keyLen = unpack_from(">H", apr_binary)[0]
    attKey = getAttributesKey(apr_binary[:2+keyLen])
    nodeNum = unpack_from(">I", apr_binary[2+keyLen:])[0]
    return ss.BTRecord(attKey, ss.BTPointer(nodeNum))

def getAttributesIndex(ai_binary):
    ai_buf = memoryview(ai_binary)
    nd = getNodeDescriptor(ai_buf)
    offsetList = [14]
    PointerRecList = []
    for i in range(nd.numRecords):
        offset = unpack(">H", ai_buf[-2*i-4:-2*i-2])[0]
        offsetList.append(offset)
    for i in range(len(offsetList)-1):
        temp = ai_buf[offsetList[i]:offsetList[i+1]]
        apr = getAttributesPointerRec(temp)
        PointerRecList.append(apr)
    return ss.IndexNode(nd,PointerRecList)

'''
Header, Map
'''

def getHeaderNode(ch_binary): 
    ch_buf = memoryview(ch_binary)
    nd = getNodeDescriptor(ch_buf)
    hr = getBTHeaderRec(ch_buf[14:])
    ch_buf = ch_buf[120:]
    udr = ch_buf[:128]
    mr = ch_buf[128:-8]
    return ss.HeaderNode(nd, hr, udr, mr)

def getMapNode(mn_binary):
    mn_buf = memoryview(mn_binary)
    nd = getNodeDescriptor(mn_buf)
    offsetList = [14]
    for i in range(nd.numRecords):
        offset = unpack(">H", mn_buf[-2*i-4:-2*i-2])[0]
        offsetList.append(offset)
    mr = mn_buf[14:offsetList[1]]
    return ss.MapNode(nd, mr)

'''
VolumeHeader
'''
    
def getVolumeHeader(vh_binary):
    vh_0 = vh_binary[:80]
    vh_1 = vh_binary[80:112]
    vh_sp = []
    for i in range(5):
        t = vh_binary[112+80*i:112+80*(i+1)]
        vh_sp.append(t)
        
    vec = list(unpack('>HHIIIIIIIIIIIIIIIIIQ',vh_0))
    
    fI = unpack('>IIIIIIII',vh_1)
    vec.append(fI)
    
    for i in range(5):
        vec.append(getForkData(vh_sp[i]))
    return ss.VolumeHeader(*vec)


# User class

def getparseInfo(journal_blob):
    sfLoc = {}
    vh_samInd = journal_blob.find("H+")
    jnl = memoryview(journal_blob)
    j_header = getJournalHeader(jnl)
    sect_size = j_header.jhdr_size
    vh = getVolumeHeader(journal_blob[vh_samInd:vh_samInd+sect_size])
    sfLoc['AllocationFile'] = vh.allocationFile.extents
    sfLoc['ExtentsFile'] = vh.extentsFile.extents
    sfLoc['CatalogFile'] = vh.catalogFile.extents
    sfLoc['AttributesFile'] = vh.attributesFile.extents
    blockMag = vh.blockSize/sect_size
    return parseInfo(sect_size, blockMag, sfLoc)
    