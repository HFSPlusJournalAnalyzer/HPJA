import collect_tools
from output.output_generic import *
from output.output_fs import *
from analysis.hfs_parse import *
from analysis.journal_pattern import *
from analysis.journal_track import *
from analysis.recovery import *
from lib.etc_util import *

def main(option):

    if 'I' in option:
        temp=collect_tools.main(option)
        journal=temp[0]
        vh=temp[1]
        allocationFile=temp[2]
        extentsFile=temp[3]
        catalogFile=temp[4]
        attributesFile=temp[5]

    elif 'J' in option:

        f=open(option['J'],'rb')
        journal=f.read()
        f.close()

        files=[]
        for i in ['V','AL','E','C','AT']:
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
    if 'c' in option:
        form+=1

    if 's' in option:
        form+=2

    if form>0:
        if 'v' in option:
            print 'Parsing volume...'
            volumeInfo(path,vh)
            outputParsedspecialFile(form,path,{'Extents':extentsFile,'Catalog':catalogFile,'Attributes':attributesFile})
        if 'j' in option:
            print 'Printing journal parsing result...'
            outputParsedJournal(form,path,jParseList,bOffList)
        #outputCoreFields(form,path,jParseList,bOffList)

    jT = journalTrack(jParseList, pInfo)

    if 't' in option:
        print 'Tracking journal...'
        journalTrackPrint(jT, "{0}/journalTrack.txt".format(path))

    if 'p' in option:
        print 'Finding pattern...'
        Pattern_useMe(jT, "{0}/pattern.csv".format(path))

    if 'f' in option:
        print 'Output file system format result...'
        getFSOutput(journal, jParseList, pInfo, bOffList)

    if 'r' in option:
        if 'I' in option:
            print 'Recover the file...'
            recovery(option['I'],path,option['r'],jParseList,vh)
        else:
            print 'Not able to recover the file. Please input a disk image.'

    print 'Mnemosyne zzang!'

if __name__=='__main__':
    main(translatingInput(sys.argv))