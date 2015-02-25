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

    if catalogFile!=0:
        makefstruct(catalogFile)

    path='result{0}'.format(option['id'])
    DirectoryCleaning(path)

    form=0
    if 'csv' in option:
        print 'Creating CSV files...'
        form+=1

    if 'sql' in option:
        print 'Creating SQLite file...'
        form+=2

    if form>0:
        journalParser(form,path,jParseList,bOffList)
        if 'va' in option:
            print 'Analyzing volume...'
            volumeInfo(path,vh)
            specialFileParser(form,path,{'Extents':extentsFile,'Catalog':catalogFile,'Attributes':attributesFile})

    jT = journalTrack(jParseList, pInfo)

    if 't' in option:
        print 'Tracking journal...'
        journalTrackPrint(jT, "{0}/journalTrack.txt".format(path))

    if 'p' in option:
        print 'Finding pattern...'
        Pattern_useMe(jT, "{0}/pattern.txt".format(path))

    if 'f' in option:
        print 'Output file system format result...'
        getFSOutput(journal, jParseList, pInfo, bOffList)

    if 'r' in option:
        if 'i' in option:
            print 'Recover the file...'
            recovery(option['l'],path,option['r'],jParseList,vh)
        else:
            print 'Not able to recover the file. Please input a disk image.'

    print 'Mnemosyne zzang!'

if __name__=='__main__':
    main(translatingInput(sys.argv))