import Analyzer
import Collector
import Utility
import datetime
import csv
from HFSPlusFormat import *

def main():
    
    Utility.DirectoryCleaning('transaction')
    Utility.DirectoryCleaning('result')

    if raw_input('Is disk connected? [y/n]: ').lower()=='y':

        disk=Collector.VolumeFinder()

        select = (raw_input('Would you like to create image? [y/n] : ').lower()=='y')
        recovery = (raw_input('Would you like to recover the image? [y/n] : ').lower()=='y')
        
        print 'Collecting files...'
        volumeHeader=VolumeHeader(Utility.DiskDump(disk,'HFSPlusVolumeHeader',512,2,1,select))

        journal=Collector.JournalExtractor(self.journalInfoBlock,disk,volumeHeader.blockSize,select)
        allocationFile=Collector.SpecialFileExtractor('AllocationFile',volumeHeader.specialFileFork[0],disk,volumeHeader.blockSize,select)
        extentsOverflowFile=Collector.SpecialFileExtractor('ExtentsOverflowFile',volumeHeader.specialFileFork[1],disk,volumeHeader.blockSize,select)
        catalogFile=Collector.SpecialFileExtractor('CatalogFile',volumeHeader.specialFileFork[2],disk,volumeHeader.blockSize,select)
    
    else:
        
        path=raw_input('Input path of volume header\n')
        f=open(path,'rb')
        volumeHeader=VolumeHeader(f.read())
        f.close()
        
        path=raw_input('Input path of journal\n')
        f=open(path,'rb')
        journal=f.read()
        f.close()

        if raw_input('Input path of catalog file(y/n)\n') == 'y':
            path=input()
            f=open(path,'rb')
            catalogFile=f.read()
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
    tranBlocks=Analyzer.journalParser(journal)
    
    print 'Printing transactions...'
    for i in range(1,tranBlocks[0]+1):
        fName='./transaction/transaction{0}_block{1}(journaloffset:{2}_location:{3})'.format(i,j,tranBlocks[i].journalOffset,tranBlocks[i].offset)
        f=open(fName,'wb')
        f.write(tranBlocks[i].content)
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
    '''
    if recovery:
        print 'Recoverying deleted files...'
        Analyzer.DataRecovery(disk,,volumeHeader.blockSize)
        '''


if __name__=='__main__':
    main()
