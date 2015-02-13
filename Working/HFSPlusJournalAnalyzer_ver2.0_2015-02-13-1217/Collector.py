import os
import re
from Utility import *
from HFSPlusFormat import *

if __name__=='__main__':
    main()

def volumeFinder():

    os.system('diskutil list')
    disk=raw_input('Input identifier of target disk : ')
    disk='/dev/r'+disk

    return disk


def journalExtractor(journalInfoBlock,disk,blockSize,select):
    
    JournalInfoBlock=DiskDump(disk,'JournalInfoBlock',1,journalInfoBlock*blockSize,0x74,select)
    
    flags=buffer(JournalInfoBlock,0,4)
    offset=buffer(JournalInfoBlock,0x24,8)
    size=buffer(JournalInfoBlock,0x2C,8)
    
    Journal=DiskDump(disk,'Journal',1,offset,size,select)

    return Journal

    
def specialFileExtractor(fileName,fileFork,disk,blockSize,select):
    
    specialFile=[]
    for i in range(4):

        DirectoryCleaning(fileName)

        fileContent=[]
        for i in range(8):
            fileContent.append(DiskDump(disk,'./{0}/{0}{1}'.format(fileName[i],j),blockSize,fileFork[i].extents[j].start,fileFork[i].extents[j].end,select))
        
        specialFile.append(''.join(fileContent))

    return specialFile


def main():

    specialFileName-['AllocationFile','ExtentsOverflowFile','CatalogFile','AttributesFile']

    Utility.DirectoryCleaning('transaction')
    Utility.DirectoryCleaning('result')

    disk=volumeFinder()

    select = (re.match('y?$',raw_input('Would you like to create image? [y/n] : '),re.I)!=None)
    
    print 'Collecting files...'
    volumeHeader=VolumeHeader(Utility.DiskDump(disk,'HFSPlusVolumeHeader',512,2,1,select))

    journal=journalExtractor(volumeHeader.journalInfoBlock,disk,volumeHeader.blockSize,select)

    if select:
        specialFileExtractor(specialFileName,volumeHeader.specialFileFork,disk,volumeHeader.blockSize,select)
    
    return (volumeHeader,journal,specialFile)
