'''
Created on 2015. 2. 8.

@author: biscuit
'''
from HFSPlus_GetInstance import *

def journalParser(journal_blob):
    jnl = memoryview(journal_blob)
    j_header = getJournalHeader(jnl[:0x200])
    j_buf = jnl[0x200:]
    '''
    Some codes for identifying 'startOffset'
    ''' 
    j_ParseList = journalBufferParser(j_buf, j_header, 0, [])
    j_ParseList.insert(0, j_header)
    
    return j_ParseList
    

def journalBufferParser(j_buffer, JournalHeader, startOffset, parseList):
    if startOffset == (JournalHeader.end - 0x200): # -0x200 for Journal Header area
        return parseList
    blh = getBlockListHeader(j_buffer[startOffset:])
    
    nextOffset = ( startOffset + blh.bytes_used ) % len(j_buffer)
    if nextOffset - startOffset != blh.bytes_used:
        curTrans = memoryview( j_buffer[startOffset:].tobytes() + j_buffer[:nextOffset].tobytes() )
    else: curTrans = j_buffer[startOffset:startOffset+blh.bytes_used]
    
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
    
    return [bi_List, data_List]

# auxiliary function ; To identify a data block.
def getDataBlock(data_block, BlockInfo):
    if BlockInfo.bsize == 0x200:
        return getVolumeHeader(data_block)
    if BlockInfo.bsize == 0x1000:
        return data_block
    if BlockInfo.bsize == 0x2000:
        kindList = [getCatalogLeaf, getCatalogIndex, getCatalogHeader, getCatalogMap]
        kind = unpack_from(">b", data_block, 8)[0] + 1
        return kindList[kind](data_block)

