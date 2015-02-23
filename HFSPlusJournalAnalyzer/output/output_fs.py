'''
Created on 2015. 2. 16.

@author: biscuit
'''
from analysis.hfs_parse import *
import os, shutil
import time

def getFSOutput(journal_blob, j_ParseList, pInfo, bOffData, rPath="."):
    j_view = memoryview(journal_blob)
    stPath = os.getcwd()
    os.chdir(os.path.dirname(rPath))
    rtFoldName = time.strftime("%Y%m%d_%H-%M-%S_Journal.dump", time.localtime())
    os.mkdir(rtFoldName)
    os.chdir("./"+rtFoldName)
        
    # codes for printing basic information of whole journal
    
    lenBuf = len(j_view)-pInfo.sect_size
    for i, bOff in enumerate(bOffData):
        bOffDump(bOff, j_view, i, lenBuf)
        
    os.chdir(stPath)

def bOffDump(bOff, j_buf, count, mod):
    initPath = os.getcwd()
    fName = "%02d %s" %(count, bOff.name)
    start = (bOff.start + bOff.offset) % mod
    end = (bOff.end + bOff.offset) % mod
    if bOff.contain == None:
        with open(fName+".bin", "wb") as b:
            b.write(getBufContent(j_buf, start, end).tobytes())
        
        # codes for printing info of data (use bOff.data)
        
    else:
        os.mkdir(fName)
        os.chdir("./"+fName)
        for i, c in enumerate(bOff.contain):
            bOffDump(c, j_buf, i, mod)
                
        os.chdir(initPath)
        
def main():
    f = open(r"C:\Users\user\Desktop\Journal_4", 'rb')
    s = f.read()
    jParseList, pInfo, bOffList = journalParser(s)
    getFSOutput(s, jParseList, pInfo, bOffList, r"C:\TEMP\\")
    
if __name__ == '__main__':
    main()
    