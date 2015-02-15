
'''
Created on 2015. 2. 8.

@author: biscuit
'''
'''
from HFSPlus_GetInstance import *

def journalBufferParser(endian,journalBuffer):

    blhdrPointer=base
    bnext=0
    tranNum=0
    blockNum=0
    tranBlocks=[0]

    while not VerifyChecksum('blhdr',endian,journalBuffer[blhdrPointer%size:(blhdrPointer+32)%size],32):
        blhdrPointer+=jhdr_size

    while blhdrPointer<base+size:

        if bnext==0:
            tranNum+=1
            blockNum=0
            
        max_blocks,num_blocks,bytes_used,checksum,pad,temp1,bnext=unpack_from(endian+'HHLLLQL',journalBuffer,blhdrPointer%size)

        blPointer=blhdrPointer+blhdr_size
        blhdrPointer+=32

        for i in range(1,num_blocks):

            blockNum+=1
            tranBlocks[0]+=1
            
            bnum,bsize=unpack_from(endian+'LL',journalBuffer,blhdrPointer%size)
                
            if blPointer<size and blPointer+bsize>=size:
                tranBlocks.append(RawBlock(blPointer,tranNum,blockNum,bnum,bsize,jhdr_size,journalBuffer[blPointer:size]+journalBuffer[0:(blPointer+bsize)%size]))
                            
            else:
                tranBlocks.append(RawBlock(blPointer,tranNum,blockNum,bnum,bsize,jhdr_size,journalBuffer[blPointer%size:(blPointer+bsize)%size]))
            
            blPointer+=bsize

            blhdrPointer+=16
        
        blhdrPointer+=bytes_used-(num_blocks+1)*16
            
    return tranBlocks
'''

'''
Created on 2015. 2. 8.

@author: biscuit
'''
from HFSPlus_getInstance import *

sect_size = 0x200  # variable for storing a sector size 
blockMag = 8  # variable for storing a magnification of block from sect_size (blockSize/sect_size)
sfLoc = {}  # dict for storing the location of special files

def journalParser(journal_blob):
    global sect_size, blockMag, sfLoc
    vh_samInd = journal_blob.find("H+")
    jnl = memoryview(journal_blob)
    j_header = getJournalHeader(jnl)
    
    sect_size = j_header.jhdr_size
    vh = getVolumeHeader(journal_blob[vh_samInd:vh_samInd+sect_size])
    sfLoc['allocationFile'] = vh.allocationFile.extents
    sfLoc['extentsFile'] = vh.extentsFile.extents
    sfLoc['catalogFile'] = vh.catalogFile.extents
    sfLoc['attributesFile'] = vh.attributesFile.extents
    blockMag = vh.blockSize/sect_size
        
    j_buf = jnl[sect_size:]
    
    startOffset = getStart(j_buf, j_header.end) # setting the startOffset
    
    j_ParseList = journalBufferParser(j_buf, j_header, startOffset, [])
    j_ParseList.insert(0, j_header)
    
    return j_ParseList

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
        if cur == end:
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
        

def journalBufferParser(j_buffer, JournalHeader, startOffset, parseList):
    global sect_size
    if startOffset == (JournalHeader.end - sect_size): # -0x200 for Journal Header area
        return parseList
    blh = getBlockListHeader(j_buffer[startOffset:])
    
    nextOffset = ( startOffset + blh.bytes_used ) % len(j_buffer)
    if nextOffset - startOffset != blh.bytes_used:
        curTrans = memoryview( j_buffer[startOffset:].tobytes() + j_buffer[:nextOffset].tobytes() )
    else: curTrans = j_buffer[startOffset:nextOffset]
    
    parseList.append(transParser(curTrans))
    
    return journalBufferParser(j_buffer, JournalHeader, nextOffset, parseList)

def transParser(trans):
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
        data_List.append(getDataBlock(data_area[:b.bsize], b))
        data_area = data_area[b.bsize:]
    
    return [blh, bi_List, data_List]

# auxiliary function ; To identify a data block.
def getDataBlock(data_block, BlockInfo):
    global sect_size, sfLoc, blockMag
    
    data_sNum = BlockInfo.bnum / blockMag
    
    curSType = ""
    for s in sfLoc:
        for e in sfLoc[s]:
            if e.isIn(data_sNum):
                curSType = s
                break
        if curSType != "":
            break
        
    raw_data = data_block.tobytes()
    if "H+\x00\x04" in raw_data:
        vh_off = raw_data.find("H+\x00\x04")
        return getVolumeHeader(data_block[vh_off:vh_off+0x200])
    if curSType == 'allocationFile':
        return data_block
     
    kindDict = {'catalogFile': [getCatalogLeaf, getCatalogIndex],
                'extentsFile': [getExtentsLeaf, getExtentsIndex],
                'attributesFile': [getAttributesLeaf, getAttributesIndex] }
    
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