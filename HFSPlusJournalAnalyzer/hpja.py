import collect_tools
from output.output_generic import *
from output.output_fs import *
from analysis.hfs_parse import *
from analysis.journal_pattern import *
from analysis.journal_track import *
from analysis.recovery import *
from etc_util import *

def main(option):

    if 'i' in option:
        temp=collect_tools.main(option)
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
    jParseList, pInfo, bOffList = journalParser(journal)
    jT = journalTrack(jParseList)
    
    outputPath1 = r"C:\TEMP\sibalsibal.txt"
    outputPath2 = r"C:\TEMP\ssibal.txt"
    
    journalTrackPrint(jT, outputPath1)
    Pattern_useMe(jT, outputPath2)
    getFSOutput(journal, jParseList, pInfo, bOffList)

    path='result{0}'.format(option['id'])

    DirectoryCleaning(path)

    specialFileAnalyzer(path,{'Extents':extentsFile,'Catalog':catalogFile,'Attributes':attributesFile})

    rawCSV(path,jParseList)
    rawSQLite3(path,jParseList)

    if 'r' in option:
        recovery(option['l'],path,option['r'],jParseList,vh)

if __name__=='__main__':
    main(translatingInput(sys.argv))