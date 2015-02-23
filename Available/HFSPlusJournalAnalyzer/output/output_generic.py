import sqlite3
from lib.format import *
from lib.hfs_instance import *
from lib.etc_util import *
from collections import *
from analysis.file_analysis import *



def genTypes(seen,prefix,*standard):
    seen_add = seen.add
    types=[]
    for i in standard:
        for j,k in i._asdict().iteritems():
            j=prefix+j
            try:
                k._asdict()
                types+=genTypes(seen,j+'/',k)

            except AttributeError:
                if not j in seen:
                    types.append(j)
                    seen_add(j)

    return types


def getTypesNFields(data,prefix):
    typesNFields=[]
    for i,j in data._asdict().iteritems():
        i=prefix+i
        try:
            j._asdict()
            typesNFields+=getTypesNFields(j,i+'/')

        except AttributeError:
            typesNFields.append((i,j))

    return typesNFields


def getRow1(data,types):

    fields=OrderedDict([(i,'') for i in types])

    for i,j in getTypesNFields(data.record,''):
        fields[i]=j

    if 'recordType' in fields and fields['recordType']<5:

        if fields['recordType']==3 or fields['recordType']==4:

            for i,j in getTypesNFields(data.key,''):

                if i!='nodeName/nameLen' and i!='nodeName/nodeUnicode':

                    if i=='parentID':
                        fields['CNID']=j
                    else:
                        fields[i]=j

        fields['fullPath']=getFullPath(fields['CNID'])

    if 'recordType' not in fields or (fields['recordType']!=3 and fields['recordType']!=4):
        for i,j in getTypesNFields(data.key,''):
            fields[i]=j
        
    return fields.values()


def getRow2(data,types):

    fields=OrderedDict([(i,'') for i in types])
    for i,j in getTypesNFields(data,''):
        fields[i]=j
        
    return fields.values()


emptyString=300*'\x00'
CatalogLeafTypes=genTypes(set(),'',getCatalogKey(emptyString),getCatalogFile(emptyString),getCatalogFolder(emptyString),getCatalogThread(emptyString))
CatalogLeafTypes.append('fullPath')
ExtentsLeafTypes=genTypes(set(),'',getExtentsKey(emptyString),ExtentsDataRec(getExtentDescriptor(emptyString),getExtentDescriptor(emptyString),
                                                                             getExtentDescriptor(emptyString),getExtentDescriptor(emptyString),
                                                                             getExtentDescriptor(emptyString),getExtentDescriptor(emptyString),
                                                                             getExtentDescriptor(emptyString),getExtentDescriptor(emptyString)))
AttrLeafTypes=genTypes(set(),'',getAttributesKey(emptyString),getAttributesForkData(emptyString),getAttributesExtents(emptyString),getAttributesData(emptyString))
CatalogIndexTypes=genTypes(set(),'',getCatalogKey(emptyString),BTPointer(0))
ExtentsIndexTypes=genTypes(set(),'',getExtentsKey(emptyString),BTPointer(0))
AttrIndexTypes=genTypes(set(),'',getAttributesKey(emptyString),BTPointer(0))
HeaderTypes=genTypes(set(),'',getBTHeaderRec(emptyString))

nodeTypes={'Catalog':{'LeafRecList':CatalogLeafTypes,'BTHeaderRec':HeaderTypes,'PointerRecList':CatalogIndexTypes}}
nodeTypes['Extents']={'LeafRecList':ExtentsLeafTypes,'BTHeaderRec':HeaderTypes,'PointerRecList':ExtentsIndexTypes}
nodeTypes['Attributes']={'LeafRecList':AttrLeafTypes,'BTHeaderRec':HeaderTypes,'PointerRecList':AttrIndexTypes}
volumeHeaderTypes=genTypes(set(),'',getVolumeHeader(2*emptyString))


def volumeInfo(path,vh):

    if vh!=0:
        f = open("{0}/VolumeInfo.txt".format(path),'w')
        for i in vh._asdict():
            f.write('{0} : {1}\n'.format(i,vh.__getattribute__(i)))
    
        f.close()

def outputKeyedRec(f,records,nodeType):

    for i in range(len(records)):
        for j in getRow1(records[i],nodeType):
            if type(j)==str or type(j)==unicode:
                j=j.replace('"','"""')
            if type(j)==tuple:
                j='"'+unicode(j).replace('"','"""')+'"'
            f.write(unicode(j).encode('utf-8')+',')

        f.write('\n')


def rawCSV(path,jParseList):

    f={'VolumeHeader':open('{0}/VolumeHeader.csv'.format(path),'w')}

    for i in volumeHeaderTypes:
        f['VolumeHeader'].write('{0},'.format(i))

    for i in ['Catalog','Extents','Attributes']:

        f[i]={}

        for j in ['LeafRecList','PointerRecList','BTHeaderRec']:

            f[i][j]=open('{0}/Journal_{1}{2}.csv'.format(path,i,j),'w')

            for k in nodeTypes[i][j]:
                f[i][j].write('{0},'.format(k))

            f[i][j].write('\n')


    for i in range(1,len(jParseList)):        

        blocks=jParseList[i][2]

        for j in range(len(blocks)):

            block=blocks[j]

            try:
                records=block[1]

                if type(records)==list:

                    fileType=records[0].getType()
                    recType=block._fields[1]

                    nt=nodeTypes[fileType][recType]

                    outputKeyedRec(f[fileType][recType],records,nt)

                elif block.__class__.__name__=='VolumeHeader':

                    for k in getRow2(block,volumeHeaderTypes):
                        if type(k)==str or type(k)==unicode:
                            k=k.replace('"','"""')
                        if type(k)==tuple:
                            k='"'+unicode(k).replace('"','"""')+'"'
                        f['VolumeHeader'].write(unicode(k).encode('utf-8')+',')

                    f['VolumeHeader'].write('\n')

            except Exception,e:
                print e
                pass

    f['VolumeHeader'].close()

    for i in ['Catalog','Extents','Attributes']:
        for j in ['LeafRecList','BTHeaderRec','PointerRecList']:
            f[i][j].close()


def rawSQLite3(path,jParseList):

    con=sqlite3.connect('{0}/Journal.db'.format(path))
    con.isolation_level=None
    cur=con.cursor()

    cur.execute('CREATE TABLE VolumeHeader {0}'.format(tuple(volumeHeaderTypes)))

    for i in ['Catalog','Extents','Attributes']:
        for j in ['LeafRecList','PointerRecList','BTHeaderRec']:
            cur.execute('CREATE TABLE {0}{1} {2}'.format(i,j,tuple(nodeTypes[i][j])))

    for i in range(1,len(jParseList)):

        blocks=jParseList[i][2]
        for j in range(len(blocks)):
            
            block=blocks[j]

            try:

                records=block[1]

                if type(records)==list:

                    fileType=records[0].getType()
                    recType=block._fields[1]

                    nt=nodeTypes[fileType][recType]

                    for k in range(len(records)):

                        lf=getRow1(records[k],nt)

                        for i in range(len(lf)):
                            if type(lf[i])==tuple:
                                lf[i]=unicode(lf[i])
                            if type(lf[i])==str or type(lf[i])==unicode:
                                lf[i]=lf[i].replace("'","''").replace('&','&&')

                        cur.execute(u'insert into {0}{1} values {2}'.format(fileType,recType,tuple(lf)).replace("u'","'").replace('u"','"') .replace('"',"'"))

                elif block.__class__.__name__=='VolumeHeader':

                    vh=getRow2(block,volumeHeaderTypes)

                    for i in range(len(vh)):
                        if type(vh[i])==tuple:
                            vh[i]=unicode(vh[i])
                        if type(vh[i])==str or type(vh[i])==unicode:
                            vh[i]=vh[i].replace("'","''").replace('&','&&')

                    cur.execute(u'insert into VolumeHeader values {0}'.format(tuple(vh)).replace("u'","'").replace('u"','"') .replace('"',"'"))

            except Exception,e:
                print e
                pass

    cur.close()
    con.close()


