import os
import shutil

def BytesToValue(byte,endian=0x12345678):
    
    result=0
    
    if endian==0x12345678:
        for i in byte:
            result=result*256+int(i.encode('hex'),16)
    elif endian==0x78563412:
        temp=byte[::-1]
        for i in temp:
            result=result*256+int(i.encode('hex'),16)

    return result



#def DiskDump(inputFile,outputFile,bs,skip,count):
#os.system('dd if={0} of=temp bs={1} skip={2} count={3}'.format(inputFile,bs,skip,count))
def DiskDump(inputFile, outputFile, bs, skip, count, select=True):

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
    
    if headerType=='block list header':
        for i in range(0,length):
            if 8<=i<0xC:
                cksum=cksum<<8 ^ cksum
            else:
                cksum=cksum<<8 ^ cksum+BytesToValue(ptr[i])

    if ~cksum & 0xFFFFFFFF==BytesToValue(ptr[8:0xC],endian):
        return True
    else:
        return False
