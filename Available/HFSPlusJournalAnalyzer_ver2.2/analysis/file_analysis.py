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

def makefstruct(catalogFile):

    global fstruct
    
    nodeSize,temp1,totalNodes=unpack_from('>HHL',catalogFile,32)
    nodePointer=0
    for i in xrange(totalNodes):
        node=getBlock(buffer(catalogFile,nodePointer,nodeSize),'Catalog')
        if node.NodeDescriptor.kind==-1:
            for j in node.LeafRecList:
                if j.record.recordType>2:
                    fstruct[j.key.parentID]=['/'+j.record.nodeName.nodeUnicode,j.record.parentID]
        nodePointer+=nodeSize


def getFullPath(CNID):

    global fstruct

    if CNID!=2:
        try:
            fullPath=getFullPath(fstruct[CNID][1])+fstruct[CNID][0]
            return fullPath
        except KeyError:
            fullPath='unknown'
            return fullPath
        fstruct[CNID]=[fullPath,2]

    else:
        return ''




