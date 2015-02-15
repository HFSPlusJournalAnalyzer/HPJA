import sys
import time
import os
import re
from Utility import *
from HFSPlusFormat import *

if __name__=='__main__':
    main(translatingInput(sys.argv))

def journalExtractor(disk,vh,select):
    
    JournalInfoBlock=DiskDump(disk,'JournalInfoBlock',1,vh.journalInfoBlock*vh.blockSize,0x74)
    
    flags=unpack_from('>I',buffer(JournalInfoBlock,0))[0]
    offset=unpack_from('>Q',buffer(JournalInfoBlock,0x24))[0]
    size=unpack_from('>Q',buffer(JournalInfoBlock,0x2C))[0]
    
    Journal=DiskDump(disk,'Journal',1,offset,size,select)

    return Journal

    
def specialFileExtractor(disk,vh,select):
    
    specialFileName=['allocationFile','extentsFile','catalogFile','attributesFile']
    specialFile=[]
    for i in range(4):

        DirectoryCleaning(specialFileName[i])

        fileContent=[]
        for i in range(8):
            fileContent.append(DiskDump(disk,'./{0}/{0}{1}'.format(specialFileName[i],j),vh.blockSize,vh.__dict__[specialFileName[i]].extents[j].start,vh.__dict__[specialFileName[i]].extents[j].end,select))
        
        specialFile.append(''.join(fileContent))

    return specialFile


def main(option):

    select='d' in option

    if select:
        os.mkdir('dump_{0}_{1}'.format(option['n'],time.strftime('%Y-%m-%d-%H:%M:%S',time.localtime()))

    print 'Collecting files...'
    vh=getVolumeHeader(Utility.DiskDump(disk,'HFSPlusVolumeHeader',512,2,1,select))

    journal=journalExtractor(disk,vh,select)

    if select:
        temp=specialFileExtractor(disk,vh,select)
        allocationFile=temp[0]
        extentsFile=temp[1]
        catalogFile=temp[2]
        attributesFile=temp[3]
    
    return (journal,vh,allocationFile,extentsFile,catalogFile,attributesFile)
