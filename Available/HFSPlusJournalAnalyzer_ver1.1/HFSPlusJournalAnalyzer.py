import Analyzer
import Collector
import Utility
import datetime
import csv

def main():
    
    Utility.DirectoryCleaning('transaction')
    Utility.DirectoryCleaning('result')

    if raw_input('Is disk connected? [y/n]: ').lower()=='y':
        temp=Collector.VolumeFinder()
        disk =temp[0]
        select = temp[1]
        recovery = temp[2]
        
        print 'Collecting files...'
        temp=Collector.VolumeHeaderParser(Utility.DiskDump(disk,'HFSPlusVolumeHeader',1024,1,1,select))    
        blockSize=temp[0]
        journalInfoBlock=temp[1]
        specialFileInfo=temp[2]

        
        AllocationFile=Collector.SpecialFileExtractor('AllocationFile',specialFileInfo[0],disk,blockSize,select)
        ExtentsOverflowFile=Collector.SpecialFileExtractor('ExtentsOverflowFile',specialFileInfo[1],disk,blockSize,select)
        CatalogFile=Collector.SpecialFileExtractor('CatalogFile',specialFileInfo[2],disk,blockSize,select)
        Journal=Collector.JournalExtractor(journalInfoBlock,disk,blockSize,select)
    
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
        Journal=f.read()
        f.close()

        if raw_input('Input path of catalog file(y/n)\n') == 'y':
            path=input()
            f=open(path,'rb')
            CatalogFile=f.read()
            f.close()
        
        """
        if raw_input('Input path of allocation file(y/n)') == 'y':
        path=raw_input()
        f=open(path,'rb')
        AllocationFile=f.read()
        f.close()
        
        if raw_input('Input path of extents overflow file(y/n)\n') == 'y':
        path=raw_input()
        f=open(path,'rb')
        ExtentsOverflowFile=f.read()
        f.close()
        """
        recovery=False

    print 'Analyzing journal...'
    temp=Analyzer.JournalParser(Journal)
    sectorSize=temp[0]
    transaction=temp[1]
    
    print 'Printing transactions...'
    for i in range(1,transaction[0]+1):
        for j in range(1,transaction[i][0]+1):
            fName='./transaction/transaction'+str(i)+'_'+str(j)+'(sector'+hex(transaction[i][j][0])+')'
            f=open(fName,'wb')
            f.write(transaction[i][j][1])
            f.close()

    print 'Analyzing CatalogFile...'
    nameAndParent=Analyzer.CatalogFileAnalyzer(CatalogFile)

    print 'Analyzing transactions...'
    Analyzer.TransactionAnalyzer(transaction,specialFileInfo[0],specialFileInfo[2],nameAndParent,sectorSize,blockSize)

    print 'Printing record list...'

    keyForType=['recordType']
    keyForString=['nodeName','fullPath']
    keyForID=['parentID','CNID','ownerID','groupID']
    keyForDate=['createDate','contentModDate','attributeModDate','accessDate']
    keyForFork=['dataFork','resourceFork']

    fName='./result/recordList.csv'

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

    f=open(fName,'w')
    for i in range(1,transaction[0]+1):

        f.write('\ntransaction{0}\n'.format(i))

        for j in range(1,transaction[i][0]+1):

            f.write('\ntransaction{0}_{1}\n'.format(i,j))
            
            if transaction[i][j][1][0]=='c' and transaction[i][j][1][1]=='l':

                for k in transaction[i][j][2].keys():

                    if transaction[i][j][2][k]['recordType']<3:
                    
                        for l in keyForType:

                            if transaction[i][j][2][k][l]==1:
                                f.write(',')
                                f.write('folder')
                            else:
                                f.write(',')
                                f.write('file')
                    
                        for l in keyForString:
                            f.write(',')
                            f.write(transaction[i][j][2][k][l].encode('utf-8'))
                        f.write(',')

                        for l in keyForID:
                            f.write(hex(transaction[i][j][2][k][l])[2:])
                        f.write(',')
                    
                        for l in keyForDate:
                            f.write((datetime.datetime(1904,1,1)+datetime.timedelta(seconds=transaction[i][j][2][k][l])).isoformat(' ')+',')
                        
                        if transaction[i][j][2][k]['recordType']==2:

                            duplicated=''
                            allocatedFork=0
                            for l in keyForFork:
                                for m in range(1,transaction[i][j][2][k][l][0]+1):
                                    if transaction[i][j][2][k][l][m][0]==1:
                                        allocatedFork+=1
                                    elif transaction[i][j][2][k][l][m][0]==-1:
                                        duplicated='(duplicated)'

                            f.write('{0}/{1}{2}'.format(allocatedFork,transaction[i][j][2][k]['dataFork'][0]+transaction[i][j][2][k]['resourceFork'][0],duplicated)+',')
                                
                        f.write('\n')

    f.close()


if __name__=='__main__':
    main()
