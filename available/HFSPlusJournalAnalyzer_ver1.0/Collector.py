import os
import re
from Utility import *

def VolumeFinder():

    os.system('diskutil list')
    disk=raw_input('Input identifier of target disk : ')
    disk='/dev/r'+disk
    select = (raw_input('Would you like to create image? [y/n] : ').lower()=='y')
    recovery = (raw_input('Would you like to recover the image? [y/n] : ').lower()=='y')
    return (disk,select,recovery)
    


def VolumeHeaderParser(HFSPlusVolumeHeader):

    signature=BytesToValue(HFSPlusVolumeHeader[0:2])
    version=BytesToValue(HFSPlusVolumeHeader[2:4])
    attributes=BytesToValue(HFSPlusVolumeHeader[4:8])
    lastMountedVersion=BytesToValue(HFSPlusVolumeHeader[8:0xC])
    journalInfoBlock=BytesToValue(HFSPlusVolumeHeader[0xC:0x10])
    createDate=BytesToValue(HFSPlusVolumeHeader[0x10:0x14])
    modifyDate=BytesToValue(HFSPlusVolumeHeader[0x14:0x18])
    backupDate=BytesToValue(HFSPlusVolumeHeader[0x18:0x1C])
    checkedDate=BytesToValue(HFSPlusVolumeHeader[0x1C:0x20])
    fileCount=BytesToValue(HFSPlusVolumeHeader[0x20:0x24])
    folderCount=BytesToValue(HFSPlusVolumeHeader[0x20:0x24])
    folderCount=BytesToValue(HFSPlusVolumeHeader[0x24:0x28])
    blockSize=BytesToValue(HFSPlusVolumeHeader[0x28:0x2C])
    totalBlocks=BytesToValue(HFSPlusVolumeHeader[0x2C:0x30])
    freeBlocks=BytesToValue(HFSPlusVolumeHeader[0x30:0x34])
    dataClumpSize=BytesToValue(HFSPlusVolumeHeader[0x3C:0x40])
    writeCount=BytesToValue(HFSPlusVolumeHeader[0x44:0x48])
    encodingsBitmap=BytesToValue(HFSPlusVolumeHeader[0x48:0x50])

    specialFileInfo=[]
    
    offset=0x70
    for i in range(0,3):
        
        specialFileInfo.append([BytesToValue(HFSPlusVolumeHeader[offset:offset+8])])
        specialFileInfo[i].append(BytesToValue(HFSPlusVolumeHeader[offset+0xC:offset+0x10]))
        specialFileInfo[i].append([0])

        offset+=0x10
        for j in range(0,8):

            startBlock=BytesToValue(HFSPlusVolumeHeader[offset:offset+4])
            blockCount=BytesToValue(HFSPlusVolumeHeader[offset+4:offset+8])

            if startBlock!=0 and blockCount!=0:
                specialFileInfo[i][2][0]+=1
                specialFileInfo[i][2].append((startBlock,blockCount))

            offset+=8
    
    return (blockSize,journalInfoBlock,specialFileInfo)



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
