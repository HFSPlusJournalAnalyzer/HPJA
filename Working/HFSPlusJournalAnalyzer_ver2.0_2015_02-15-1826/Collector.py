import sys
import time
import os
import re
from Utility import *
from HFSPlus_sStructure import *
from HFSPlus_getInstance import *

def journalExtractor(disk,vh,select,path):
    
    JournalInfoBlock=DiskDump(disk,'JournalInfoBlock',1,vh.journalInfoBlock*vh.blockSize,0x74)
    
    flags=unpack_from('>I',buffer(JournalInfoBlock,0))[0]
    offset=unpack_from('>Q',buffer(JournalInfoBlock,0x24))[0]
    size=unpack_from('>Q',buffer(JournalInfoBlock,0x2C))[0]
    
    Journal=DiskDump(disk,'dump{0}/Journal'.format(path),1,offset,size,select)

    return Journal

    
def specialFileExtractor(disk,vh,select,path):
    
    specialFileName=['allocationFile','extentsFile','catalogFile','attributesFile']
    specialFile=[]
    for i in range(4):

        DirectoryCleaning(specialFileName[i])

        fileContent=[]
        for j in range(8):
            if vh.__dict__[specialFileName[i]].extents[j].startBlock!=0 or vh.__dict__[specialFileName[i]].extents[j].blockCount!=0:
                fileContent.append(DiskDump(disk,'{0}/{1}{2}'.format(path,specialFileName[i],j),vh.blockSize,vh.__dict__[specialFileName[i]].extents[j].startBlock,vh.__dict__[specialFileName[i]].extents[j].blockCount,select))
        
        specialFile.append(''.join(fileContent))

    return specialFile


def main(option):

    select='d' in option

    if 'l' in option:
        disk=option['l']

    if 'i' in option:
        disk=option['i']

    path='dump_{0}'.format(option['id'])

    if select:
        DirectoryCleaning(path)


    print 'Collecting files...'
    vh=getVolumeHeader(DiskDump(disk,'{0}/HFSPlusVolumeHeader'.format(path),512,2,1,select))

    journal=journalExtractor(disk,vh,select,path)

    if select:
        temp=specialFileExtractor(disk,vh,select,path)
        allocationFile=temp[0]
        extentsFile=temp[1]
        catalogFile=temp[2]
        attributesFile=temp[3]

    else:
        allocationFile=0
        extentsFile=0
        catalogFile=0
        attributesFile=0
    
    return (journal,vh,allocationFile,extentsFile,catalogFile,attributesFile)


if __name__=='__main__':
    main(translatingInput(sys.argv))