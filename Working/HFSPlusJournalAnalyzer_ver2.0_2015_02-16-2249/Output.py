from sqlalchemy import *

engine=create_engine('raw.db')

CatalogBase=declarative_base()
ExtentsBase=declarative_base()
AttrBase=declarative_base()

class CatalogLeaf(CatalogKey,CatalogFile,CatalogFolder,CatalogThread):

    __slots__=()

    def __init__(self,cdr):

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

class AttrLeaf(AttrKey,AttrForkData,AttrExtents,AttrData):

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
        for j in range(len(jParseList[i][2])):

            try:
    
                for k in range(len(jParseList[i][2][j].LeafRecList)):

                    index=jParseList[i][2][j].LeafRecList[k].getType()
                    lf=BTLeafType[index](jParseList[i][2][j].LeafRecList[k])

                    for l in lf.__dict__:
                        f[index].write(str(lf.__dict__[l]).replace(',',' ')+',')

                    f.write('\n')

            except AttributeError:
                pass

    for i in ['Catalog','Extents','Attributes']:
        f.close(f[i])


def rawSQLite3(path,jParseList):

    
