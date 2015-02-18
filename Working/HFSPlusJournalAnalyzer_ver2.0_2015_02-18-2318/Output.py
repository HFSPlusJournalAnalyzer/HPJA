import sqlite3

class CatalogLeaf(CatalogKey,CatalogFile,CatalogFolder,CatalogThread):

    __slots__=()

    def __init__(self,cdr):

        for i in CatalogLeaf._fields:
            self.__dict__[i]=''

        if cdr.record.recordType<3:

            for i in cdr.key.__dict__:
                self.__dict__[i]=cdr.key.__dict__[i]

        else:
            self.CNID=cdr.key.parentID

        for i in cdr.record.__dict__:
            self.__dict__[i]=cdr.record.__dict__[i]


class ExtentsLeaf(ExtentsKey,ExtentsDataRec):

    __slots__=()

    def __init__(self,edr):

        for i in edr.key.__dict__:
            self.__dict__[i]=edr.key.__dict__[i]

        for i in edr.record.__dict__:
            self.__dict__[i]=edr.record.__dict__[i]


class AttrLeaf(AttrBase,AttrKey,AttrForkData,AttrExtents,AttrData):

    __slots__=()

    def __init__(self,adr):

        for i in adr.key.__dict__:
            self.__dict__[i]=adr.key.__dict__[i]

        for i in adr.record.__dict__:
            self.__dict__[i]=adr.record.__dict__[i]


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


def outputNode(f,node):

    for i in range(len(node)):

            try:
    
                for j in range(len(node[i].LeafRecList)):

                    index=node[i].LeafRecList[j].getType()
                    lf=BTLeafType[index](node[i].LeafRecList[j])

                    for k in lf.__dict__:
                        f[index].write(str(lf.__dict__[k]).replace(',',' ')+',')

                    f[index].write('\n')

            except AttributeError:
                pass


def rawcsv(path,jParseList):

    BTLeafType={'Catalog':CatalogLeaf,"Extents":ExtentsLeaf,"Attributes":AttrLeaf}

    for i in BTType:
        f.append(open('{0}/{1}.csv'.format(path,i),'w'))

    f={}
    for i in ['Catalog','Extents','Attributes']:
        for j in BTLeafType[i]._fields:
            f[i].write('{0},'.format(j))
        f[i].write('\n')

    for i in range(1,len(jParseList)):
        outputNode(jParseList[i][2])

    for i in ['Catalog','Extents','Attributes']:
        f.close(f[i])


def rawSQLite3(path,jParseList):

    BTLeafType={'Catalog':CatalogLeaf,"Extents":ExtentsLeaf,"Attributes":AttrLeaf}

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
                    lf=BTLeafType[index](node[i].LeafRecList[j])
                    
                    cur.excute('insert into {0} values {1}'.format(index,[lf.__dict__[k] for k in lf.__dict__]).replace('[','(').replace(']',')')

            except AttributeError:
                pass

    cur.close()
    con.close()

        



    
