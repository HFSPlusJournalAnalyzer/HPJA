'''
Created on 2015. 2. 8.

@author: biscuit
'''
from HFSPlus_GetInstance import *

etcData = []

def journalParser(journal_blob):
    pInfo = getparseInfo(journal_blob)
    jnl = memoryview(journal_blob)
    j_header = getJournalHeader(jnl)
    j_buf = jnl[pInfo.sect_size:]
    startOffset = getStart(j_buf, j_header.end) # setting the startOffset
    
    j_ParseList = journalBufferParser(j_buf, j_header, startOffset, [], pInfo)
    j_ParseList.insert(0, j_header)
    
    return j_ParseList, pInfo

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
        

def journalBufferParser(j_buffer, JournalHeader, startOffset, parseList, pInfo):
    if startOffset == (JournalHeader.end - pInfo.sect_size): # -0x200 for Journal Header area
        return parseList
    blh = getBlockListHeader(j_buffer[startOffset:])
    
    nextOffset = ( startOffset + blh.bytes_used ) % len(j_buffer)
    if nextOffset - startOffset != blh.bytes_used:
        curTrans = memoryview( j_buffer[startOffset:].tobytes() + j_buffer[:nextOffset].tobytes() )
    else: curTrans = j_buffer[startOffset:nextOffset]
    
    parseList.append(transParser(curTrans, pInfo))
    
    return journalBufferParser(j_buffer, JournalHeader, nextOffset, parseList, pInfo)

def transParser(trans, pInfo):
    blh = getBlockListHeader(trans)  # block list header
    bi_List = []  # list of block info's 
    data_offset = 0  # for computing the offset from the bottom of the transaction block, of the data-area.
    for i in range(blh.num_blocks-1):
        bi = getBlockInfo(trans[0x20+0x10*i:])
        data_offset += bi.bsize
        bi_List.append(bi)
    
    data_List = []
    data_area = trans[-data_offset:]
    for b in bi_List:
        dBlock = getDataBlock(data_area[:b.bsize], b, pInfo)
        if dBlock != None:
            data_List.append(dBlock)
        data_area = data_area[b.bsize:]
    
    return [blh, bi_List, data_List]

# auxiliary function ; To identify a data block.
def getDataBlock(data_block, BlockInfo, pInfo):
    global etcData
    data_sNum = BlockInfo.bnum / pInfo.blockMag
    
    curSType = ""
    for s in pInfo.sfLoc:
        for e in pInfo.sfLoc[s]:
            if e.isIn(data_sNum):
                curSType = s
                break
        if curSType != "":
            break
        
    raw_data = data_block.tobytes()
    if "H+\x00\x04" in raw_data:
        vh_off = raw_data.find("H+\x00\x04")
        return getVolumeHeader(data_block[vh_off:vh_off+0x200])
    if curSType == 'AllocationFile':
        return data_block
     
    kindDict = {'CatalogFile': [getCatalogLeaf, getCatalogIndex],
                'ExtentsFile': [getExtentsLeaf, getExtentsIndex],
                'AttributesFile': [getAttributesLeaf, getAttributesIndex] }
    
    if curSType == "":
        etcData.append([data_block, BlockInfo])
        return None
    
    kindList = kindDict[curSType]
    kindList.extend([getHeaderNode, getMapNode])
    kind = unpack_from(">b", data_block, 8)[0] + 1
    
    return kindList[kind](data_block)

def main():
    f = open(r"C:\Users\user\Desktop\Journal", 'rb')
    s = f.read()
    jParseList = journalParser(s)
    g = open(r"C:\result2.txt", 'w')
    for i in jParseList:
        g.write("-----------\n")
        for j in i:
            g.write(str(j)+"\n")
    
    g.close()
    f.close()
        
if __name__ == '__main__':
    main()