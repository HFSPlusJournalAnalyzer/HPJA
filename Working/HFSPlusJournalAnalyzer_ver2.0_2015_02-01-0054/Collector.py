import os
from Utility import *
from HFSPlusFormat import *

def VolumeFinder():

    os.system('diskutil list')
    disk=raw_input('Input identifier of target disk : ')
    disk='/dev/r'+disk

    return disk


def JournalExtractor(journalInfoBlock,disk,blockSize,select):
    
    JournalInfoBlock=DiskDump(disk,'JournalInfoBlock',1,journalInfoBlock*blockSize,0x74,select)
    
    flags=BytesToValue(JournalInfoBlock[0:4])
    offset=BytesToValue(JournalInfoBlock[0x24:0x2C])
    size=BytesToValue(JournalInfoBlock[0x2C:0x34])
    
    Journal=DiskDump(disk,'Journal',1,offset,size,select)

    return Journal

    
def SpecialFileExtractor(fileName,fileInfo,disk,blockSize,select):
    
    fileContent=''

    DirectoryCleaning(fileName)
    
    for i in range(1,fileInfo[2][0]+1):
        fileContent+=DiskDump(disk,'./{0}/{0}{1}'.format(fileName,i),blockSize,fileInfo[2][i][0],fileInfo[2][i][1],select)
        
    return fileContent
