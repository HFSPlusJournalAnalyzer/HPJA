from Utility import *
from struct import *
from HFSPlus_ParseModule import *
from HFSPlus_JournalTrack import *
from HFSPlus_sStructure import *
from types import MethodType
from collections import *
from Output import *
import types
import Collector
import sys
import datetime
import csv

def specialFileAnalyzer(path,specialFile):

    fileType=['Extents','Catalog','Attributes']

    f=[]
    fstruct={}

    for i in range(3):

        sf=specialFile[i]
        if sf==0:
            break
        ft=fileType[i]

        f.append({})
        fp=f[i]

        for j,k in enumerate(["Leaf", "Index", "Header"]):
            fp[j]=open('{0}/{1}{2}'.format(path,ft,j))

        nodeSize,temp1,totalNodes=unpack_from('>HHL',sf,32)

        nodePointer=0
        for j in xrange(totalNodes):

            node=getBlock(buffer(sf,nodePointer,nodeSize),ft)
            index=node.kind+1

            if index<3:

                records=blocks[1]

                if type(records)==list:
                    for l in records:
                        outputRecords(fp[index],l)

                else:
                    outputRecords(fp[index],records)

                if i==1 and index==0:
                    for k in blocks.LeafRecList:
                        if k.record.recordType<2:
                            fstruct[k.key.parentID]=[k.record.nodeName.nodeUnicode,k.record.parentID]

            nodePointer+=nodeSize

    return fstruct
'''
def allocDataAnalyzer(self):

    allocatedBlock=[0]
    bitOffset=self.offset*8
    start=-1
    for k in range(size):
        for l in range(8):

            if start==-1 and (ord(self.content[k])>>(7-l))%2==1:
                start==k*8+l

            elif start!=-1 and (ord(self.content[k])>>(7-l))%2==0:

                allocatedBlock[0]+=1
                allocatedBlock.append((start+bitOffset,k*8+l-start))
                start=-1
    
    for k in range(1,existentExtent[0]+1):

        if existentExtent[k].state==1:

            check=0

            if RangeChecking(bitOffset,self.size*8,existentExtent[k].startBlock,existentExtent[k].blockCount)==2:
                
                check=1
                for l in range(1,allocatedBlock[0]+1):
                    if RangeChecking(allocatedBlock[l][0],allocatedBlock[l][1],existentExtent[k].startBlock,existentExtent[k].blockCount):
                        check=2
                        break
                        
            elif bitOffset<=existentExtent[k].startBlock<bitOffset+tranLen*8:
                
                check=1
                for l in range(1,allocatedBlock[0]+1):
                    if allocatedBlock[l][0]<=existentExtent[k].startBlock and allocatedBlock[l][0]+allocatedBlock[l][1]==bitOffset+tranLen*8:
                        check=2
                        break

            elif bitOffset<existentExtent[k].startBlock+existentExtent[k].blockCount<=bitOffset+tranLen*8:

                check=1
                for l in range(1,allocatedBlock[0]+1):
                    if allocatedBlock[l][0]==bitOffset and allocatedBlock[l][0]+allocatedBlock[l][1]>=existentExtent[k].startBlock+existentExtent[k].blockCount:
                        check=2
                        break

            if check==2:
                allocatedBlock.pop(l)
                allocatedBlock[0]-=1

            elif check==1:
                existentExtent[k].state=0


def modifiedInit(self):

    self.startBlock,self.blockCount=unpack('>LL')

    if self.startBlock!=0 or self.blockCount!=0:

        n=1
        while n<=existentExtent[0]:

            if RangeChecking(existentExtent[n].startBlock,existentExtent[n].blockCount,self.startBlock,self.blockCount)>0:

                existentExtent[n].state=-1
                existentExtent.pop(n)
                existentExtent[0]-=1
                n-=1

            n+=1

        existentExtent[0]+=1
        existentExtent.append(self)
'''

def getFullPath(CNID,fstruct):

    fullPath=[]

    i=CNID
    while i!=1:

        if i not in fstruct.keys():
            fullPath=['unknown']
            break

        fullPath.insert(0,u'{0}/'.format(fstruct[CNID][0]))
        i=fstruct[CNID][1]

    fullPath=u''.join(fullPath)

    return fullPath


def main(option):

    if 'i' in option:

        temp=Collector.main(option)
        journal=temp[0]
        vh=temp[1]
        allocationFile=temp[2]
        extentsFile=temp[3]
        catalogFile=temp[4]
        attributesFile=temp[5]

    else:

        f=open(option['j'],'rb')
        journal=f.read()
        f.close()

        files=[]
        for i in ['v','al','e','c','at']:
            if i in option:

                f=open(option[i],'rb')
                files.append(f.read())
                f.close()

            else:
                files.append(0)

        vh=files[0]
        allocationFile=files[1]
        extentsFile=files[2]
        catalogFile=files[3]
        attributesFile=files[4]

    print 'Analyzing journal...'
    jParseList=journalParser(journal)[0]
    #jT = journalTrack(jParseList)

    path='result{0}'.format(option['id'])

    DirectoryCleaning(path)

    rawCSV(path,jParseList)
    rawSQLite3(path,jParseList)

    if 'r' in option:
        recovery(option['l'],path,option['r'],jParseList,vh)

if __name__=='__main__':
    main(translatingInput(sys.argv))