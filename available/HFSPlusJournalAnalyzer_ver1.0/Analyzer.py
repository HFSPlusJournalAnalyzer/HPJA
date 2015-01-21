from Utility import *

def JournalParser(Journal):
    print 'JournalParser'
    endian=BytesToValue(Journal[4:8])
    start=BytesToValue(Journal[8:0x10],endian)
    end=BytesToValue(Journal[0x10:0x18],endian)
    size=BytesToValue(Journal[0x18:0x20],endian)
    blhdr_size=BytesToValue(Journal[0x20:0x24],endian)
    jhdr_size=BytesToValue(Journal[0x28:0x2C],endian)
    
    blhdrPointer=end
    turn=False
    jbsize=size-jhdr_size
    bnext=0
    transaction=[0]

    while not VerifyChecksum('block list header',endian,Journal[blhdrPointer:blhdrPointer+0x20],0x20):
        blhdrPointer+=jhdr_size
        if blhdrPointer==size:
            blhdrPointer=jhdr_size
            turn=True

    while blhdrPointer<end or not turn:

        if bnext==0:
            transaction[0]+=1
            transaction.append([0])
            
        num_blocks=BytesToValue(Journal[blhdrPointer+2:blhdrPointer+4],endian)
        bytes_used=BytesToValue(Journal[blhdrPointer+4:blhdrPointer+8],endian)
        bnext=BytesToValue(Journal[blhdrPointer+0x1C:blhdrPointer+0x20],endian)

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
                bnum=BytesToValue(Journal[blhdrPointer:blhdrPointer+8],endian)
                bsize=BytesToValue(Journal[blhdrPointer+8:blhdrPointer+0xC],endian)
                
                transaction[transaction[0]][0]+=1
                    
                if blPointer+bsize>size:
                    transaction[transaction[0]].append([bnum,Journal[blPointer:size]+Journal[jhdr_size:blPointer+bsize-jbsize]])
                    blPointer+=bsize-jbsize
                                
                else:
                    transaction[transaction[0]].append([bnum,Journal[blPointer:blPointer+bsize]])
                    blPointer+=bsize

                blhdrPointer+=0x10

            if blhdrPointer==size:
                blhdrPointer=jhdr_size

        
        blhdrPointer+=bytes_used-(num_blocks+1)*0x10
        if blhdrPointer>=size:
            blhdrPointer-=jbsize
            turn=1
        

            
    return (jhdr_size,transaction)


def CatalogFileAnalyzer(CatalogFile):

    nameAndParent={1:(u'',0)}

    nodeSize=BytesToValue(CatalogFile[0x20:0x22])
    totalNodes=BytesToValue(CatalogFile[0x24:0x28])

    nodePointer=nodeSize
    for i in range(1,totalNodes):

        if BytesToValue(CatalogFile[nodePointer+8])==0xFF:

            numRecords=BytesToValue(CatalogFile[nodePointer+0xA:nodePointer+0xC])

            for j in range(0,numRecords):

                offset=nodePointer+BytesToValue(CatalogFile[nodePointer+nodeSize-2*(j+1):nodePointer+nodeSize-2*j])                
                        
                keyLength=BytesToValue(CatalogFile[offset:offset+2])                
                        
                if 2<BytesToValue(CatalogFile[offset+keyLength+2:offset+keyLength+4])<5:

                    CNID=BytesToValue(CatalogFile[offset+2:offset+6])

                    offset+=2+keyLength
                    
                    parentID=BytesToValue(CatalogFile[offset+4:offset+8])

                    nodeName=u''    
                    for k in range(0,BytesToValue(CatalogFile[offset+8:offset+0xA])):
                        nodeName+=('\u'+CatalogFile[offset+0xA+2*k].encode('hex')+CatalogFile[offset+0xA+2*k+1].encode('hex')).decode('unicode-escape')
                    
                    nameAndParent[CNID]=(nodeName,parentID)

    return nameAndParent
                

def TransactionAnalyzer(transaction,allocationFileInfo,catalogFileInfo,nameAndParent,sectorSize,blockSize):

    existentData=[0]
    
    for i in range(1,transaction[0]+1):        
        for j in range(1,transaction[i][0]+1):
            
            transaction[i][j].append('')
            
            check=False
            for k in range(1,catalogFileInfo[2][0]+1):
                if catalogFileInfo[2][k][0]*blockSize<=transaction[i][j][0]*sectorSize<(catalogFileInfo[2][k][0]+catalogFileInfo[2][k][1])*blockSize:
                    transaction[i][j][2]+='c'
                    check=True
                    break
                
            if check:
                
                kind=BytesToValue(transaction[i][j][1][8])

                numRecords=BytesToValue(transaction[i][j][1][0xA:0xC])
                tranLen=len(transaction[i][j][1])

                transaction[i][j].append({})
                
                if kind==0xFF:
                    
                    transaction[i][j][2]+='l'
                    
                    for k in range(0,numRecords):

                        offset=BytesToValue(transaction[i][j][1][tranLen-2*(k+1):tranLen-2*k])
                        recordOffset=str(offset)
            
                        transaction[i][j][3][recordOffset]={}
                        
                        keyLength=BytesToValue(transaction[i][j][1][offset:offset+2])
                        transaction[i][j][3][recordOffset]['keyLength']=keyLength
                        
                        recordType=BytesToValue(transaction[i][j][1][offset+keyLength+2:offset+keyLength+4])
                        transaction[i][j][3][recordOffset]['recordType']=recordType
                        
                        if recordType<3:

                            
                            transaction[i][j][3][recordOffset]['parentID']=BytesToValue(transaction[i][j][1][offset+2:offset+6])

                            nodeName=u''                        
                            for l in range(0,BytesToValue(transaction[i][j][1][offset+6:offset+8])):
                                nodeName+=('\u'+transaction[i][j][1][offset+8+2*l].encode('hex')+transaction[i][j][1][offset+8+2*l+1].encode('hex')).decode('unicode-escape')

                            transaction[i][j][3][recordOffset]['nodeName']=nodeName.replace('/',':')
                            
                            offset+=2+keyLength
                        
                            transaction[i][j][3][recordOffset]['flags']=BytesToValue(transaction[i][j][1][offset+2:offset+4])
                            CNID=BytesToValue(transaction[i][j][1][offset+8:offset+0xC])
                            transaction[i][j][3][recordOffset]['CNID']=CNID
                            createDate=BytesToValue(transaction[i][j][1][offset+0xC:offset+0x10])
                            transaction[i][j][3][recordOffset]['createDate']=createDate
                            transaction[i][j][3][recordOffset]['contentModDate']=BytesToValue(transaction[i][j][1][offset+0x10:offset+0x14])
                            transaction[i][j][3][recordOffset]['attributeModDate']=BytesToValue(transaction[i][j][1][offset+0x14:offset+0x18])
                            transaction[i][j][3][recordOffset]['accessDate']=BytesToValue(transaction[i][j][1][offset+0x18:offset+0x1C])
                            transaction[i][j][3][recordOffset]['backupDate']=BytesToValue(transaction[i][j][1][offset+0x1C:offset+0x20])
                            transaction[i][j][3][recordOffset]['ownerID']=BytesToValue(transaction[i][j][1][offset+0x20:offset+0x24])
                            transaction[i][j][3][recordOffset]['groupID']=BytesToValue(transaction[i][j][1][offset+0x24:offset+0x28])
                            transaction[i][j][3][recordOffset]['permissions']=BytesToValue(transaction[i][j][1][offset+0x20:offset+0x30])
                            transaction[i][j][3][recordOffset]['userInfo']=BytesToValue(transaction[i][j][1][offset+0x30:offset+0x40])
                            transaction[i][j][3][recordOffset]['finderInfo']=BytesToValue(transaction[i][j][1][offset+0x40:offset+0x50])
                            transaction[i][j][3][recordOffset]['textEncoding']=BytesToValue(transaction[i][j][1][offset+0x50:offset+0x54])

                            fullPath=u''
                            l=CNID
                            while l>0:

                                if not l in nameAndParent:
                                    fullPath='unknown'
                                    break

                                fullPath=nameAndParent[l][0]+'/'+fullPath
                                l=nameAndParent[l][1]

                            transaction[i][j][3][recordOffset]['fullPath']=fullPath
                            
                            if recordType==2:

                                offset+=0x58
                                fork=[]
                                for l in range(0,2):
                                                 
                                    fork.append([0])
                                    
                                    for m in range(0,8):

                                        startBlock=BytesToValue(transaction[i][j][1][offset+0x10+8*m:offset+0x14+8*m])
                                        blockCount=BytesToValue(transaction[i][j][1][offset+0x14+8*m:offset+0x18+8*m])
         
                                        if startBlock!=0 and blockCount!=0:
                                            
                                            fork[l][0]+=1
                                            fork[l].append([1,startBlock,blockCount])

                                            n=1
                                            while n<=existentData[0]:

                                                if (transaction[existentData[n][0]][existentData[n][1]][3][existentData[n][2]]['createDate']!=createDate or transaction[existentData[n][0]][existentData[n][1]][3][existentData[n][2]]['CNID']!=CNID) and (existentData[n][5]<=startBlock<existentData[n][5]+existentData[n][6] or existentData[n][5]<startBlock+blockCount<=existentData[n][5]+existentData[n][6]):

                                                    if existentData[n][3]==0:
                                                        transaction[existentData[n][0]][existentData[n][1]][3][existentData[n][2]]['dataFork'][existentData[n][4]][0]=-1
                                                    else:
                                                        transaction[existentData[n][0]][existentData[n][1]][3][existentData[n][2]]['resourceFork'][existentData[n][4]][0]=-1
                                                    
                                                    existentData.pop(n)
                                                    existentData[0]-=1
                                                    n-=1

                                                n+=1

                                                offset+=0x50

                                transaction[i][j][3][recordOffset]['dataFork']=fork[0]
                                transaction[i][j][3][recordOffset]['resourceFork']=fork[1]
                                transaction[i][j][3][recordOffset]['reserved']=BytesToValue(transaction[i][j][1][offset+4:offset+8])
                                transaction[i][j][3][recordOffset]['reserved2']=BytesToValue(transaction[i][j][1][offset+0x54:offset+0x58])

                                for l in range(0,2):
                                    for m in range(1,fork[l][0]+1):
                                        existentData[0]+=1
                                        existentData.append((i,j,recordOffset,l,m,fork[l][m][1],fork[l][m][2]))

                            elif recordType==1:

                                transaction[i][j][3][recordOffset]['valence']=BytesToValue(transaction[i][j][1][offset+4:offset+8])
                                transaction[i][j][3][recordOffset]['reserved']=BytesToValue(transaction[i][j][1][offset+0x54:offset+0x58])

                        else:

                            transaction[i][j][3][recordOffset]['CNID']=BytesToValue(transaction[i][j][1][offset+2:offset+6])

                            offset+=2+keyLength
                            
                            transaction[i][j][3][recordOffset]['reserved']=BytesToValue(transaction[i][j][1][offset+2:offset+4])
                            transaction[i][j][3][recordOffset]['parentID']=BytesToValue(transaction[i][j][1][offset+4:offset+8])

                            nodeName=u''
                        
                            for l in range(0,BytesToValue(transaction[i][j][1][offset+8:offset+0xA])):
                                nodeName+=('\u'+transaction[i][j][1][offset+8+2*l].encode('hex')+transaction[i][j][1][offset+8+2*l+1].encode('hex')).decode('unicode-escape')

                            transaction[i][j][3][recordOffset]['nodeName']=nodeName

                elif kind==1:

                    transaction[i][j][2]+='h'

                    offset=BytesToValue(transaction[i][j][1][tranLen-2:tranLen])
                    
                    transaction[i][j][3]['treeDepth']=BytesToValue(transaction[i][j][1][offset:offset+2])
                    transaction[i][j][3]['rootNode']=BytesToValue(transaction[i][j][1][offset+2:offset+6])
                    transaction[i][j][3]['leafRecords']=BytesToValue(transaction[i][j][1][offset+6:offset+0xA])
                    transaction[i][j][3]['firstLeafNode']=BytesToValue(transaction[i][j][1][offset+0xA:offset+0xE])                
                    transaction[i][j][3]['lastLeafNode']=BytesToValue(transaction[i][j][1][offset+0xE:offset+0x12])
                    transaction[i][j][3]['nodeSize']=BytesToValue(transaction[i][j][1][offset+0x12:offset+0x14])
                    transaction[i][j][3]['maxKeyLength']=BytesToValue(transaction[i][j][1][offset+0x14:offset+0x16])
                    transaction[i][j][3]['totalNodes']=BytesToValue(transaction[i][j][1][offset+0x16:offset+0x1A])
                    transaction[i][j][3]['freeNodes']=BytesToValue(transaction[i][j][1][offset+0x1A:offset+0x1E])
                    transaction[i][j][3]['reserved1']=BytesToValue(transaction[i][j][1][offset+0x1E:offset+0x20])
                    transaction[i][j][3]['clumpSize']=BytesToValue(transaction[i][j][1][offset+0x20:offset+0x24])
                    transaction[i][j][3]['btreeType']=BytesToValue(transaction[i][j][1][offset+0x24:offset+0x25])
                    transaction[i][j][3]['keyCompareType']=BytesToValue(transaction[i][j][1][offset+0x25:offset+0x26])
                    transaction[i][j][3]['attributes']=BytesToValue(transaction[i][j][1][offset+0x26:offset+0x2A])
                    transaction[i][j][3]['reserved3']=BytesToValue(transaction[i][j][1][offset+0x2A:offset+0x6A])

                else:
                    
                    transaction[i][j][2]+='i'

                    for k in range(0,numRecords):

                        offset=BytesToValue(transaction[i][j][1][tranLen-2*(k+1):tranLen-2*k])
                        recordOffset=str(offset)
            
                        transaction[i][j][3][recordOffset]={}
                        
                        keyLength=BytesToValue(transaction[i][j][1][offset:offset+2])
                        transaction[i][j][3][recordOffset]['keyLength']=keyLength

                        transaction[i][j][3][recordOffset]['key']=BytesToValue(transaction[i][j][1][offset+2:offset+2+keyLength])
                        transaction[i][j][3][recordOffset]['nodeNumber']=BytesToValue(transaction[i][j][1][offset+2+keyLength:offset+6+keyLength])
                        
                continue
            
            offset=0
            for k in range(1,allocationFileInfo[2][0]+1):
                
                if allocationFileInfo[2][k][0]*blockSize<=transaction[i][j][0]*sectorSize<(allocationFileInfo[2][k][0]+allocationFileInfo[2][k][1])*blockSize:
                    offset+=transaction[i][j][0]*sectorSize-allocationFileInfo[2][k][0]*blockSize
                    check=True
                    break
                
                offset+=allocationFileInfo[2][k][1]*blockSize
            
                                        
            if check:

                tranLen=len(transaction[i][j][1])
                allocatedBlock=[0]
                start=-1
                for k in range(0,tranLen):
                    for l in range(0,8):
                        if start==-1 and (BytesToValue(transaction[i][j][1][k])>>(7-l))%2==1:
                            start==k*8+l
                        elif start!=-1 and (BytesToValue(transaction[i][j][1][k])>>(7-l))%2==0:
                            allocatedBlock[0]+=1
                            allocatedBlock.append((start+offset*8,k*8+l-start))
                            start=-1
                
                for k in range(1,existentData[0]+1):

                    check=0
                                    
                    if offset*8<=existentData[k][5] and existentData[k][5]+existentData[k][6]<=(offset+tranLen)*8:
                        
                        check=1
                        for l in range(1,allocatedBlock[0]+1):
                            if allocatedBlock[l][0]<=existentData[k][5] and existentData[k][5]+existentData[k][6]<=allocatedBlock[l][0]+allocatedBlock[l][1]:
                                check=2
                                break
                                
                    elif offset*8<=existentData[k][5]<(offset+tranLen)*8:
                        
                        check=1
                        for l in range(1,allocatedBlock[0]+1):
                            if allocatedBlock[l][0]<=existentData[k][5] and allocatedBlock[l][0]+allocatedBlock[l][1]==(offset+tranLen)*8:
                                check=2
                                break

                    elif offset*8<existentData[k][5]+existentData[k][6]<=(offset+tranLen)*8:

                        check=1
                        for l in range(1,allocatedBlock[0]+1):
                            if allocatedBlock[l][0]==offset*8 and allocatedBlock[l][0]+allocatedBlock[l][1]>=existentData[k][5]+existentData[k][6]:
                                check=2
                                break

                    if check==2:
                        allocatedBlock.pop(l)
                        allocatedBlock[0]-=1

                    elif check==1:
                        if existentData[k][3]==0 and transaction[existentData[k][0]][existentData[k][1]][3][existentData[k][2]]['dataFork'][existentData[k][4]][0]==1:
                            transaction[existentData[k][0]][existentData[k][1]][3][existentData[k][2]]['dataFork'][existentData[k][4]][0]=0

                        elif existentData[k][3]==1 and transaction[existentData[k][0]][existentData[k][1]][3][existentData[k][2]]['resourceFork'][existentData[k][4]][0]==1:
                            transaction[existentData[k][0]][existentData[k][1]][3][existentData[k][2]]['resourceFork'][existentData[k][4]][0]=0

    for i in range(1,transaction[0]+1):
        for j in range(1,transaction[i][0]+1):
            if transaction[i][j][2]=='cl' or transaction[i][j][2]=='ch' or transaction[i][j][2]=='ci':
                transaction[i][j].pop(1)


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
        
                for k in transaction[i][j][2].keys():
                    
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

                        
