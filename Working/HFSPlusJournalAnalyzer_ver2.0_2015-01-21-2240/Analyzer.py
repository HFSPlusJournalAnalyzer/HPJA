from Utility import *

existentFork=[0]
nameAndParent=[{},{}]

def JournalParser(journal):

    endian=BytesToValue(journal[4:8])
    start=BytesToValue(journal[8:0x10],endian)
    end=BytesToValue(journal[0x10:0x18],endian)
    size=BytesToValue(journal[0x18:0x20],endian)
    blhdr_size=BytesToValue(journal[0x20:0x24],endian)
    jhdr_size=BytesToValue(journal[0x28:0x2C],endian)
    
    blhdrPointer=end
    turn=False
    jbsize=size-jhdr_size
    bnext=0
    transaction=[0]

    while not VerifyChecksum('block list header',endian,journal[blhdrPointer:blhdrPointer+0x20],0x20):
        blhdrPointer+=jhdr_size
        if blhdrPointer==size:
            blhdrPointer=jhdr_size
            turn=True

    while blhdrPointer<end or not turn:

        if bnext==0:
            transaction[0]+=1
            transaction.append([0])
            
        num_blocks=BytesToValue(journal[blhdrPointer+2:blhdrPointer+4],endian)
        bytes_used=BytesToValue(journal[blhdrPointer+4:blhdrPointer+8],endian)
        bnext=BytesToValue(journal[blhdrPointer+0x1C:blhdrPointer+0x20],endian)

        blPointer=blhdrPointer+blhdr_size
        if blPointer>=size:
            blPointer-=jbsize

        blhdrPointer+=0x20
        jhdr_div16=jhdr_size/16
        num_sectors=(num_blocks+1)/jhdr_div16+1

        for i in range(0,num_sectors):
            
            if i<num_sectors-1:
                k=jhdr_div16
            else:
                k=(num_blocks+1)%jhdr_div16
            
            if i==0:
                k-=2
            
            for j in range(0,k):
                bnum=BytesToValue(journal[blhdrPointer:blhdrPointer+8],endian)
                bsize=BytesToValue(journal[blhdrPointer+8:blhdrPointer+0xC],endian)
                
                transaction[transaction[0]][0]+=1
                    
                if blPointer+bsize>size:
                    transaction[transaction[0]].append([bnum,journal[blPointer:size]+journal[jhdr_size:blPointer+bsize-jbsize]])
                    blPointer+=bsize-jbsize
                                
                else:
                    transaction[transaction[0]].append([bnum,journal[blPointer:blPointer+bsize]])
                    blPointer+=bsize

                blhdrPointer+=0x10

            if blhdrPointer==size:
                blhdrPointer=jhdr_size

        
        blhdrPointer+=bytes_used-(num_blocks+1)*0x10
        if blhdrPointer>=size:
            blhdrPointer-=jbsize
            turn=1
        

            
    return (jhdr_size,transaction)


def CatalogFileAnalyzer(catalogFile,modifiedNodes):

    nodeSize=BytesToValue(catalogFile[0x20:0x22])
    totalNodes=BytesToValue(catalogFile[0x24:0x28])

    nodePointer=0
    for i in range(1,totalNodes):

        nodePointer+=nodeSize

        if nodePointer not in modifiedNodes and BytesToValue(catalogFile[nodePointer+8])==0xFF:

            numRecords=BytesToValue(catalogFile[nodePointer+0xA:nodePointer+0xC])

            for j in range(0,numRecords):

                offset=nodePointer+BytesToValue(catalogFile[nodePointer+nodeSize-2*(j+1):nodePointer+nodeSize-2*j])                
                        
                keyLength=BytesToValue(catalogFile[offset:offset+2])

                if BytesToValue(catalogFile[offset+keyLength+2:offset+keyLength+4])<3:

                    parentID=BytesToValue(catalogFile[offset+2:offset+6])

                    for k in range(0,BytesToValue(catalogFile[offset+6:offset+8])):
                        nodeName+=('\u'+catalogFile[offset+8+2*k].encode('hex')+catalogFile[offset+8+2*k+1].encode('hex')).decode('unicode-escape')

                    offset+=2+keyLength
                    
                    CNID=BytesToValue(catalogFile[offset+keyLength+0xA:offset+keyLength+0xE])

                if 2<BytesToValue(catalogFile[offset+keyLength+2:offset+keyLength+4])<5:

                    CNID=BytesToValue(catalogFile[offset+2:offset+6])

                    offset+=2+keyLength
                    
                    parentID=BytesToValue(catalogFile[offset+4:offset+8])

                    nodeName=u''    
                    for k in range(0,BytesToValue(catalogFile[offset+8:offset+0xA])):
                        nodeName+=('\u'+catalogFile[offset+0xA+2*k].encode('hex')+catalogFile[offset+0xA+2*k+1].encode('hex')).decode('unicode-escape')
                    
                nameAndParent[0][CNID]=[nodeName,parentID]


def ForkAnalyzer(rawFork,parsedFork,createDate,CNID):

    for i in range(0,2):
                         
        parsedFork[i]['logicalSize']=BytesToValue(rawFork[80*i:80*i+8])
        parsedFork[i]['clumpSize']=BytesToValue(rawFork[80*i+8:80*i+12])
        parsedFork[i]['totalBlocks']=BytesToValue(rawFork[80*i+12:80*i+16])
        parsedFork[i]['extents']=[]
        
        for j in range(0,8):

            parsedFork[i]['extents'][j].append({})

            startBlock=BytesToValue(rawFork[80*i+8*j+16:80*i+8*j+20])
            parsedFork[i]['extents'][j]['startBlock']=startBlock

            blockCount=BytesToValue(rawFork[80*i+8*j+20:80*i+8*j+24])
            parsedFork[i]['extents'][j]['blockCount']=blockCount

            parsedFork[i]['extents'][j]['state']='allocated'

            if startBlock!=0 and blockCount!=0:

                n=1
                while n<=existentFork[0]:

                    if (existentFork[n]['createDate']!=createDate or existentFork[n]['CNID']!=CNID) and RangeChecking((existentFork[n]['startBlock'],existentFork[n]['startBlock']+existentFork['blockCount']),(startBlock,startBlock+blockCount))>0:

                        existentFork[n][0][0]=-1
                        existentFork.pop(n)
                        existentFork[0]-=1
                        n-=1

                    n+=1

    for i in range(0,2):
        for j in range(1,parsedFork[l][0]+1):
            existentFork[0]+=1
            existentFork.append([parsedFork[i]['extents'][j],createDate,CNID])


def FileAndFolderRecordParser(rawRecord,parsedRecord):

    parsedRecord['parentID']=BytesToValue(parsedRecord['key'][0:4])

    nodeName=u''
    for i in range(0,BytesToValue(parsedRecord['key'][4:6])):
        nodeName+=('\u'+parsedRecord['key'][6+2*i].encode('hex')+parsedRecord['key'][6+2*i+1].encode('hex')).decode('unicode-escape')

    parsedRecord['flags']=BytesToValue(rawRecord[2:4])
    CNID=BytesToValue(rawRecord[8:12])
    parsedRecord['CNID']=CNID
    createDate=BytesToValue(rawRecord[12:16])
    parsedRecord['createDate']=createDate
    parsedRecord['contentModDate']=BytesToValue(rawRecord[16:20])
    parsedRecord['attributeModDate']=BytesToValue(rawRecord[20:24])
    parsedRecord['accessDate']=BytesToValue(rawRecord[24:28])
    parsedRecord['backupDate']=BytesToValue(rawRecord[28:32])
    parsedRecord['ownerID']=BytesToValue(rawRecord[32:36])
    parsedRecord['groupID']=BytesToValue(rawRecord[36:40])
    parsedRecord['adminFlags']=BytesToValue(rawRecord[40:41])
    parsedRecord['ownerFlags']=BytesToValue(rawRecord[41:42])
    parsedRecord['fileMode']=BytesToValue(rawRecord[42:44])
    parsedRecord['special']=BytesToValue(rawRecord[44:48])
    parsedRecord['userInfo']=BytesToValue(rawRecord[48:64])
    parsedRecord['finderInfo']=BytesToValue(rawRecord[64:80])
    parsedRecord['textEncoding']=BytesToValue(rawRecord[80:84])

    if recordType==2:

        parsedRecord['reserved1']=BytesToValue(rawRecord[4:8])
        parsedRecord['reserved2']=BytesToValue(rawRecord[84:88])

        parsedFork=[{},{}]
        ForkAnalyzer(rawRecord[88:248],parsedRecord,createDate,CNID)

        parsedRecord['dataFork']=parsedFork[0]
        parsedRecord['resourceFork']=parsedFork[1]

    elif recordType==1:

        parsedRecord['valence']=BytesToValue(rawRecord[4:8])
        parsedRecord['folderCount']=BytesToValue(rawRecord[84:88])


def ThreadRecordParser(rawRecord,parsedRecord):

    parsedRecord['CNID']=BytesToValue(parsedRecord['key'][0:4])
    parsedRecord['reserved']=BytesToValue(rawRecord[2:4])
    parsedRecord['parentID']=BytesToValue(rawRecord[4:8])

    nodeName=u''

    for l in range(0,BytesToValue(rawRecord[8:10])):
        nodeName+=('\u'+rawRecord[10+2*l].encode('hex')+rawRecord[10+2*l+1].encode('hex')).decode('unicode-escape')

    parsedRecord['nodeName']=nodeName


def CatalogDataRecordParser(rawRecord,parsedRecord):
    
    DataRecordParser=[FileAndFolderRecordParser,ThreadRecordParser]

    recordType=BytesToValue(rawRecord[0:2])
    parsedRecord['recordType']=recordType

    DataRecordParser[(recordType-1)/2](rawRecord,parsedRecord)

    parsedRecord['nodeName']=nodeName.replace('/',':')

    nameAndParent[1][parsedRecord['CNID']]=[parsedRecord['nodeName'],parsedRecord['parentID']]

    fullPath=u''

    j=parsedRecord['CNID']
    while j in nameAndParent[1].keys():
        fullPath='/'+nameAndParent[1][j][0]+fullPath
        j=nameAndParent[1][j][1]

    parsedRecord['unidentifiedAncestor']=j
    parsedRecord['fullPath']=fullPath


def ExtentsDataRecordParser(rawRecord,parsedRecord):

    parsedRecord['parentID']=BytesToValue(parsedRecord['key'][0:4])

    nodeName=u''
    for i in range(0,BytesToValue(parsedRecord['key'][4:6])):
        nodeName+=('\u'+parsedRecord['key'][6+2*i].encode('hex')+parsedRecord['key'][6+2*i+1].encode('hex')).decode('unicode-escape')


def BtreeNodeParser(classification,rawTransaction,parsedTransaction,tranLen):

    DataRecordParser=[CatalogDataRecordParser,ExtentsDataRecordParser,AttributesDataRecordParser]

    kind=BytesToValue(rawTransaction[8])

    if kind==0 or kind==0xFF:
        
        numRecords=BytesToValue(rawTransaction[0xA:0xC])
        parsedTransaction.append(numRecords)

        for i in range(1,numRecords+1):

            start=BytesToValue(rawTransaction[tranLen-2*(i+1):tranLen-2*i])
            end=BytesToValue(rawTransaction[tranLen-2*(i+2):tranLen-2*(i+1)])

            parsedTransaction.append({})
            
            keyLength=BytesToValue(rawTransaction[start:start+2])
            parsedTransaction[i]['keyLength']=keyLength
            parsedTransaction[i]['key']=rawTransaction[start+2:start+keyLength+2]
            
            if kind==0xFF:

                DataRecordParser[classification](rawTransaction[start+keyLength:end],parsedTransaction[i])

            if kind==0:

                parsedTransaction[i]['nodeNumber']=BytesToValue(rawTransaction[start+keyLength+2:start+keyLength+6])

    elif kind==1:

        offset=BytesToValue(rawTransaction[tranLen-2:tranLen])
        
        parsedTransaction['treeDepth']=BytesToValue(rawTransaction[offset:offset+2])
        parsedTransaction['rootNode']=BytesToValue(rawTransaction[offset+2:offset+6])
        parsedTransaction['leafRecords']=BytesToValue(rawTransaction[offset+6:offset+0xA])
        parsedTransaction['firstLeafNode']=BytesToValue(rawTransaction[offset+0xA:offset+0xE])                
        parsedTransaction['lastLeafNode']=BytesToValue(rawTransaction[offset+0xE:offset+0x12])
        parsedTransaction['nodeSize']=BytesToValue(rawTransaction[offset+0x12:offset+0x14])
        parsedTransaction['maxKeyLength']=BytesToValue(rawTransaction[offset+0x14:offset+0x16])
        parsedTransaction['totalNodes']=BytesToValue(rawTransaction[offset+0x16:offset+0x1A])
        parsedTransaction['freeNodes']=BytesToValue(rawTransaction[offset+0x1A:offset+0x1E])
        parsedTransaction['reserved1']=BytesToValue(rawTransaction[offset+0x1E:offset+0x20])
        parsedTransaction['clumpSize']=BytesToValue(rawTransaction[offset+0x20:offset+0x24])
        parsedTransaction['btreeType']=BytesToValue(rawTransaction[offset+0x24:offset+0x25])
        parsedTransaction['keyCompareType']=BytesToValue(rawTransaction[offset+0x25:offset+0x26])
        parsedTransaction['attributes']=BytesToValue(rawTransaction[offset+0x26:offset+0x2A])
        parsedTransaction['reserved3']=BytesToValue(rawTransaction[offset+0x2A:offset+0x6A])


    return kind


def AllocationContentParser(transaction,blockOffset,tranLen):

    allocatedBlock=[0]
    start=-1
    for k in range(0,tranLen):
        for l in range(0,8):
            if start==-1 and (BytesToValue(transaction[i][j][1][k])>>(7-l))%2==1:
                start==k*8+l
            elif start!=-1 and (BytesToValue(transaction[i][j][1][k])>>(7-l))%2==0:
                allocatedBlock[0]+=1
                allocatedBlock.append((start+blockoffset,k*8+l-start))
                start=-1
    
    for k in range(1,existentFork[0]+1):

        if existentFork[k][0]['state']==1:

            check=0

            if (blockoffset,(specialFileOffset+tranLen)*8)<=existentFork[k][0][1] and existentFork[k][0][1]+existentFork[k][0][2]<=:
                
                check=1
                for l in range(1,allocatedBlock[0]+1):
                    if allocatedBlock[l][0]<=existentFork[k][0][1] and existentFork[k][0][1]+existentFork[k][0][2]<=allocatedBlock[l][0]+allocatedBlock[l][1]:
                        check=2
                        break
                        
            elif blockoffset<=existentFork[k][0][1]<(specialFileOffset+tranLen)*8:
                
                check=1
                for l in range(1,allocatedBlock[0]+1):
                    if allocatedBlock[l][0]<=existentFork[k][0][1] and allocatedBlock[l][0]+allocatedBlock[l][1]==(specialFileOffset+tranLen)*8:
                        check=2
                        break

            elif blockoffset<existentFork[k][0][1]+existentFork[k][0][2]<=(specialFileOffset+tranLen)*8:

                check=1
                for l in range(1,allocatedBlock[0]+1):
                    if allocatedBlock[l][0]==blockoffset and allocatedBlock[l][0]+allocatedBlock[l][1]>=existentFork[k][0][1]+existentFork[k][0][2]:
                        check=2
                        break

            if check==2:
                allocatedBlock.pop(l)
                allocatedBlock[0]-=1

            elif check==1:
                existentFork[k][0][0]=0


def CompletingFullPath(transaction,catalogFile):

    modifiedNodes=[]
    for i in range(1,transaction[0]+1):
        for j in range(1,transaction[i][0]+1):
            if transaction[i][j][2][0]==0 and transaction[i][j][2][1][1] not in modifiedNodes:
                modifiedNodes.append(transaction[i][j][2][1][1])

    CatalogFileAnalyzer(catalogFile,modifiedNodes)


    for i in range(1,transaction[0]+1):
        for j in range(1,transaction[i][0]+1):
            for k in transaction[i][j].keys():

                fullPath=transaction[i][j][k]['fullPath']
                j=transaction[i][j][k]['unidentifiedAncestor']

                while j!=1:
                    if j not in nameAndParent[0].keys():
                        fullPath='unknown'
                        break
                    fullPath='/'+nameAndParent[0][j][0]+fullPath
                    j=nameAndParent[0][j][1]

                transaction[i][j][k]['fullPath']=fullPath
                

def TransactionAnalyzer(transaction,specialFileInfo,catalogFile,sectorSize,blockSize):

    for i in range(1,transaction[0]+1):        
        for j in range(1,transaction[i][0]+1):
            
            tranLen=len(transaction[i][j][1])

            if transaction[0]*sectorSize==1024:
                VolumeHeaderContentParser(transaction[i][j][1],transaction[i][j][3])
            
            for k in range(0,3):
                
                check=False
                offset=0
                for l in range(1,specialFileInfo[k][2][0]+1):

                    if specialFileInfo[k][2][l][0]*blockSize<=transaction[i][j][0]*sectorSize<(specialFileInfo[k][2][l][0]+specialFileInfo[k][2][l][1])*blockSize:
                        offset+=transaction[i][j][0]*sectorSize-allocationFileInfo[2][k][0]*blockSize
                        transaction[i][j].append([k])
                        check=True
                        break

                    offset+=specialFileInfo[2][k][1]*blockSize
                    
                if check:
                    if k<3:
                        transaction[i][j].append([])
                        transaction[i][j][2].append(offset)
                        transaction[i][j][2].append(BtreeNodeParser(k,transaction[i][j][1],transaction[i][j][3],tranLen))

                    elif:
                        transaction[i][j][2].append(offset)
                        ContentParser[k](transaction[i][j][1],8*offset,tranLen)

                    break

    CompletingFullPath(transaction,catalogFile)


def RecordDeduplication(transaction):
    
    deduplicatedRecord=[[0],{},[0]]
    
    for i in range(1,transaction[0]+1):

        deduplicatedRecord[0][0]+=1
        deduplicatedRecord[0].append([0])
        
        deduplicatedRecord[2][0]+=1
        deduplicatedRecord[2].append([0])
        
        for j in range(1,transaction[i][0]+1):

            deduplicatedRecord[0][i][0]+=1
            deduplicatedRecord[0][i].append([0])

            deduplicatedRecord[2][i][0]+=1
            deduplicatedRecord[2][i].append([0])

            if transaction[i][j][1]=='cl':
                
                bnum=str(transaction[i][j][0])

                check=True
                for k in deduplicatedRecord[1].keys():
                    if bnum==k:
                        check=False
                        break

                if check:
                    deduplicatedRecord[1][bnum]={}
        
                for k in transaction[i][j][2].keys():p
                    
                    check=True
                    for l in deduplicatedRecord[1][bnum].keys():
                        if k==l:
                            check=False
                            break

                    if check:
                        
                        deduplicatedRecord[0][i][j][0]+=1
                        deduplicatedRecord[0][i][j].append(transaction[i][j][2][k])
                        
                        deduplicatedRecord[1][bnum][k]={str((i,j)):transaction[i][j][2][k]}

                        if transaction[i][j][2][k]['recordType']==2:
                            
                            deduplicatedRecord[2][i][j][0]+=1
                            deduplicatedRecord[2][i][j].append(transaction[i][j][2][k])

                    else:
                        
                        if transaction[i][j][2][k]['recordType']==2:
                            check=0
                        else:
                            check=1
                        
                        for l in deduplicatedRecord[1][bnum][k]:                        
                                
                            if transaction[i][j][2][k]==deduplicatedRecord[1][bnum][k][l]:
                                check=2
                                break

                            elif transaction[i][j][2][k]['recordType']==2 and deduplicatedRecord[1][bnum][k][l]['recordType']==2:
                                if transaction[i][j][2][k]['dataFork']==deduplicatedRecord[1][bnum][k][l]['dataFork'] and transaction[i][j][2][k]['resourceFork']==deduplicatedRecord[1][bnum][k][l]['resourceFork']:
                                    check=1

                        if check<2:
                            
                            deduplicatedRecord[0][i][j][0]+=1
                            deduplicatedRecord[0][i][j].append(transaction[i][j][2][k])
                            
                            deduplicatedRecord[1][bnum][k][str((i,j))]=transaction[i][j][2][k]

                            if check<1:

                                deduplicatedRecord[2][i][j][0]+=1
                                deduplicatedRecord[2][i][j].append(transaction[i][j][2][k])

    return deduplicatedRecord
                    

def DataRecovery(disk,deduplicatedRecord,blockSize):

    keyForFork=['dataFork','resourceFork']

    DirectoryCleaning('recovery')
    
    for i in range(1,deduplicatedRecord[0]+1):
        for j in range(1,deduplicatedRecord[i][0]+1):
            for k in range(1,deduplicatedRecord[i][j][0]+1):

                check=False
                for l in range(0,2):
                    for m in range(1,deduplicatedRecord[i][j][k][keyForFork[l]][0]+1):
                        if deduplicatedRecord[i][j][k][keyForFork[l]][m][0]==0:
                            check=True
                            break

                if check:
                    
                    fork=['','']
                    
                    for l in range(0,2):
                        
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

                        
