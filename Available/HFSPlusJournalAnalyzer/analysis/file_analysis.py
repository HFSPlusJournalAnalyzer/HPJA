from lib.etc_util import *
from struct import *
from analysis.hfs_parse import *
from analysis.journal_track import *
from lib.format import *
from types import MethodType
from collections import *
from output.output_generic import *
import types
import collect_tools
import sys
import datetime
import csv
from recovery import *

fstruct={}

def volumeInfo(path,vh):

    if vh!=0:
        f = open("{0}/VolumeInfo.txt".format(path),'w')
        for i in vh._asdict():
            f.write('{0} : {1}\n'.format(i,vh.__getattribute__(i)))
    
        f.close()


def specialFileAnalyzer(path,specialFile):

    fileTypes=['Extents','Catalog','Attributes']
    recTypes=["LeafRecList", "PointerRecList", "BTHeaderRec"]

    f={}

    sf=specialFile['Catalog']

    if sf!=0:
        nodeSize,temp1,totalNodes=unpack_from('>HHL',sf,32)
        nodePointer=0
        for i in xrange(totalNodes):
            node=getBlock(buffer(sf,nodePointer,nodeSize),'Catalog')
            if node.NodeDescriptor.kind==-1:
                for j in node.LeafRecList:
                    if j.record.recordType>2:
                        fstruct[j.key.parentID]=[j.record.nodeName.nodeUnicode,j.record.parentID]

            nodePointer+=nodeSize


    for i in fileTypes:

        sf=specialFile[i]

        if sf==0:
            break

        fp=f[i]={}

        for j in recTypes:

            f[i][j]=open('{0}/{1}{2}.csv'.format(path,i,j),'w')

            for k in nodeTypes[i][j]:
                f[i][j].write('{0},'.format(k))

            f[i][j].write('\n')

        nodeSize,temp1,totalNodes=unpack_from('>HHL',sf,32)

        nodePointer=0
        for j in xrange(totalNodes):

            node=getBlock(buffer(sf,nodePointer,nodeSize),i)

            if node.NodeDescriptor.kind<2:

                index=recTypes[node.NodeDescriptor.kind+1]
                records=node[1]

                if type(records)==list:
                    outputKeyedRec(fp[index],records,nodeTypes[i][index])

                else:

                    for k in getRow2(records,nodeTypes[i][index]):
                        fp[index].write(unicode(k).replace('"','""').replace(',','","').replace('"','"""').replace('\n','"\n"').encode('utf-8')+',')

                    fp[index].write('\n')

            nodePointer+=nodeSize


def getFullPath(CNID):

    fullPath=[]
    i=CNID
    while i!=1:
        if i not in fstruct.keys():
            fullPath=['unknown']
            break
        fullPath.insert(0,u'{0}/'.format(fstruct[CNID][0]))
        i=fstruct[CNID][1]
    fullPath=u''.join(fullPath)
    return fullPath



