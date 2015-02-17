'''
Created on 2015. 2. 8.

@author: biscuit
'''
from HFSPlus_GetInstance import *

etcData = []

def journalParser(journal_blob):
    pInfo = getparseInfo(journal_blob)
    bOffData = []
    
    jnl = memoryview(journal_blob)
    j_header = getJournalHeader(jnl)
    bOffData.append(bOffsetInfo(0, pInfo.sect_size, None, j_header, "JournalHeader", 0))
    j_buf = jnl[pInfo.sect_size:]
    startOffset = getStart(j_buf, j_header.end) # setting the startOffset
    
    j_ParseList, bl_bOff = journalBufferParser(j_buf, j_header, startOffset, [], [], pInfo)
    bOffData.append(bOffsetInfo(startOffset, j_header.end, bl_bOff, j_ParseList, 'JournalBuffer', pInfo.sect_size))  
    # with offset pInfo.sect_size
    j_ParseList.insert(0, j_header)
    
    return j_ParseList, pInfo, bOffData

def getStart(j_buf, end):
    cur = end
    lenBuf = len(j_buf)
    curLine = j_buf[cur:cur+0x10]
    while curLine != 'Z'*16:
        cur = (cur+0x10) % lenBuf
        curLine = j_buf[cur:cur+0x10]
    while(True):
        cur = (cur-0x10) % lenBuf
        curLine = j_buf[cur:cur+0x10]
        if cur == (end - 0x10) % lenBuf:
            while curLine != 'Z'*16:
                cur = (cur+0x10) % lenBuf
                curLine = j_buf[cur:cur+0x10]
            while curLine == 'Z'*16:
                cur = (cur+0x10) % lenBuf
                curLine = j_buf[cur:cur+0x10]
            while curLine != 'Z'*16:
                cur = (cur+0x10) % lenBuf
                curLine = j_buf[cur:cur+0x10]
            cur = (cur-0x10) % lenBuf
            curLine = j_buf[cur:cur+0x10]
        if curLine[4:8] != '\x00\x00\x00\x00':
            return cur

def getBufContent(buf, start, end):
    if end < start:
        return memoryview( buf[start:].tobytes() + buf[:end].tobytes() )
    else: return buf[start:end]
    
def detBlockType(secNumber, sfLocDict ):
    for s in sfLocDict:
        for e in sfLocDict[s]:
            if e.isIn(secNumber):
                return s
    return None

def journalBufferParser(j_buffer, JournalHeader, startOffset, parseList, bOffList, pInfo):
    if startOffset == (JournalHeader.end - pInfo.sect_size): # -0x200 for Journal Header area
        return parseList, bOffList
    blh = getBlockListHeader(j_buffer[startOffset:])
    
    nextOffset = ( startOffset + blh.bytes_used ) % len(j_buffer)
    curTrans = getBufContent(j_buffer, startOffset, nextOffset)
    
    tParse, trans_bOff = transParser(curTrans, pInfo, startOffset+pInfo.sect_size)
    parseList.append(tParse)
    bOffList.append(bOffsetInfo(startOffset, nextOffset, trans_bOff, tParse, "BlockList", pInfo.sect_size))
    return journalBufferParser(j_buffer, JournalHeader, nextOffset, parseList, bOffList, pInfo)

def transParser(trans, pInfo, offset):
    t_bOff = [] # with offset startOffset+pInfo.sect_size
    blh = getBlockListHeader(trans)  # block list header
    t_bOff.append(bOffsetInfo(0, 0x20, None, blh, "BlockListHeader", offset))
    bi_List = []  # list of block info's 
    data_offset = 0  # for computing the offset from the bottom of the transaction block, of the data-area.
    for i in range(blh.num_blocks-1):
        bi = getBlockInfo(trans[0x20+0x10*i:])
        data_offset += bi.bsize
        bi_List.append(bi)
    t_bOff.append(bOffsetInfo(0x20, 0x10+0x10*blh.num_blocks, None, bi_List, 'BlockInfo', offset))
    
    data_List = []
    b_erase = []
    data_area = trans[-data_offset:]
    data_bOff = []
    point = len(trans)-data_offset
    
    for b in bi_List:
        dBlock, d_bOff = getDataBlock(data_area[:b.bsize], b, pInfo, offset + point)
        if dBlock != None:
            data_List.append(dBlock)
            data_bOff.append(d_bOff)
        else: b_erase.append(b)
        data_area = data_area[b.bsize:]
        point += b.bsize
        
    for e in b_erase:
        bi_List.remove(e)
    
    t_bOff.append(bOffsetInfo(len(trans)-data_offset, len(trans), data_bOff, data_List, "DataBlocks", offset))
    return [blh, bi_List, data_List], t_bOff

# auxiliary function ; To identify a data block.
def getDataBlock(data_block, BlockInfo, pInfo, offset):
    global etcData
    data_sNum = BlockInfo.bnum / pInfo.blockMag
    
    curSType = detBlockType(data_sNum, pInfo.sfLoc)
        
    raw_data = data_block.tobytes()
    if "H+\x00\x04" in raw_data:
        vh_off = raw_data.find("H+\x00\x04")
        VolHead = getVolumeHeader(data_block[vh_off:vh_off+0x200])
        d_bOff = bOffsetInfo(vh_off, vh_off+0x200, None, VolHead, "VolumeHeader", offset)
        return VolHead, d_bOff
    if curSType == 'AllocationFile':
        d_bOff = bOffsetInfo(0, BlockInfo.bsize, None, None, "Allocation", offset)  # memoryview
        return data_block, d_bOff
     
    kindDict = {'CatalogFile': [getCatalogLeaf, getCatalogIndex],
                'ExtentsFile': [getExtentsLeaf, getExtentsIndex],
                'AttributesFile': [getAttributesLeaf, getAttributesIndex] }
    
    strList = ["Leaf", "Index", "Header", "Map"]
    
    if curSType == None:
        etcData.append([data_block, BlockInfo])
        return None, None
    
    kindList = kindDict[curSType]
    kindList.extend([getHeaderNode, getMapNode])
    kind = unpack_from(">b", data_block, 8)[0] + 1
    nodeData = kindList[kind](data_block)
    
    d_bOff = bOffsetInfo(0, BlockInfo.bsize, None, nodeData, curSType+"_%s" %strList[kind], offset)
    return nodeData, d_bOff

def main():
    f = open(r"C:\Users\user\Desktop\Journal_4", 'rb')
    s = f.read()
    jParseList, pInfo, bOffList = journalParser(s)
    g = open(r"C:\TEMP\Result2-1.txt", 'w')
    h = open(r"C:\TEMP\Result2-2.txt", 'w')
    for i in jParseList:
        g.write("-----------\n")
        for j in i:
            g.write(str(j)+"\n")
    for i in bOffList:
        h.write("-----------\n")
        for j in i:
            h.write(str(j)+"\n")
    
    g.close()
    f.close()
    h.close()
        
if __name__ == '__main__':
    main()