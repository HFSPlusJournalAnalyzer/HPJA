import sqlite3
from lib.format import *
from lib.hfs_instance import *
from lib.etc_util import *
from collections import *
from analysis.file_analysis import *

con=None
cur=None

fileTypes=['Catalog','Extents','Attributes']
recordTypes=['Leaf','Index','Header']
KeyExistence={'Catalog_Leaf':1,'Catalog_Index':1,'Catalog_Header':0,'Catalog_Map':-1,
            'Extents_Leaf':1,'Extents_Index':1,'Extents_Header':0,'Extents_Map':-1,
            'Attributes_Leaf':1,'Attributes_Index':1,'Attributes_Header':0,'Attributes_Map':-1,
            'VolumeHeader':0, 'Allocation':-1}

def genFields(standard,prefix,seen):

    fields=[]
    try:
        for i,j in standard._asdict().iteritems():    
            fields+=genFields(j,prefix+i+'/',seen)

    except AttributeError:
        if not prefix in seen:
            fields.append(prefix)
            seen.add(prefix)

    return fields


def getFieldsNValues(data,prefix):

    fieldsNValues=[]
    try:
        for i,j in data._asdict().iteritems():
            fieldsNValues+=getFieldsNValues(j,prefix+i+'/')

    except AttributeError:
        fieldsNValues.append((prefix,data))

    return fieldsNValues


def getRow1(data,fields):

    row=OrderedDict([(i,'') for i in fields])
    for i,j in getFieldsNValues(data,''):
        row[i]=j
        
    return row.values()

def getRow2(data,fields):

    row=OrderedDict([(i,'') for i in fields])
    for i,j in getFieldsNValues(data.key,''):
        row[i]=j

    try:
        row['CNID/']
        row['CNID/']=row['parentID/']
    except KeyError:
        pass

    for i,j in getFieldsNValues(data.record,''):
        row[i]=j

    try:
        row['fullPath/']
        row['fullPath/']=getFullPath(row['CNID/'])
    except KeyError:
        pass
        
    return row.values()

getRow=[getRow1,getRow2]

es=300*'\x00'
tableFields={}
for i,j in KeyExistence.iteritems():
    tableFields[i]=['offset/']

s=set()
tableFields['Catalog_Leaf']+=genFields(getCatalogKey(es),'',s)
tableFields['Catalog_Leaf']+=genFields(getCatalogFile(es),'',s)
tableFields['Catalog_Leaf']+=genFields(getCatalogFolder(es),'',s)
tableFields['Catalog_Leaf']+=genFields(getCatalogThread(es),'',s)
tableFields['Catalog_Leaf'].append('fullPath/')

s=set()
ed=getExtentDescriptor(es)
tableFields['Extents_Leaf']+=genFields(getExtentsKey(es),'',s)
tableFields['Extents_Leaf']+=genFields(ExtentsDataRec(ed,ed,ed,ed,ed,ed,ed,ed),'',s)

s=set()
tableFields['Attributes_Leaf']+=genFields(getAttributesKey(es),'',s)
tableFields['Attributes_Leaf']+=genFields(getAttributesForkData(es),'',s)
tableFields['Attributes_Leaf']+=genFields(getAttributesExtents(es),'',s)
tableFields['Attributes_Leaf']+=genFields(getAttributesData(es),'',s)

tableFields['Catalog_Index']+=genFields(getCatalogKey(es),'',set())
tableFields['Catalog_Index']+=genFields(BTPointer(0),'',set())

tableFields['Extents_Index']+=genFields(getExtentsKey(es),'',set())
tableFields['Extents_Index']+=genFields(BTPointer(0),'',set())

tableFields['Attributes_Index']+=genFields(getAttributesKey(es),'',set())
tableFields['Attributes_Index']+=genFields(BTPointer(0),'',set())

tableFields['Catalog_Header']+=genFields(getBTHeaderRec(es),'',set())

tableFields['Extents_Header']+=genFields(getBTHeaderRec(es),'',set())

tableFields['Attributes_Header']+=genFields(getBTHeaderRec(es),'',set())

tableFields['VolumeHeader']+=genFields(getVolumeHeader(2*es),'',set())


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
                row[i]=row[i].replace('"','"""').replace('\r','')
            elif type(row[i])==tuple or type(row[i])==list:
                row[i]='"{0}"'.format(str(row[i]).replace('"','"""'))
            elif row[i].__class__==Binary:
                row[i]='"{0}"'.format(str(row[i]).replace('"','"""')).encode('string_escape')
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
            if type(row[i])==str or type(row[i])==unicode:
                row[i]=row[i].replace("'","''").replace('&','&&')
            elif type(row[i])==tuple or type(row[i])==list:
                row[i]="'{0}'".format(str(row[i]).replace("'","''").replace('&','&&'))
            elif row[i].__class__==Binary:
                row[i]=str(row[i]).replace("'","''").replace('&','&&')
        cur.execute('insert into {0} values {1}'.format(table[sql],tuple(row)).replace("u'","'").replace('u"','"').replace("\\'\\'","''"))


def initFileCSV(path,fileType):
    table={}
    for i in recordTypes:
        fn='{0}_{1}'.format(fileType,i)
        t=open('{0}/{1}.csv'.format(path,fn),'w')
        table[fn]=t
        for j in tableFields[fn]:
            t.write(j[:-1]+',')
        t.write('\n')

    return table


def initJournalCSV(path):

    table={'VolumeHeader':open('{0}/VolumeHeader.csv'.format(path),'w')}

    for i in tableFields['VolumeHeader']:
        table['VolumeHeader'].write(i[:-1]+',')
    table['VolumeHeader'].write('\n')

    for i in fileTypes:
        table.update(initFileCSV(path,i))

    return table


def initSQL(path):

    global con,cur

    con=sqlite3.connect('{0}'.format(path))
    con.isolation_level=None
    cur=con.cursor()
    
    table={'VolumeHeader':'VolumeHeader'}
    col=[]
    for i in tableFields['VolumeHeader']:
        col.append(i[:-1])
    cur.execute('CREATE TABLE VolumeHeader {0}'.format(tuple(col)))
    for i in fileTypes:
        for j in recordTypes:
            fn='{0}_{1}'.format(i,j)
            table[fn]=fn
            col=[]
            for k in tableFields[fn]:
                col.append(k[:-1])
            cur.execute('CREATE TABLE {0} {1}'.format(fn,tuple(col)))
    
    return table


def finishFileCSV(table,fileType):
    for i in recordTypes:
        table['{0}_{1}'.format(fileType,i)][1].close()


def finishJournalCSV(table):

    table['VolumeHeader'][1].close()
    for i in fileTypes:
        finishFileCSV(table,i)

def finishSQL():

    global cur,con

    cur.close()
    con.close()

def outputParsedJournal(form,path,jParseList,bOffList):

    DirectoryCleaning(path+'/Journal')

    table={i:[None,None,None] for i in KeyExistence.keys()}
    if form&1:
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
            if KeyExistence[bn]==1:
                tf=tableFields[bn]
                rl=block[1]
                rol=block[-1]
                for k in range(len(rl)):
                    outputRecord(form,table[bn],tf,[bOff.offset+rol[k]],rl[k],1)

            elif KeyExistence[bn]==0:
                tf=tableFields[bn]
                record=block
                if bn!='VolumeHeader':
                    record=block[1]
                outputRecord(form,table[bn],tf,[bOff.offset],record,0)

    if form&1:
        finishJournalCSV(table)
    if form&2:
        finishSQL()

'''
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
'''


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

    for i in fileTypes:
        sf=specialFile[i]
        if sf==0:
            break
        nodeSize,temp1,totalNodes=unpack_from('>HHL',sf,32)
        nodePointer=0
        for j in xrange(totalNodes):
            node=getBlock(buffer(sf,nodePointer,nodeSize),i)
            if node.NodeDescriptor.kind<2:
                nn='{0}_{1}'.format(i,recordTypes[node.NodeDescriptor.kind+1])
                if KeyExistence[nn]==1:
                    tf=tableFields[nn]
                    rl=node[1]
                    rol=node[-1]
                    for k in range(len(rl)):
                        outputRecord(form,table[nn],tf,[nodePointer+rol[k]],rl[k],1)
                elif KeyExistence[nn]==0:
                    record=node[1]
                    tf=tableFields[nn]
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