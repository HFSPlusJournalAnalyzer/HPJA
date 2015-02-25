import sqlite3
from lib.format import *
from lib.hfs_instance import *
from lib.etc_util import *
from collections import *
from analysis.file_analysis import *

con=None
cur=None

def genFields(standard,prefix='',seen=set()):
    fields=[]
    for i,j in standard._asdict().iteritems():
        i=prefix+j
        try:
            j._asdict()
            fields+=genFields(j,i+'/',seen)

        except AttributeError:
            if not j in seen:
                fields.append(j)
                seen.add(j)

    return fields


def getFieldsNValues(data,prefix=set()):
    fieldsNValues=[]
    for i,j in data._asdict().iteritems():
        i=prefix+i
        try:
            j._asdict()
            fieldsNValues+=getFieldsNValues(j,i+'/')

        except AttributeError:
            fieldsNValues.append((i,j))

    return fieldsNValues


def getRow1(data,fields):

    row=OrderedDict([(i,'') for i in fields])
    for i,j in getFieldsNValues(data,''):
        row[i]=j
        
    return row.values()

def getRow2(data,fields):

    row=OrderedDict([(i,'') for i in fields])

    for i,j in getFieldsNValues(data.record,''):
        row[i]=j

    if 'recordType' in fields and row['recordType']<5:

        if row['recordType']==3 or row['recordType']==4:

            for i,j in getFieldsNValues(data.key,''):

                if i!='nodeName/nameLen' and i!='nodeName/nodeUnicode':

                    if i=='parentID':
                        row['CNID']=j
                    else:
                        row[i]=j

        row['fullPath']=getFullPath(row['CNID'])

    if 'recordType' not in fields or (row['recordType']!=3 and row['recordType']!=4):
        for i,j in getFieldsNValues(data.key,''):
            row[i]=j
        
    return row.values()

getRow=[getRow1,getRow2]


es=300*'\x00'
tableFields={}
tableFields['Catalog_Leaf']=['journalOffset']
tableFields['Catalog_Leaf']+=genFields(getCatalogKey(es))
tableFields['Catalog_Leaf']+=genFields(getCatalogFile(es))
tableFields['Catalog_Leaf']+=genFields(getCatalogFolder(es))
tableFields['Catalog_Leaf']+=genFields(getCatalogThread(es))
tableFields['Catalog_Leaf'].append('fullPath')

tableFields['Extents_Leaf']=['journalOffset']
tableFields['Extents_Leaf']+=genFields(getExtentsKey(es))
tableFields['Extents_Leaf']+=genFields(ExtentsDataRec(getExtentDescriptor(es),getExtentDescriptor(es),getExtentDescriptor(es),
                            getExtentDescriptor(es),getExtentDescriptor(es),getExtentDescriptor(es),getExtentDescriptor(es),
                            getExtentDescriptor(es)))

tableFields['Attributes_Leaf']=['journalOffset']
tableFields['Attributes_Leaf']+=genFields(getAttributesKey(es))
tableFields['Attributes_Leaf']+=genFields(getAttributesForkData(es))
tableFields['Attributes_Leaf']+=genFields(getAttributesExtents(es))
tableFields['Attributes_Leaf']+=genFields(getAttributesData(es))

tableFields['Catalog_Index']=['journalOffset']
tableFields['Catalog_Index']+=genFields(getCatalogKey(es))
tableFields['Catalog_Index']+=genFields(BTPointer(0))

tableFields['Extents_Index']=['journalOffset']
tableFields['Extents_Index']+=genFields(getExtentsKey(es))
tableFields['Extents_Index']+=genFields(BTPointer(0))

tableFields['Attributes_Index']=['journalOffset']
tableFields['Attributes_Index']+=genFields(getAttributesKey(es))
tableFields['Attributes_Index']+=genFields(BTPointer(0))

tableFields['Header']=['journalOffset']
tableFields['Header']+=genFields(getBTHeaderRec(es))

tableFields['VolumeHeader']=['journalOffset']
tableFields['VolumeHeader']+=genFields(getVolumeHeader(2*es))


def outputRecord(form,table,fields,prefix,record,keyed):

    csv=form&1
    sql=form&2
    if csv:
        tc=table[csv]
        for i in prefix:
            tc.write(i+',')
        for i in getRow[keyed](record,fields):
            if type(i)==str or type(i)==unicode:
                i=i.replace('"','"""')
            elif type(i)==tuple or type(i)=list:
                i='"'+unicode(i).replace('"','"""')+'"'
            else:
                i=str(i)
            tc.write(i+',')
        tc.write('\n')

    if sql:
        row=getRow[keyed](record,fields)
        for i in range(len(row)):
            if type(row[i])==str or type(row[i])==unicode:
                row[i]=row[i].replace("'","''").replace('&','&&')
            elif type(row[i])==tuple or type(row[i])==list:
                row[i]="'"+str(row[i]).replace("'","''").replace('&','&&')+"'"
        cur.execute('insert into {0} values {1}'.format(table[sql],tuple(prefix+row)).replace("u'","'").replace('u"','"'))


fileTypes=['Catalog','Extents','Attributes']
recordTypes=['Leaf','Pointer','Header']

def initFileCSV(path,fileType,table={}):
    for i in recordTypes:
        fn='{0}_{1}'.format(fileType,i)
        t=open('{0}/{1}.csv'.format(path,fn),'w')
        table[fn]=t
        for j in tableFields[fn]:
            t.write('{0},'.format(j))
        t.write('\n')

    return table


def initJournalCSV(path):

    table={'VolumeHeader':open('{0}/Journal/VolumeHeader.csv'.format(path),'w')}

    for i in tableFields['VolumeHeader']:
        table['VolumeHeader'].write('{0},'.format(i))

    for i in fileTypes:
        initFileCSV(path,i,table)

    return table


def initSQL(path):

    con=sqlite3.connect('{0}'.format(path))
    con.isolation_level=None
    cur=con.cursor()

    cur.execute('CREATE TABLE VolumeHeader {0}'.format(tuple(tableFields['VolumeHeader'])))

    for i in fileTypes:
        for j in recordTypes:
            fn='{0}_{1}'.format(i,j)
            table[fn]=fn
            cur.execute('CREATE TABLE {0} {1}'.format(fn,tuple(tableFields[fn])))

    return table


def finishFileCSV(table,fileType):
    for i in recordTypes:
        table['{0}_{1}'.format(fileType,i)].close()


def finishJournalCSV(table):

    table['VolumeHeader'][0].close()
    for i in fileTypes:
        finishFileCSV(table,i)

def finishSQL():

    cur.close()
    con.close()


KeyExistence={'Catalog_Leaf':1,'Catalog_Index':1,'Catalog_Header':0,'Catalog_Map':-1,
            'Extents_Leaf':1,'Extents_Index':1,'Extents_Header':0,'Extents_Map':-1,
            'Attributes_Leaf':1,'Attributes_Index':1,'Attributes_Header':0,'Attributes_Map':-1,
            'VolumeHeader':0, 'Allocation':-1}



def journalParser(form,path,jParseList,bOffList):

    DirectoryCleaning(path+'/Journal')

    if form&1:
        table1=initCSV(path+'/Journal')
    if form&2:
        table2=initSQL(path+'/Journal/Journal.db')

    table={}
    for i in fileTypes:
        for j in recordTypes:
            fn='{0}_{1}'.format(i,j)
            table[fn]=[table1[fn],table2[fn]]

    for i in range(1,len(jParseList)):        

        blocks=jParseList[i][2]
        bOffs=bOffList[i].contain[2]

        for j in range(len(blocks)):

            block=blocks[j]
            bOff=bOffs.contain[j]
            bn=bOff.name
            
            if KeyExistence[bn]==1:
                tf=tableFields[bn]
                rl=block[1]
                rol=block[-1]
                for k in range(rl):
                    outputRecord(form,table[bn],tf,[bOff.offset+rol[k]],rl[k],1):

            elif KeyExistence[bn]==0:
                record=block
                if bn!='VolumeHeader':
                    record=block[1]
                    tf=tableFields[bn.find('_')+1:]
                else:
                    tf=tableFields[bn]
                outputRecord(form,table[bn],tf,[bOff.offset],record,0):

    if form&1:
        finishFileCSV(table)
    if form&2:
        finishSQL()


def specialFileParser(form,path,sepcialFile):

    if form&2:
        initSQL(path+'specialFile.db')

    for i in fileTypes:
        sf=specialFile[i]
        if sf==0:
            break
        if form&1:
            initFileCSV(path,fileType,table={})
        nodeSize,temp1,totalNodes=unpack_from('>HHL',sf,32)
        nodePointer=0
        for j in xrange(totalNodes):
            node=getBlock(buffer(sf,nodePointer,nodeSize),i)
            rt=recordTypes[node.NodeDescriptor.kind+1]
            nn='{0}_{1}'.format(i,rt)
            if KeyExistence[nn]==1:
                tf=tableFields[nn]
                rl=node[1]
                rol=node[-1]
                for k in range(rl):
                    outputRecord(form,table[nn],tf,[bOff.offset+rol[k]],rl[k],1):
            elif KeyExistence[nn]==0:
                record=node[1]
                tf=tableFields[rt]
                outputRecord(form,table[nn],tf,[bOff.offset],record,0):
            nodePointer+=nodeSize
        finishFileCSV(table,i)
    finishSQL()

def volumeInfo(path,vh):

    if vh!=0:
        f = open("{0}/VolumeInfo.txt".format(path),'w')
        for i in vh._asdict():
            f.write('{0} : {1}\n'.format(i,vh.__getattribute__(i)))
    
        f.close()