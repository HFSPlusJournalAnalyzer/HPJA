import sqlite3
from HFSPlus_sStructure import *
from collections import *
from HFSPlus_GetInstance import *
from Utility import *
from Analyzer import *

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

def getRow1(data,types):

    fields=OrderedDict([(i,'') for i in types])
    for i,j in getTypesNFields(data.record,''):
        fields[i]=j
    if 'recordType' in fields

        if fields['recordType']==3 or fields['recordType']==4:
            for i,j in getTypesNFields(data.key,''):

                if i!='nodeName/nameLen' and i!='nodeName/nodeUnicode':

                    if i=='parentID':
                        fields['CNID']=j
                    else:
                        fields[i]=j

        fields['fullPath']=getFullPath(fields['CNID'])

    if 'recordType' not in fields or fields['recordType']==1 or fields['recordType']==2:
        for i,j in getTypesNFields(data.key,''):
            fields[i]=j
        
    return fields.values()

def getRow2(data,types):

    fields=OrderedDict([(i,'') for i in types])
    for i,j in getTypesNFields(data,''):
        fields[i]=j
        
    return fields.values()

emptyString=300*'\x00'
CatalogLeafTypes=genTypes(set(),'',getCatalogKey(emptyString),getCatalogFile(emptyString),getCatalogFolder(emptyString),getCatalogThread(emptyString)).append('fullPath')
ExtentsLeafTypes=genTypes(set(),'',getExtentsKey(emptyString),ExtentsDataRec(getExtentDescriptor(emptyString),getExtentDescriptor(emptyString),getExtentDescriptor(emptyString),getExtentDescriptor(emptyString),getExtentDescriptor(emptyString),getExtentDescriptor(emptyString),getExtentDescriptor(emptyString),getExtentDescriptor(emptyString)))
AttrLeafTypes=genTypes(set(),'',getAttributesKey(emptyString),getAttributesForkData(emptyString),getAttributesExtents(emptyString),getAttributesData(emptyString))
CatalogIndexTypes=genTypes(set(),'',getCatalogKey(emptyString),BTPointer(0))
ExtentsIndexTypes=genTypes(set(),'',getCatalogKey(emptyString),BTPointer(0))
AttrIndexTypes=genTypes(set(),'',getCatalogKey(emptyString),BTPointer(0))
HeaderTypes=genTypes(set(),'',getHeaderNode(emptyString))

nodeTypes={'Catalog':{'LeafRecList':CatalogLeafTypes,'BTHeaderRec':HeaderTypes,'PointerRecList':CatalogIndexTypes}}
nodeTypes['Extents']={'LeafRecList':ExentsLeafTypes,'BTHeaderRec':HeaderTypes,'PointerRecList':ExtentsIndexTypes}
nodeTypes['Attr']={'LeafRecList':AttrLeafTypes,'BTHeaderRec':HeaderTypes,'PointerRecList':AttrIndexTypes}
volumeHeaderTypes=genTypes(set(),'',getVolumeHeader(2*emptyString))

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

def outputKeyedRec(f,records,nodeType):

    for i in range(len(records)):
        for j in getRow1(records[j],nodeType):
            f.write((unicode(j).replace(',','","')+',').encode('utf-8'))
        f.write('\n')


def rawCSV(path,jParseList):

    f={'VolumeHeader':open('{0}/VolumeHeader.csv'.format(path),'w')}

    for i in ['Catalog','Extents','Attributes']:

        f[i]={}

        for j in ['LeafRecList','BTHeaderRec','PointerRecList']:

            f[i][j]=open('{0}/{1}{2}.csv'.format(path,i,j),'w')

            for k in nodeTypes[i][j]:
                f[i][j].write('{0},'.format(k))

            f[i][j].write('\n')

    for i in range(1,len(jParseList)):        

        blocks=jParseList[i][2]

        for j in range(len(blocks)):

            block=blocks[j]
            records=block[1]

            if type(records)==list:

                nt=nodeTypes[records[0].getType()][block._fields[1]]

                outputKeyedRec(f[records[0].getType()][blocks._fields[1]],records,nt)

            '''
            elif block.__class__.__name__=="HeaderNode":

                for k in getRow2(blocks,nodeTypes[]['BTHeaderRec']):
                    f.write((unicode(j).replace(',','","')+',').encode('utf-8'))
                f.write('\n')
            '''

            elif block.__class__.__name__=='VolumeHeader':
                for k in getRow2(block,volumeHeaderTypes):
                    f[''].write((unicode(j).replace(',','","')+',').encode('utf-8'))
                f.write('\n')

    f['VolumeHeader'].close()

    for i in ['Catalog','Extents','Attributes']:
        for j in ['LeafRecList','BTHeaderRec','PointerRecList']:
            f[i][j].close()


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

                    for i in range(len(lf)):
                        if type(lf)==tuple:
                            lf=unicode(lf)
                        if type(lf)==str or type(lf)==unicode:
                            lf=lf.replace("'","''").replace('"',"'")

                    cur.execute(u'insert into {0} values {1}'.format(index,tuple(lf)).replace("u'","'"))

            except AttributeError:
                pass

    cur.close()
    con.close()


def recovery(disk,path,target,jParseList,vh):
    d=target.find(',')
    CNID=int(target[1:d])
    nodeName=target[d+1:-1]
    for i in range(len(jParseList)-1,0,-1):

        blocks=jParseList[i][2]
        for j in range(len(blocks)-1,-1,0):
            
            try:

                records=blocks[j].LeafRecList

                if 'Catalog'==records[0].getType():

                    for k in range(len(records)):

                        if records.key.nodeName.nodeUnicode==unicode(nodeName) and records.record.CNID==CNID:

                            dataFork=[]
                            extents=records.record.dataFork.extents
                            for l in extents.__dict__.itervalues():
                                dataFork.append(DiskDump(disk,'',vh.blockSize,l.startBlock,l.blockCount))
                            dataFork=''.join(dataFork)
                            f=open('{0}/{1}_DataFork'.format(path,nodeName),'wb')
                            f.write(dataFork)
                            f.close()

                            resourceFork=[]
                            extents=records.record.resourceFork.extents
                            for l in extents.__dict__.itervalues():
                                resourceFork.append(DiskDump(disk,'{0}/{1}'.format(path,nodeName),vh.blockSize,l.startBlock,l.blockCount))
                            resourceFork=''.join(resourceFork)
                            f=open('{0}/{1}_ResourceFork'.format(path,nodeName),'wb')
                            f.write(resourceFork)
                            f.close()

                            return


            except AttributeError:
                pass




