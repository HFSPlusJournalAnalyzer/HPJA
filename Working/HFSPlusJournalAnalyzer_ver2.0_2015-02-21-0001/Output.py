import sqlite3
from HFSPlus_sStructure import *
from collections import *
from HFSPlus_GetInstance import *
from types import *

def genTypes(seen,prefix,*standard):
    seen_add = seen.add
    types=[]
    for i in standard:
        for j,k in i.__dict__.iteritems():
            j=prefix+j
            try:
                k.__dict__
                types+=genTypes(seen,j+'/',k)

            except AttributeError:
                if not j in seen:
                    types.append(j)
                    seen_add(j)

    return types

def getTypesNFields(data,prefix):
    typesNFields=[]
    for i,j in data.__dict__.iteritems():
        i=prefix+i
        try:
            j.__dict__
            typesNFields+=getTypesNFields(j,i+'/')

        except AttributeError:
            typesNFields.append((i,j))

    return typesNFields

def getRow(data,types):
    fields=OrderedDict([(i,'') for i in types])
    for i,j in getTypesNFields(data.record,''):
        fields[i]=j
    if 'recordType' in fields and (fields['recordType']==3 or fields['recordType']==4):
        for i,j in getTypesNFields(data.key,''):
            if i!='nodeName/nameLen' and i!='nodeName/nodeUnicode':
                if i=='parentID':
                    fields['CNID']=j
                else:
                    fields[i]=j
    else :
        for i,j in getTypesNFields(data.key,''):
            fields[i]=j
        
                    
    return fields.values()

emptyString=300*'\x00'
CatalogLeafTypes=genTypes(set(),'',getCatalogKey(emptyString),getCatalogFile(emptyString),getCatalogFolder(emptyString),getCatalogThread(emptyString))
ExtentsLeafTypes=genTypes(set(),'',getExtentsKey(emptyString),ExtentsDataRec(getExtentDescriptor(emptyString),getExtentDescriptor(emptyString),getExtentDescriptor(emptyString),getExtentDescriptor(emptyString),getExtentDescriptor(emptyString),getExtentDescriptor(emptyString),getExtentDescriptor(emptyString),getExtentDescriptor(emptyString)))
AttrLeafTypes=genTypes(set(),'',getAttributesKey(emptyString),getAttributesForkData(emptyString),getAttributesExtents(emptyString),getAttributesData(emptyString))

def temp(path,jParseList):

    f = open("{0}/result1.txt".format(path),'w')
    for i in jParseList:
        f.write("-----------\n")
        for j in i:
            f.write(str(j)+"\n")
    
    f.close()


def volumeInfo(path,vh):

    if vh!=0:
        f = open("{0}/VolumeInfo.txt".format(path),'w')
        for i in vh.__dict__:
            f.write('{0} : {1}\n'.format(i,vh.__dict__[i]))
    
    f.close()

leafNodeTypes={'Catalog':CatalogLeafTypes,"Extents":ExtentsLeafTypes,"Attributes":AttrLeafTypes}

def outputNode(f,blocks):

    for i in range(len(blocks)):

        try:

            records=blocks[i].LeafRecList

            for j in range(len(records)):

                index=records[j].getType()
                lf=getRow(records[j],leafNodeTypes[index])

                for k in lf:
                    f[index].write((unicode(k).replace(',','","')+',').encode('utf-8'))
                f[index].write('\n')

        except AttributeError:
            pass


def rawCSV(path,jParseList):

    f={}
    for i in ['Catalog','Extents','Attributes']:
        f[i]=open('{0}/{1}.csv'.format(path,i),'w')
        for j in leafNodeTypes[i]:
            f[i].write('{0},'.format(j))
        f[i].write('\n')

    for i in range(1,len(jParseList)):
        outputNode(f,jParseList[i][2])

    for i in ['Catalog','Extents','Attributes']:
        f[i].close()


def rawSQLite3(path,jParseList):

    con=sqlite3.connect('{0}/sqlite3.db'.format(path))
    con.isolation_level=None
    cur=con.cursor()

    for i in ['Catalog','Extents','Attributes']:
        cur.execute('CREATE TABLE {0} {1}'.format(i,tuple(leafNodeTypes[i])))

    for i in range(1,len(jParseList)):

        blocks=jParseList[i][2]
        for j in range(len(blocks)):
            
            try:

                records=blocks[j].LeafRecList

                for k in range(len(records)):

                    index=records[k].getType()
                    lf=getRow(records[k],leafNodeTypes[index])
                    
                    print lf

                    for i in range(len(lf)):
                        if type(lf)==StringType or type(lf)==UnicodeType:
                            lf=lf.replace("'","''")
                        elif type(lf)==TupleType:
                            lf=unicode(lf)
                        lf[i]=lf[i].replace("'","''")

                    cur.execute(u'insert into {0} values {1}'.format(index,tuple(lf)).replace('"',"'"))

            except AttributeError:
                pass

    cur.close()
    con.close()