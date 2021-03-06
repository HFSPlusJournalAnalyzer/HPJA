'''
Created on 2015. 2. 8.

@author: biscuit
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


def journalParser(journal_blob):

    if unpack_from('>L',journal,4)==0x12345678:
        endian='>'
    else:
        endian='<'

    jnl = memoryview(journal_blob)

    j_header=getJournalHeader(endian,jnl[:0x200])
    
    return (j_header,journalBufferParser(endian,j_header,jnl[0x200:]))

"""
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
    else: curTrans = j_buffer[startOffset:nextOffset]
    
    parseList.append(transParser(curTrans))
    
    return journalBufferParser(j_buffer, JournalHeader, nextOffset, parseList)
    """

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
    if BlockInfo.bsize == 0x200:
        return getVolumeHeader(data_block)
    if BlockInfo.bsize == 0x1000:
        return data_block
    if BlockInfo.bsize == 0x2000:
        kindList = [getCatalogLeaf, getCatalogIndex, getCatalogHeader, getCatalogMap]
        kind = unpack_from(">b", data_block, 8)[0] + 1
        return kindList[kind](data_block)

