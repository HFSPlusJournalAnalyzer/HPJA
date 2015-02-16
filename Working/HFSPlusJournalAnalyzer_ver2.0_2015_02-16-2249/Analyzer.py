from Utility import *
from struct import *
from HFSPlus_ParseModule import *
from HFSPlus_JournalTrack import *
from HFSPlus_sStructure import *
from types import MethodType
from collections import *
import types
import Collector
import sys
import datetime
import csv

def catalogFileAnalyzer(catalogFile,tranBlocks):

    modifiedNodes=[]
    for i in range(1,trnaBlock[0]+1):
        if tranBlocks[i].blockType[0]==2 and tranBlocks[i].offset not in modifiedNodes:
            modifiedNodes.append(tranBlocks[i].offset)

    nodeSize,temp1,totalNodes=unpack_from('>HHL',catalogFile,32)

    nodePointer=0
    for i in range(1,totalNodes):

        nodePointer+=nodeSize

        if nodePointer not in modifiedNodes and ord(catalogFile[nodePointer+8])==0xFF:

            numRecords=unpack_from('>H',catalogFile,nodePointer+10)

            for j in range(numRecords):

                offset=nodePointer+unpack_from('>H',catalogFile,nodePointer+nodeSize-2*(j+1))
                        
                keyLength=unpack_from('>H',catalogFile,offset)

                if unpack_from('>H',catalogFile,offset+keyLength+2)<3:

                    parentID=unpack_from('>L',catalogFile,offset+2)

                    for k in range(unpack_from('>H',catalogFile,offset+6)):
                        nodeName+=('\u'+catalogFile[offset+8+2*k].encode('hex')+catalogFile[offset+8+2*k+1].encode('hex')).decode('unicode-escape')

                    offset+=2+keyLength
                    
                    CNID=unpack_from('>L',catalogFile,offset+keyLength+0xA)

                elif unpack_from('>H',catalogFile,offset+keyLength+2)<5:

                    CNID=unpack_from('>L',catalogFile,offset+2)

                    offset+=2+keyLength
                    
                    parentID=unpack_from('>L',catalogFile,offset+4)

                    nodeName=u''
                    for k in range(unpack_from('>H',catalogFile,offset+8)):
                        nodeName+=('\u'+catalogFile[offset+2*k+10].encode('hex')+catalogFile[offset+2*k+11].encode('hex')).decode('unicode-escape')
                    
                nameAndParent[0][CNID]=[nodeName,parentID]


def parsingBlock(specialFileFork,allocBlockSize):

    nonLeafNode=[BTIndexNode,BTHeaderNode,BTMapNode]
    leafNodeType=[ExtentsLeafNode,CatalogLeafNode,AttrLeafNode]

    if self.offset==1024:

        self.blockType.append(4)
        self.content=VolumeHeader(self.content)
    
    for i in range(3):
        
        check=False
        offset=0

        for j in range(8):

            if specialFileFork[i].extents[j].startBlock*allocBlockSize<=self.offset<(specialFileFork[i].extents[j].startBlock+specialFileFork[i].extents[j])*allocBlockSize:
                offset+=self.offset-specialFileFork[i].extents[j].startBlock*allocBlockSize
                check=True
                break

            self.offset=offset+specialFileFork[i].extents[j].startBlock*allocBlockSize
            
        if check:

            self.blockType.append(i)

            if k>0:

                kind=ord(self.content[8])
                self.blockType.append(kind)

                if kind==255:
                    self.content=leafNodeType[i](self.content,size)

                else:
                    self.content=nonLeafNode[kind]

            else:
                self.allocDataAnalyzer()

            break


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


def initFullPath(self):

    nameAndParent[1][self.CNID]=[self.nodeName,self.parentID]
    fullPath=[]

    i=self.CNID
    while i in nameAndParent[1].keys():
        fullPath.insert(0,'/{0}'.format(nameAndParent[1][i][0]))
        i=nameAndParent[1][i][1]

    self.fullPath=u''.join(fullPath)
    self.unidentifiedAncestor=i


def completeFullPath(self):

    fullPath=[]

    i=self.unidentifiedAncestor
    while i!=1:

        if i not in nameAndParent[0].keys():

            self.fullPath='unknown'
            fullPath=[]
            break

        fullPath.insert(0,'/{0}'.format(nameAndParent[0][j][0]))
        i=nameAndParent[0][j][1]

    self.fullPath+=u''.join(fullPath)


def initFullPathOfRecords(self):

    self.records.initFullPath()


def completeFullPathOfRecords(self):

    self.records.completeFullPath()


def tranAnalyzer(tranBlocks,specialFileFork,allocBlockSize):

    TranBlock.parsingBlock=MethodType(parsingBlock,None,TranBlock)
    TranBlock.allocDataAnalyzer=MethodType(allocDataAnalyzer,None,TranBlock)
    ExtentDescriptor.__init__=MethodType(modifiedInit,None,ExtentDescriptor)
    CatalogDataRec.initFullPath=MethodType(initFullPath,None,CatalogDataRec)
    CatalogDataRec.completeFullPath=MethodType(completeFullPath,None,CatalogDataRec)
    CatalogLeafNode.initFullPathOfRecords=MethodType(initFullPathOfRecords,None,CatalogLeafNode)
    CatalogLeafNode.completeFullPathOfRecords=MethodType(completeFullPathOfRecords,None,CatalogLeafNode)

    for i in range(1,tranBlocks[0]+1):

        tranBlocks.parsingBlock(specialFileFork,allocBlockSize)

        if tranBlocks.blockType==[2,255]:
            tranBlocks.content.initFullPathOfRecords()

    catalogFileAnalyzer(catalogFile,tranBlocks)

    for i in range(1,tranBlocks[0]+1):
        if tranBlocks.blockType==[2,255]:
            tranBlocks.content.completeFullPathOfRecords()
                    

def DataRecovery(disk,deduplicatedRecord,blockSize):

    keyForFork=['dataFork','resourceFork']

    DirectoryCleaning('recovery')
    
    for i in range(1,deduplicatedRecord[0]+1):
        for j in range(1,deduplicatedRecord[i][0]+1):
            for k in range(1,deduplicatedRecord[i][j][0]+1):

                check=False
                for l in range(2):
                    for m in range(1,deduplicatedRecord[i][j][k][keyForFork[l]][0]+1):
                        if deduplicatedRecord[i][j][k][keyForFork[l]][m][0]==0:
                            check=True
                            break

                if check:
                    
                    fork=['','']
                    
                    for l in range(2):
                        
                        check=True
                        
                        for m in range(1,deduplicatedRecord[i][j][k][keyForFork[l]][0]+1):
                            if deduplicatedRecord[i][j][k][keyForFork[l]][m][0]==-1:
                                check=False
                            else:
                                fork[l]+=DiskDump(disk,'./recovery/{0}{1}{2}{3}{4}{5}{6}_'.format(i,j,k,deduplicatedRecord[i][j][k]['CNID'],deduplicatedRecord[i][j][k]['createDate'],keyForFork[l],m)+deduplicatedRecord[i][j][k]['nodeName'],blockSize,deduplicatedRecord[i][j][k][keyForFork[l]][m][1],deduplicatedRecord[i][j][k][keyForFork[l]][m][2])

                        if check:
                            f=open('./recovery/{0}{1}{2}{3}{4}{5}_'.format(i,j,k,deduplicatedRecord[i][j][k]['CNID'],deduplicatedRecord[i][j][k]['createDate'],keyForFork[l])+deduplicatedRecord[i][j][k]['nodeName'],'wb')
                            f.write(fork[l])
                            f.close()

                        
def main(option):

    if ('l' in option) or ('i' in option):

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

        specialFile=[]
        for i in ['al','e','c','at']:
            if i in option:

                f=open(option[i],'rb')
                specialFile.append(f.read())
                f.close()

            else:
                specialFile.append(0)

        allocationFile=temp[0]
        extentsFile=temp[1]
        catalogFile=temp[2]
        attributesFile=temp[3]

    print 'Analyzing journal...'
    jParseList=journalParser(journal)[0]
    #jT = journalTrack(jParseList)

    path='result{0}'.format(option['id'])

    DirectoryCleaning(path)

    f = open("{0}/result1.txt".format(path),'w')
    for i in jParseList:
        f.write("-----------\n")
        for j in i:
            f.write(str(j)+"\n")
    
    f.close()

    if vh!=0:
        f = open("{0}/VolumeInfo.txt".format(path),'w')
        for i in vh.__dict__:
            f.write('{0} : {1}\n'.format(i,vh.__dict__[j]))
    
    f.close()

    BTType=['Catalog', "Extents", "Attributes"]
    BTAttr=[list(OrderedDict.fromkeys(CatalogKey._fields+CatalogFile._fields+CatalogFolder._fields+CatalogThread._fields)),list(OrderedDict.fromkeys(ExtentsKey._fields+ExtentsDataRec._fields)),list(OrderedDict.fromkeys(AttrKey._fields+AttrForkData._fields+AttrExtents._fields+AttrData._fields))]

    f=[]
    for i in BTType:
        f.append(open('{0}/{1}.csv'.format(path,i),'w'))

    for i in range(0,3):
        for j in BTAttr[i]:
            f[i].write('{0},'.format(j))
        f[i].write('\n')

    for i in range(1,len(jParseList)):
        for j in range(len(jParseList[i][2])):

            try:

                for k in range(len(jParseList[i][2][j].LeafRecList)):

                    fi=BTType.find(jParseList[i][2][j].LeafRecList[k].getType())

                    for l in BTAttr[fi]:

                        if l in jParseList[i][2][j].LeafRecList[k].key.__dict__:

                            f[fi].write('{0},'.format(jParseList[i][2][j].LeafRecList[k].key.__dict__[l]).replace(',',':'))

                        elif l in jParseList[i][2][j].LeafRecList[k].record.__dict__:

                            f[fi].write('{0},'.format(jParseList[i][2][j].LeafRecList[k].record.__dict__[l]).replace(',',':'))

                        else:

                            f[fi].write(',')

                    f.write('\n')

            except AttributeError:
                pass

'''
    f = open("{0}/result2.txt".format(path),'w')
    for i in jT:
        f.write("-----------\n")
        for j in i:
            f.write(str(j)+"\n")

    f.close()

    
    print 'Analyzing CatalogFile...'
    Analyzer.CatalogFileAnalyzer(CatalogFile)

    print 'Analyzing transactions...'
    Analyzer.TransactionAnalyzer(tranBlocks,volumeHeader.specialFileFork,volumeHeader.blockSize)

    print 'Printing record list...'
    fName='./result/recordList.csv'
    f=open(fName,'w')
    for i in range(1,tranBlocks[0]+1):

        if 0<tranBlocks.blockType[0]<4:

            for j in range(tranBlocks.content.numRecords):

                f.write(str(tranBlocks[i]))
                f.write(str(tranBlocks.content.records[j]))

        else:

            f.write(str(tranBlocks[i]))

    f.close()
    
    if recovery:
        print 'Recoverying deleted files...'
        Analyzer.DataRecovery(disk,,volumeHeader.blockSize)
    '''

if __name__=='__main__':
    main(translatingInput(sys.argv))