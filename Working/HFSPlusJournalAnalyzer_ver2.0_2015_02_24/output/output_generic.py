import sqlite3
from lib.format import *
from lib.hfs_instance import *
from lib.etc_util import *
from collections import *
from analysis.file_analysis import *

con=None
cur=None

def genFields(standard,prefix,seen=set()):
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


emptyString=300*'\x00'
CatalogLeafFields=genFields(set(),'',getCatalogKey(emptyString),getCatalogFile(emptyString),getCatalogFolder(emptyString),getCatalogThread(emptyString))
CatalogLeafFields.append('fullPath')
ExtentsLeafFields=genFields(set(),'',getExtentsKey(emptyString),ExtentsDataRec(getExtentDescriptor(emptyString),getExtentDescriptor(emptyString),
                                                                             getExtentDescriptor(emptyString),getExtentDescriptor(emptyString),
                                                                             getExtentDescriptor(emptyString),getExtentDescriptor(emptyString),
                                                                             getExtentDescriptor(emptyString),getExtentDescriptor(emptyString)))
AttrLeafFields=genFields(set(),'',getAttributesKey(emptyString),getAttributesForkData(emptyString),getAttributesExtents(emptyString),getAttributesData(emptyString))
CatalogIndexFields=genFields(set(),'',getCatalogKey(emptyString),BTPointer(0))
ExtentsIndexFields=genFields(set(),'',getExtentsKey(emptyString),BTPointer(0))
AttrIndexFields=genFields(set(),'',getAttributesKey(emptyString),BTPointer(0))
HeaderFields=genFields(set(),'',getBTHeaderRec(emptyString))

nodeFields={'Catalog':{'LeafRecList':CatalogLeafFields,'BTHeaderRec':HeaderFields,'PointerRecList':CatalogIndexFields}}
nodeFields['Extents']={'LeafRecList':ExtentsLeafFields,'BTHeaderRec':HeaderFields,'PointerRecList':ExtentsIndexFields}
nodeFields['Attributes']={'LeafRecList':AttrLeafFields,'BTHeaderRec':HeaderFields,'PointerRecList':AttrIndexFields}
volumeHeaderFields=genFields(set(),'',getVolumeHeader(2*emptyString))

def outputRecord(form,f,fields,record,keyed):
    if form&1:
        for i in getRow[keyed](record,fields):
            if type(i)==str or type(i)==unicode:
                i=i.replace('"','"""')
            elif type(i)==tuple or type(i)=list:
                i='"'+unicode(i).replace('"','"""')+'"'
            else:
                i=str(i)
            f.write(i+',')
        f.write('\n')

    if form&2:
        row=getRow[keyed](record,fields)
        for i in range(len(row)):
            if type(row[i])==str or type(row[i])==unicode:
                record[i]=record[i].replace("'","''").replace('&','&&')
            elif type(row[i])==tuple or type(row[i])==list:
                row[i]="'"+str(row[i]).replace("'","''").replace('&','&&')+"'"
        cur.execute('insert into {0} values {1}'.format(f,tuple(row)).replace("u'","'").replace('u"','"'))


fileTypes=['Catalog','Extents','Attributes']
recordTypes=['LeafRecList','PointerRecList','BTHeaderRec']

def initCSV(path):

    f={'VolumeHeader':open('{0}/Journal/VolumeHeader.csv'.format(path),'w')}

    for i in volumeHeaderFields:
        f['VolumeHeader'].write('{0},'.format(i))

    for i in fileTypes:

        f[i]={}

        for j in recordTypes:

            f[i][j]=open('{0}/Journal/{1}{2}.csv'.format(path,i,j),'w')

            for k in nodeFields[i][j]:
                f[i][j].write('{0},'.format(k))

            f[i][j].write('\n')

    return f

def initSQLite3(path):

    con=sqlite3.connect('{0}/Journal/Journal.db'.format(path))
    con.isolation_level=None
    cur=con.cursor()

    cur.execute('CREATE TABLE VolumeHeader {0}'.format(tuple(volumeHeaderFields)))

    for i in fileTypes:
        for j in recordTypes:
            cur.execute('CREATE TABLE {0}{1} {2}'.format(i,j,tuple(nodeFields[i][j])))


def journalParsing(form,path,jParseList):

    if form&1:
        f=initCSV(path)
    if form&2:
        initSQLite3(path)

    for i in range(1,len(jParseList)):        

        blocks=jParseList[i][2]

        for j in range(len(blocks)):

            block=blocks[j]

            try:
                records=block[1]

                if type(records)==list:

                    fileType=records[0].getType()
                    recType=block._fields[1]

                    nt=nodeFields[fileType][recType]

                    outputKeyedRec(f[fileType][recType],records,nt)

                elif block.__class__.__name__=='VolumeHeader':

                    for k in getRow2(block,volumeHeaderFields):
                        if type(k)==str or type(k)==unicode:
                            k=k.replace('"','"""')
                        elif type(k)==tuple or type(k)==list:
                            k='"'+unicode(k).replace('"','"""')+'"'
                        else:
                            k=str(k)
                        f['VolumeHeader'].write(unicode(k).encode('utf-8')+',')

                    f['VolumeHeader'].write('\n')

            except Exception:
                pass

    f['VolumeHeader'].close()

    for i in ['Catalog','Extents','Attributes']:
        for j in ['LeafRecList','BTHeaderRec','PointerRecList']:
            f[i][j].close()




    for i in range(1,len(jParseList)):

        blocks=jParseList[i][2]
        for j in range(len(blocks)):
            
            block=blocks[j]

            try:

                records=block[1]

                if type(records)==list:

                    fileType=records[0].getType()
                    recType=block._fields[1]

                    nt=nodeFields[fileType][recType]

                    for k in range(len(records)):

                        lf=getRow1(records[k],nt)

                        for i in range(len(lf)):
                            if type(lf[i])==tuple:
                                lf[i]=unicode(lf[i])
                            if type(lf[i])==str or type(lf[i])==unicode:
                                lf[i]=lf[i].replace("'","''").replace('&','&&')

                        cur.execute(u'insert into {0}{1} values {2}'.format(fileType,recType,tuple(lf)).replace("u'","'").replace('u"','"') .replace('"',"'"))

                elif block.__class__.__name__=='VolumeHeader':

                    vh=getRow2(block,volumeHeaderFields)

                    for i in range(len(vh)):
                        if type(vh[i])==tuple:
                            vh[i]=unicode(vh[i])
                        if type(vh[i])==str or type(vh[i])==unicode:
                            vh[i]=vh[i].replace("'","''").replace('&','&&')

                    cur.execute(u'insert into VolumeHeader values {0}'.format(tuple(vh)).replace("u'","'").replace('u"','"') .replace('"',"'"))

            except Exception:
                pass

    cur.close()
    con.close()


