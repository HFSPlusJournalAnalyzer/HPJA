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
appeared={}


def makefstruct(catalogFile):
    
    nodeSize,temp1,totalNodes=unpack_from('>HHL',catalogFile,32)
    nodePointer=0
    for i in xrange(totalNodes):
        node=getBlock(buffer(catalogFile,nodePointer,nodeSize),'Catalog')
        if node.NodeDescriptor.kind==-1:
            for j in node.LeafRecList:
                if j.record.recordType>2:
                    fstruct[j.key.parentID]=[j.record.nodeName.nodeUnicode,j.record.parentID]
        nodePointer+=nodeSize


def getFullPath(CNID):

    try:
        return appeared['CNID']
    except KeyError:
        fullPath=[]
        i=CNID
        while i!=1:
            try:
                fullPath.insert(0,u'/{0}'.format(fstruct[i][0]))
                i=fstruct[i][1]
            except KeyError:
                fullPath=['unknown']
                break
        fullPath=u''.join(fullPath)
        appeared['CNID']=fullPath
        return fullPath



