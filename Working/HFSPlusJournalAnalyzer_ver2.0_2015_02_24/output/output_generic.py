import sqlite3
from lib.format import *
from lib.hfs_instance import *
from lib.etc_util import *
from collections import *
from analysis.file_analysis import *

con=None
cur=None

def genFields(prefix,seen,*standard):

    fields=[]
    for i in standard:
        for j,k in i._asdict().iteritems():
            j=prefix+j
            try:
                k._asdict()
                fields+=genFields(j+'/',seen,k)

            except AttributeError:
                if not j in seen:
                    fields.append(j)
                    seen.add(j)
    return fields


def getFieldsNValues(data,prefix):
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

prefixes=['offset']

es=300*'\x00'
tableFields={}
tableFields['Catalog_Leaf']=prefixes+genFields('',set(),getCatalogKey(es),getCatalogFile(es),getCatalogFolder(es),getCatalogThread(es))
tableFields['Catalog_Leaf'].append('fullPath')
ed=getExtentDescriptor(es)
tableFields['Extents_Leaf']=prefixes+genFields('',set(),getExtentsKey(es),ExtentsDataRec(ed,ed,ed,ed,ed,ed,ed,ed))
tableFields['Attributes_Leaf']=prefixes+genFields('',set(),getAttributesKey(es),getAttributesForkData(es),getAttributesExtents(es),getAttributesData(es))
tableFields['Catalog_Index']=prefixes+genFields('',set(),getCatalogKey(es),BTPointer(0))
tableFields['Extents_Index']=prefixes+genFields('',set(),getExtentsKey(es),BTPointer(0))
tableFields['Attributes_Index']=prefixes+genFields('',set(),getAttributesKey(es),BTPointer(0))
tableFields['Catalog_Header']=prefixes+genFields('',set(),getBTHeaderRec(es))
tableFields['Extents_Header']=prefixes+genFields('',set(),getBTHeaderRec(es))
tableFields['Attributes_Header']=prefixes+genFields('',set(),getBTHeaderRec(es))
tableFields['VolumeHeader']=prefixes+genFields('',set(),getVolumeHeader(2*es))


def outputRecord(form,table,fields,prefix,record,keyed):

    csv=form&1
    sql=form&2
    row=getRow[keyed](record,fields)
    if csv:
        tc=table[csv]
        for i,j in enumerate(prefix):
            row[i]=j
        for i in range(len(row)):
            if type(row[i])==str or type(row[i])==unicode:
                row[i]=row[i].replace('"','"""')
            elif type(row[i])==tuple or type(row[i])==list:
                row[i]='"{0}"'.format(str(row[i]).replace('"','"""'))
            else:
                row[i]=str(row[i])
            if type(row[i])==unicode:
                tc.write(row[i].encode('utf-8'))
            else:
                tc.write(row[i])
            tc.write(',')
        tc.write('\n')

    if sql:
        for i,j in enumerate(prefix):
            row[i]=j
        for i in range(len(row)):
            if type(row[i])==Binary:
                row[i]=str(row[i])
            if type(row[i])==str or type(row[i])==unicode:
                row[i]=row[i].replace("'","''").replace('&','&&')
            elif type(row[i])==tuple or type(row[i])==list:
                row[i]="'{0}'".format(str(row[i]).replace("'","''").replace('&','&&'))
        cur.execute('insert into {0} values {1}'.format(table[sql],tuple(row)).replace("u'","'").replace('u"','"').replace('\\',':'))


fileTypes=['Catalog','Extents','Attributes']
recordTypes=['Leaf','Index','Header']

def initFileCSV(path,fileType):
    table={}
    for i in recordTypes:
        fn='{0}_{1}'.format(fileType,i)
        t=open('{0}/{1}.csv'.format(path,fn),'w')
        table[fn]=t
        for j in tableFields[fn]:
            t.write('{0},'.format(j))
        t.write('\n')

    return table


def initJournalCSV(path):

    table={'VolumeHeader':open('{0}/VolumeHeader.csv'.format(path),'w')}

    for i in tableFields['VolumeHeader']:
        table['VolumeHeader'].write(i+',')
    table['VolumeHeader'].write('\n')

    for i in fileTypes:
        table.update(initFileCSV(path,i))

    return table


def initSQL(path):

    global con,cur

    con=sqlite3.connect('{0}'.format(path))
    con.isolation_level=None
    cur=con.cursor()
    
    cur.execute('CREATE TABLE VolumeHeader {0}'.format(tuple(tableFields['VolumeHeader'])))

    table={'VolumeHeader':'VolumeHeader'}
    for i in fileTypes:
        for j in recordTypes:
            fn='{0}_{1}'.format(i,j)
            table[fn]=fn
            cur.execute('CREATE TABLE {0} {1}'.format(fn,tuple(tableFields[fn])))
    
    return table


def finishFileCSV(table,fileType):
    for i in recordTypes:
        table['{0}_{1}'.format(fileType,i)][1].close()


def finishJournalCSV(table):

    table['VolumeHeader'][1].close()
    for i in fileTypes:
        finishFileCSV(table,i)

def finishSQL():

    cur.close()
    con.close()


KeyExistence={'Catalog_Leaf':1,'Catalog_Index':1,'Catalog_Header':0,'Catalog_Map':-1,
            'Extents_Leaf':1,'Extents_Index':1,'Extents_Header':0,'Extents_Map':-1,
            'Attributes_Leaf':1,'Attributes_Index':1,'Attributes_Header':0,'Attributes_Map':-1,
            'VolumeHeader':0, 'Allocation':-1}

def outputParsedJournal(form,path,jParseList,bOffList):

    DirectoryCleaning(path+'/Journal')

    table={i:[None,None,None] for i in KeyExistence.keys()}
    if form&1:
        table={'path':open('{0}/VolumeHeader.csv'.format(path),'w')}
        table1=initJournalCSV(path+'/Journal')
        for i,j in table1.iteritems():
            table[i][1]=j
    if form&2:
        table2=initSQL(path+'/Journal/Journal.db')
        for i,j in table2.iteritems():
            table[i][2]=j


    for i in range(1,len(jParseList)):        

        blocks=jParseList[i][2]
        bOffs=bOffList[1].contain[i-1].contain[2]

        for j in range(len(blocks)):

            block=blocks[j]
            bOff=bOffs.contain[j]
            bn=bOff.name
            tf=tableFields[bn]
            if KeyExistence[bn]==1:
                rl=block[1]
                rol=block[-1]
                for k in range(len(rl)):
                    outputRecord(form,table[bn],tf,[bOff.offset+rol[k]],rl[k],1)

            elif KeyExistence[bn]==0:
                record=block
                if bn!='VolumeHeader':
                    record=block[1]
                outputRecord(form,table[bn],tf,[bOff.offset],record,0)

    if form&1:
        finishJournalCSV(table)
    if form&2:
        finishSQL()


def outputCoreFields(form,path,jParseList,bOffList):

    tf=['offset', 'keyLength', 'parentID', 'nodeName/nodeUnicode', 'recordType', 'CNID', 'createDate', 'contentModDate', 'attributesDate', 'accessDate', 'permissions/ownerID', 'permissions/groupID', 'dataFork', 'resourceFork', 'valence', 'fullPath']

    table=[None,None,None]
    
    if form&1:
        table[1]=open('{0}/Journal/Summary_Catalog_Leaf.csv'.format(path),'w')

    if form&2:
        con=sqlite3.connect('{0}/Journal/Journal.db'.format(path))
        con.isolation_level=None
        cur=con.cursor()
        cur.execute('CREATE TABLE Summary_Catalog_Leaf {0}'.format(tuple(tf)))
        table[2]='Summary_Catalog_Leaf'


    for i in range(1,len(jParseList)):

        blocks=jParseList[i][2]
        bOffs=bOffList[1].contain[i-1].contain[2]

        for j in range(len(blocks)):

            block=blocks[j]
            bOff=bOffs.contain[j]
            if bOff.name=='Catalog_Leaf':
                rl=block[1]
                rol=block[-1]
                for k in range(len(rl)):
                    outputRecord(form,table,tf,[bOff.offset+rol[k]],rl[k],1)

    if form&1:
        table[1].close()
    if form&2:
        finishSQL()


def outputParsedspecialFile(form,path,specialFile):

    table={i:[None,None,None] for i in KeyExistence.keys()}
    if form&1:
        table1=initJournalCSV(path)
        for i,j in table1.iteritems():
            table[i][1]=j
    if form&2:
        table2=initSQL(path+'/fileSystem.db')
        for i,j in table2.iteritems():
            table[i][2]=j

    table={}
    for i in fileTypes:
        sf=specialFile[i]
        if sf==0:
            break
        nodeSize,temp1,totalNodes=unpack_from('>HHL',sf,32)
        nodePointer=0
        for j in xrange(totalNodes):
            node=getBlock(buffer(sf,nodePointer,nodeSize),i)
            nn='{0}_{1}'.format(i,recordTypes[node.NodeDescriptor.kind+1])
            tf=tableFields[nn]
            if KeyExistence[nn]==1:
                rl=node[1]
                rol=node[-1]
                for k in range(len(rl)):
                    outputRecord(form,table[nn],tf,[nodePointer+rol[k]],rl[k],1)
            elif KeyExistence[nn]==0:
                record=node[1]
                outputRecord(form,table[nn],tf,[nodePointer],record,0)
            nodePointer+=nodeSize
        finishFileCSV(table,i)
    finishSQL()

def volumeInfo(path,vh):

    if vh!=0:
        f = open("{0}/VolumeInfo.txt".format(path),'w')
        for i in vh._asdict():
            f.write('{0} : {1}\n'.format(i,vh.__getattribute__(i)))
    
        f.close()