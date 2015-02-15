import os
import shutil
from struct import *

def unpackLarge(fmt,string):
    
    result=0
    size=int(buffer(fmt,1,len(fmt)-1))
    
    if fmt[0]=='>':

        for i in range(size):
            result=result*256+ord(string[i])

    elif fmt[0]=='<':

        for i in range(size-1,-1,-1):
            result=result*256+ord(string[i])

    else:
        return 'Unsupported mode'

    return result


def unpackLarge_from(fmt,string,offset=0):

    unpackLarge(fmt,buffer(string,offset,len(string)-offset))


def DiskDump(inputFile, outputFile, bs, skip, count, select=False):

    fi=open(inputFile,'rb')
    
    fi.seek(bs*skip)
    dump = fi.read(bs*count)

    if select:
        print 'Creating '+outputFile+'...'
        fo = open('temp','wb')
        fo.write(dump)
        fo.close()
        os.rename('temp',outputFile)

    fi.close()
    
    return dump


def DirectoryCleaning(directory):
    
    if os.path.isdir(directory):
        shutil.rmtree(directory)

    os.mkdir(directory)


def VerifyChecksum(headerType,endian,ptr,length):

    cksum=0
    
    if headerType=='blhdr':
        for i in range(0,length):
            if 8<=i<12:
                cksum=cksum<<8 ^ cksum
            else:
                cksum=cksum<<8 ^ cksum+ord(ptr[i])

    if ~cksum & 0xFFFFFFFF==unpack(endian+'L',ptr[8:12]):
        return True
    else:
        return False


def RangeChecking(base,size,startBlock,blockCount=0):

    return (base<=startBlock<base+size)+(base<startBlock+blockCount<=base+size)