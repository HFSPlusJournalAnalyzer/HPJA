from struct import *
import HFSPlus_sStructure as ss

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
    vec.append(ext)
    return ss.ForkData(*vec)

def getCatalogKey(ck_binary):
    parID, nameLen = unpack_from(">IH", ck_binary)
    nameStr = ck_binary[6:]
    nodeUnicode = "".join(map(unichr, unpack_from(">"+nameLen*"H", nameStr)))
    return ss.CatalogKey(parID, ss.UniChar(nameLen, nodeUnicode))

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
    
def getCatalogLeafRecord(clk_binary):
    keyLen = unpack_from(">H", clk_binary)[0]
    catalKey = getCatalogKey(clk_binary[2:2+keyLen])
    Key = ss.BTKeyedRec(keyLen, catalKey) 
    rec_binary = clk_binary[len(Key):]
    recordType = unpack_from(">H", rec_binary)[0]
    typeList = [0, getCatalogFolder, getCatalogFile, getCatalogThread, getCatalogThread]
    Record = typeList[recordType](rec_binary)
    return ss.CatalogLeafRec(Key, Record)

def getCatalogLeaf(cl_binary):
    cl_buf = memoryview(cl_binary)
    nd = getNodeDescriptor(cl_binary)
    leafRecList = []
    
    cl_buf = cl_buf[14:]
    for i in range(nd.numRecords):
        lr = getCatalogLeafRecord(cl_buf)
        leafRecList.append(lr)
        cl_buf = cl_buf[len(lr):]
    
    return ss.CatalogLeaf(nd, leafRecList)

def getCatalogHeader(ch_binary): # require bounded-ness
    ch_buf = memoryview(ch_binary)
    nd = getNodeDescriptor(ch_buf)
    hr = getBTHeaderRec(ch_buf[14:])
    ch_buf = ch_buf[120:]
    udr = ch_buf[:128]
    mr = ch_buf[128:]
    
    return ss.CatalogHeader(nd, hr, udr, mr)

def getCatalogIndex(ci_binary):
    return

def getCatalogMap(cm_binary):
    return
    
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
    