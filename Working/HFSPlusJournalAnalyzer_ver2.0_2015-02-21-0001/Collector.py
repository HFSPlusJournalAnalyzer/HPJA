import sys
import time
import os
import re
import gc
from Utility import *
from HFSPlus_sStructure import *
from HFSPlus_GetInstance import *

def journalCarving(disk,offset,path):

    fi=open(disk,'rb')
    maxSize=len(fi.read())
    fi.seek(offset)

    i=-1
    while True:
        try:
            while i==-1:
                image=fi.read()
                gc.collect()
                i=image.find('\x78\x4c\x4e\x4a\x78\x56\x34\x12')
                gc.collect()
                print fi.tell()
            fi.seek(i-maxSize,os.SEEK_CUR)
            gc.collect()
            jh=getJournalHeader(f.read(4096))
            gc.collect()
            fi.seek(i-4096,os.SEEK_CUR)
            fo=open('{0}/Journal_{1}'.format(path,fi.tell()),'wb')
            for j in range(jh.size/maxSize):
                fo.write(fi.read())
                gc.collect()
            image=fi.read()
            gc.collect()
            fo.write(image[:jh.size%maxSize])
            gc.collect()
            fo.close()
            gc.collect()
            i=image.find('\x78\x4c\x4e\x4a\x78\x56\x34\x12',jh.size%maxSize)
            gc.collect()

        except Exception:
            print fi.tell(),'error!'
            temp=fi.tell()
            fi.seek(1048576,os.SEEK_CUR)
            if temp==fi.tell():
                break
            
    
    fi.close()


def journalExtractor(disk,vh,select,path):
    
    JournalInfoBlock=DiskDump(disk,'JournalInfoBlock',1,vh.journalInfoBlock*vh.blockSize,0x74)
    
    flags=unpack_from('>I',buffer(JournalInfoBlock,0))[0]
    offset=unpack_from('>Q',buffer(JournalInfoBlock,0x24))[0]
    size=unpack_from('>Q',buffer(JournalInfoBlock,0x2C))[0]
    
    Journal=DiskDump(disk,'{0}/Journal'.format(path),1,offset,size,select)

    return Journal

    
def specialFileExtractor(disk,vh,select,path):
    
    specialFileName=['allocationFile','extentsFile','catalogFile','attributesFile']
    specialFile=[]
    for i in range(4):

        fileContent=[]
        for j in range(8):
            if vh.__getattribute__(specialFileName[i]).extents[j].startBlock!=0 or vh.__getattribute__(specialFileName[i]).extents[j].blockCount!=0:
                fileContent.append(DiskDump(disk,'{0}/{1}{2}'.format(path,specialFileName[i],j),vh.blockSize,vh.__getattribute__(specialFileName[i]).extents[j].startBlock,vh.__getattribute__(specialFileName[i]).extents[j].blockCount,select))
        
        specialFile.append(''.join(fileContent))

    return specialFile


def main(option):

    select='d' in option

    if 'i' in option:
        disk=option['i']

    path='dump_{0}'.format(option['id'])

    if select or 'carv' in option:
        DirectoryCleaning(path)


    print 'Collecting files...'
    vh=getVolumeHeader(DiskDump(disk,'{0}/HFSPlusVolumeHeader'.format(path),512,2,1,select))

    journal=journalExtractor(disk,vh,select,path)

    if 'carv' in option:
        journalCarving(disk,int(option['carv']),path)

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