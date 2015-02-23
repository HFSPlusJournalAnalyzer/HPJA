import collect_tools
from output.output_generic import *
from output.output_fs import *
from analysis.hfs_parse import *
from analysis.journal_pattern import *
from analysis.journal_track import *
from analysis.recovery import *
from lib.etc_util import *

def main(option):

    if 'i' in option:
        temp=collect_tools.main(option)
        journal=temp[0]
        vh=temp[1]
        allocationFile=temp[2]
        extentsFile=temp[3]
        catalogFile=temp[4]
        attributesFile=temp[5]

    elif 'j' in option:

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

    else:

        print 'Please input disk image or journal file.'
        return


    print 'Analyzing journal...'
    jParseList, pInfo, bOffList = journalParser(journal)
    jT = journalTrack(jParseList, pInfo)

    path='result{0}'.format(option['id'])
    DirectoryCleaning(path)
    
    if 't' in option:
        journalTrackPrint(jT, "{0}/journalTrack.txt".format(path))

    if 'p' in option:
        Pattern_useMe(jT, "{0}/pattern.txt".format(path))

    if 'f' in option:
        getFSOutput(journal, jParseList, pInfo, bOffList)

    if 'va' in option:
        volumeInfo(path,vh)
        specialFileAnalyzer(path,{'Extents':extentsFile,'Catalog':catalogFile,'Attributes':attributesFile})

    if 'csv' in option:
        rawCSV(path,jParseList)

    if 'sql' in option:
        rawSQLite3(path,jParseList)

    if 'r' in option:
        if 'i' in option:
            recovery(option['l'],path,option['r'],jParseList,vh)
        else:
            print 'Not able to recover the file. Please input a disk image.'

if __name__=='__main__':
    main(translatingInput(sys.argv))