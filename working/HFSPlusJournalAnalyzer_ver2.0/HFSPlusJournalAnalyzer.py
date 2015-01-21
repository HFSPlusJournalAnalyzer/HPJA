import Analyzer
import Collector
import Utility
import datetime
import csv

def main():

    Utility.DirectoryCleaning('transaction')
    Utility.DirectoryCleaning('result')

    specialFileName=['AllocationFile','ExtentsOverflowFile','CatalogFile','AttributeFile']
    specialFile=[]

    if raw_input('Is disk connected? [y/n]: ').lower()=='y':

        temp=Collector.VolumeFinder()
        disk = temp[0]
        select = temp[1]
        recovery = temp[2]
        
        print 'Collecting files...'
        temp=Collector.VolumeHeaderParser(Utility.DiskDump(disk,'HFSPlusVolumeHeader',512,1,1,select))    
        blockSize=temp[0]
        journalInfoBlock=temp[1]
        specialFileInfo=temp[2]

        for i in range(0,4):
            specialFile.append(Collector.SpecialFileExtractor(specialFileName[i],specialFileInfo[i],disk,blockSize,select))

        journal=Collector.JournalExtractor(journalInfoBlock,disk,blockSize,select)
    
    else:
        
        path=raw_input('Input path of volume header\n')
        f=open(path,'rb')
        temp=Collector.VolumeHeaderParser(f.read())
        blockSize=temp[0]
        journalInfoBlock=temp[1]
        specialFileInfo=temp[2]
        f.close()
        
        path=raw_input('Input path of journal\n')
        f=open(path,'rb')
        journal=f.read()
        f.close()

        for i in range(0,4)
            path=raw_input('Input path of {0}\n'.format(specialFileName))
            f=open(path,'rb')
            specialFile.append(f.read())
            f.close()
        
        recovery=False

    print 'Analyzing journal...'
    temp=Analyzer.JournalParser(journal)
    sectorSize=temp[0]
    transaction=temp[1]
    
    print 'Printing transactions...'
    for i in range(1,transaction[0]+1):
        for j in range(1,transaction[i][0]+1):
            fName='./transaction/transaction'+str(i)+'_'+str(j)+'(sector'+hex(transaction[i][j][0])+')'
            f=open(fName,'wb')
            f.write(transaction[i][j][1])
            f.close()

    print 'Analyzing transactions...'
    Analyzer.TransactionAnalyzer(transaction,specialFileInfo,sectorSize,blockSize)

    print 'Printing record list...'
    fName='./result/recordList.csv'
    f=open(fName,'w')
    for i in range(1,transaction[0]+1):
        for j in range(1,transaction[i][0]+1):
            
            if transaction[i][j][1][0]=='c':
                
                if transaction[i][j][1][1]=='l' or transaction[i][j][1][1]=='i':
                    
                    for k in transaction[i][j][2].keys():
                    
                        f.write('transaction{0}_{1} record{2}\n'.format(i,j,k)+',')

                        for l in transaction[i][j][2][k].keys():
                        
                            if l=='nodeName' or l=='fullPath':
                                f.write('{0} : {1}\n'.format(l,transaction[i][j][2][k][l].encode('utf-8'))+',')
                        
                            else:
                                f.write('{0} : {1}\n'.format(l,transaction[i][j][2][k][l])+',')
            
                        f.write('\n')
                
                elif transaction[i][j][1][1]=='h':
                    
                    f.write('transaction{0}_{1}\n'.format(i,j)+',')
                    
                    for k in transaction[i][j][2].keys():
                        f.write('{0} : {1}\n'.format(k,transaction[i][j][2][k])+',')
            
                    f.write('\n')

    f.close()

    print 'Deduplicating records...'
    deduplicatedRecord=Analyzer.RecordDeduplication(transaction)

    print 'Printing deduplicated records...'
    keyForType=['recordType']
    keyForString=['nodeName','fullPath']
    keyForID=['parentID','CNID','ownerID','groupID']
    keyForDate=['createDate','contentModDate','attributeModDate','accessDate']
    keyForFork=['dataFork','resourceFork']

    fName='./result/deduplicatedRecordList.csv'
    f=open(fName,'w')

    for i in keyForType:
        f.write('transaction'+','+i+',')

    for i in keyForString:
        f.write(i+',')
        
    for i in keyForID:
        f.write(i+',')

    for i in keyForDate:
        f.write(i+',')

    f.write('AllocatedFork'+',')

    f.write('\n')
    
    for i in range(1,deduplicatedRecord[0][0]+1):
        f.write(',')

        f.write('\ntransaction{0}\n'.format(i)+',')
        
        for j in range(1,deduplicatedRecord[0][i][0]+1):

            f.write('\ntransaction{0}_{1}\n'.format(i,j))

            for k in range(1,deduplicatedRecord[0][i][j][0]+1):
                
                if deduplicatedRecord[0][i][j][k]['recordType']<3:

                    for l in keyForType:
                        if deduplicatedRecord[0][i][j][k][l]==1:
                            f.write(',')
                            f.write('folder')
                        else:
                            f.write(',')
                            f.write('file')
                
                    for l in keyForString:
                        f.write(',')
                        f.write(deduplicatedRecord[0][i][j][k][l].encode('utf-8'))
                    f.write(',')

                    for l in keyForID:
                        f.write(hex(deduplicatedRecord[0][i][j][k][l])[2:])
                    f.write(',')
                
                    for l in keyForDate:
                        f.write((datetime.datetime(1904,1,1)+datetime.timedelta(seconds=deduplicatedRecord[0][i][j][k][l])).isoformat(' ')+',')
                    
                    if deduplicatedRecord[0][i][j][k]['recordType']==2:

                        duplicated=''
                        allocatedFork=0
                        for l in keyForFork:
                            for m in range(1,deduplicatedRecord[0][i][j][k][l][0]+1):
                                if deduplicatedRecord[0][i][j][k][l][m][0]==1:
                                    allocatedFork+=1
                                elif deduplicatedRecord[0][i][j][k][l][m][0]==-1:
                                    duplicated='(duplicated)'

                        f.write('{0}/{1}{2}'.format(allocatedFork,deduplicatedRecord[0][i][j][k]['dataFork'][0]+deduplicatedRecord[0][i][j][k]['resourceFork'][0],duplicated)+',')
                            
                    f.write('\n')
                
    f.close()

    if recovery:
        print 'Recoverying deleted files...'
        Analyzer.DataRecovery(disk,deduplicatedRecord[2],blockSize)


if __name__=='__main__':
    main()
