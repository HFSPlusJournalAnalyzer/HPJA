import sqlite3
from HFSPlus_sStructure import *
from collections import *

def genTypes(seq,seen):
    seen_add = seen.add
    types=[]
    for i in seq:
        try:
            types+=genTypes(i._fields,seen)

        except AttributeError:
            if not i in seen:
                types.append(i)
                seen_add(i)

    return types

def getTypesNFields(data):
    typesNFields=[]
    for i,j in data.iteritems():
        try:
            typesNFields+=getTypesNFields(j.__dict__)

        except AttributeError:
            typesNFields.append((i,j))

    return typesNFields

def getRow(data,types):
    fields=OrderedDict([(i,'') for i in types])
    for i,j in getTypesNFields(data):
        fields[i]=j
    return fields.values()


CatalogLeafTypes=genTypes(CatalogKey._fields+CatalogFile._fields+CatalogFolder._fields+CatalogThread._fields,set())
ExtentsLeafTypes=genTypes(ExtentsKey._fields+ExtentsDataRec._fields,set())
AttrLeafTypes=genTypes(AttrKey._fields+AttrForkData._fields+AttrExtents._fields+AttrData._fields,set())

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

        print type(blocks[i])

        try:

            records=blocks[i].LeafRecList

            for j in range(len(records)):

                index=records[j].getType()
                print index
                lf=getRow(records[j],leafNodeTypes[index])

                for k in lf:
                    f[index].write((unicode(lf).replace(',','","')+',').encode('utf-8'))
                f[index].write('\n')

        except AttributeError:
            pass


def rawCSV(path,jParseList):

    f={}
    for i in ['Catalog','Extents','Attributes']:
        f[i]=open('{0}/{1}.csv'.format(path,i),'w')
        for j in leafNodeTypes:
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
        cur.execute('CREATE TABLE {0} {1}'.format(i,tuple(leafNodeTypes)).replace("'",''))

    for i in range(1,len(jParseList)):

        blocks=jParseList[i][2]
        for j in range(len(blocks)):
            
            try:

                records=blocks[j].LeafRecList

                for k in range(len(records)):

                    index=records[j].getType()
                    lf=getRow(records[j],leafNodeTypes[index])
                    
                    print lf
                    cur.execute(u'insert into {0} values {1}'.format(index,tuple(lf)).replace('[','(').replace(']',')'))

            except AttributeError:
                pass

    cur.close()
    con.close()