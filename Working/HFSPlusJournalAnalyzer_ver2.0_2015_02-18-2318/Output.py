import sqlite3
from HFSPlus_sStructure import *

def listDedupl(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if not (x in seen or seen_add(x))]

CatalogLeaf=namedtuple('CatalogLeaf',listDedupl(CatalogKey._fields,CatalogFile._fields,CatalogFolder._fields,CatalogThread._fields))
ExtentsLeaf=namedtuple('ExtentsLeaf',listDedupl(ExtentsKey._fields,ExtentsDataRec._fields))
AttrLeaf=namedtuple('AttrLeaf',listDedupl(AttrKey._fields,AttrForkData._fields,AttrExtents._fields,AttrData._fields))

def getCatalogLeaf(cdr):

    vec=dict([(i,'') for i in CatalogLeaf._fields])

    if cdr.record.recordType<3:

        for i in cdr.key.__dict__:
            vec[i]=cdr.key.__dict__[i]

    else:
        vec['CNID']=cdr.key.parentID

    for i in cdr.record.__dict__:
        vec[i]=cdr.record.__dict__[i]

    return CatalogLeaf(*vec.values())


def getExtentsLeaf(edr):

    vec={}

    for i in edr.key.__dict__:
        vec[i]=edr.key.__dict__[i]

    for i in edr.record.__dict__:
        vec[i]=edr.record.__dict__[i]

    return ExtentsLeaf(*vec.values())


def getAttrLeaf(adr):

    vec=dict([(i,'') for i in AttrLeaf._fields])

    for i in adr.key.__dict__:
        vec[i]=adr.key.__dict__[i]

    for i in adr.record.__dict__:
        vec[i]=adr.record.__dict__[i]

    return AttrLeaf(*vec.values())


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

getLeafNode={'Catalog':getCatalogLeaf,"Extents":getExtentsLeaf,"Attributes":getAttrLeaf}

def outputNode(f,node):

    for i in range(len(node)):

            try:
    
                for j in range(len(node[i].LeafRecList)):

                    index=node[i].LeafRecList[j].getType()
                    lf=getLeafNode[index](node[i].LeafRecList[j])

                    for k in lf.__dict__:
                        f[index].write(str(lf.__dict__[k]).replace(',',' ')+',')

                    f[index].write('\n')

            except AttributeError:
                pass


def rawCSV(path,jParseList):

    f={}
    for i in ['Catalog','Extents','Attributes']:
        f[i]=open('{0}/{1}.csv'.format(path,i),'w')
        for j in BTLeafType[i]._fields:
            f[i].write('{0},'.format(j))
        f[i].write('\n')

    for i in range(1,len(jParseList)):
        outputNode(f,jParseList[i][2])

    for i in ['Catalog','Extents','Attributes']:
        f.close(f[i])


def rawSQLite3(path,jParseList):


    con=sqlite3.connect('{0}/sqlite3.db'.format(path))
    con.isolation_level=None
    cur=con.cursor()

    for i in ['Catalog','Extents','Attributes']:
        cur.excute('CREATE TABLE {0} {1}'.format(i,BTLeafType[i]._fields).replace("'",''))

    for i in range(1,len(jParseList)):
        for i in range(len(node)):

            try:
    
                for j in range(len(node[i].LeafRecList)):

                    index=node[i].LeafRecList[j].getType()
                    lf=getLeafNode[index](node[i].LeafRecList[j])
                    
                    cur.excute('insert into {0} values {1}'.format(index,[lf.__dict__[k] for k in lf.__dict__]).replace('[','(').replace(']',')'))

            except AttributeError:
                pass

    cur.close()
    con.close()

        



    
