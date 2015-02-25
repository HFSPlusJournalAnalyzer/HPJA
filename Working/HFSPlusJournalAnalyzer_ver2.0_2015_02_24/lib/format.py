from collections import namedtuple

JournalHeader = namedtuple("JournalHeader", ['magic','endian','start','end','size','blhdr_size','checksum','jhdr_size', 'sequence_num'])
# endian contains '>' or '<' (instead of 0x12345678; the original value) 

BlockListHeader = namedtuple("BlockListHeader", ['max_blocks','num_blocks','bytes_used','checksum','flags','binfo0'])
BlockInfo = namedtuple("BlockInfo", ['bnum', 'bsize', 'cksum'])
NodeDescriptor = namedtuple("NodeDescriptor", ['fLink','bLink','kind','height','numRecords','reserved'])
BTHeaderRec = namedtuple("BTHeaderRec", ['treeDepth','rootNode',
                                        'leafRecords','firstLeafNode','lastLeafNode','nodeSize',
                                        'maxKeyLength','totalNodes','freeNodes','reserved1',
                                        'clumpSize','btreeType',
                                        'keyCompareType','attributes'])
VolumeHeader = namedtuple("VolumeHeader", ['signature','version','attributes','lastMountedVersion','journalInfoBlock',
                                          'createDate','modifyDate','backupDate','checkedDate',
                                          'fileCount','folderCount',
                                          'blockSize','totalBlocks','freeBlocks','nextAllocation',
                                          'rsrcClumpSize','dataClumpSize',
                                          'nextCatalogID','writeCount',
                                          'encodingsBitmap','finderInfo',
                                          'allocationFile', 'extentsFile', 'catalogFile', 'attributesFile', 'startupFile'])



'''
 Leaf Records  
'''

class ExtentDescriptor(namedtuple("ExtentDescriptor", ['startBlock','blockCount'])):
    __slots__ = ()
    def isIn(self, bnum):
        return 0 <= bnum - self.startBlock <= self.blockCount - 1
    
ForkData = namedtuple("ForkData", ['logicalSize','clumpSize','totalBlocks','extents'])

class BTPointer(namedtuple("BTPointer", ['nodeNumber'])):
    __slots__ = ()
    def __len__(self):
        return 4
    
    def getAbsT(self):
        return {"nodeNumber":self.nodeNumber}
    

BSDInfo = namedtuple("BSDInfo", ['ownerID', 'groupID', 'adminFlags', 'ownerFlags', 'fileMode', 'special'])

class BTRecord(namedtuple("BTRecord", ['key', 'record'])):
    __slots__ = ()
    def __len__(self):
        return len(self.key) + len(self.record)
    
    def __eq__(self, other):
        keyComp = ( self.key == other.key )
        recComp = ( self.record == other.record )
        return (keyComp and recComp)
    
    def getType(self):
        keyType = self.key.__class__.__name__
        tMap = {'CatalogKey': 'Catalog', 'ExtentsKey':"Extents", 'AttrKey':"Attributes"}
        return tMap[keyType]
    
    def getAbs(self):
        return dict(self.key.getAbsT().items() + self.record.getAbsT().items())
    
'''
Finder
'''
Point = namedtuple('Point', ["v", "h"])
Rect = namedtuple('Rect', ['top', 'left', 'bottom', 'right'])
FileInfo = namedtuple('FileInfo', ['fileType', 'fileCreator', 'finderFlags', 'location', 'opaque'])
ExtendedFileInfo = namedtuple("ExtendedFileInfo", ['document_id','date_added', 'extendedFinderFlags', 'reserved2', 'write_gen_counter'])
FolderInfo = namedtuple('FolderInfo', ['windowBounds', 'finderFlags', 'location', 'opaque'])
ExtendedFolderInfo = namedtuple("ExtendedFolderInfo", ['document_id', 'date_added', 'extendedFinderFlags', 'reserved3', 'write_gen_counter'])

OpaqueInfo = namedtuple("OpaqueInfo", ['opaque'])

'''
Catalog Records 
'''
class CatalogKey(namedtuple("CatalogKey", ["keyLength", "parentID", "nodeName"])):
    __slots__ = ()
    
    def __len__(self):
        return 2+self.keyLength
    
    def __eq__(self, other):
        kL_Comp = (self.keyLength == other.keyLength)
        nN_Comp = (self.nodeName == other.nodeName)
        return (kL_Comp and nN_Comp)
    
    def __hash__(self):
        return hash((self.keyLength, self.nodeName))
    
    def getAbsT(self):
        return {"nodeName":self.nodeName.nodeUnicode, 'thID': self.parentID}
     
sCatalogFolder = namedtuple('CatalogFolder', ['recordType', 'flags', 
                                             'valence', 'CNID', 
                                             'createDate', 'contentModDate', 'attributeModDate', 'accessDate', 'backupDate', 
                                             'bsdInfo', 'userInfo','finderInfo',
                                             'textEncoding', 'folderCount'])
# folderCount ; # of enclosed folders, active when HasFolderCount is set
class CatalogFolder(sCatalogFolder):
    __slots__ = ()
    def __len__(self):
        return 88
    
    def __eq__(self, other):
        return ((self.recordType == other.recordType) and (self.CNID == other.CNID))
    
    def __hash__(self):
        return hash((self.recordType, self.CNID))
    
    def getAbsT(self):
        return {"type":'folder', 'ID': self.CNID}

sCatalogFile = namedtuple('CatalogFolder', ['recordType', 'flags', 
                                             'reserved1', 'CNID', 
                                             'createDate', 'contentModDate', 'attributeModDate', 'accessDate', 'backupDate', 
                                             'permissions', 'userInfo', 'finderInfo',
                                             'textEncoding', 'reserved2',
                                             'dataFork', 'resourceFork'])

class CatalogFile(sCatalogFile):
    __slots__ = ()
    def __len__(self):
        return 248
    
    def __eq__(self, other):
        return ((self.recordType == other.recordType) and (self.CNID == other.CNID))
    
    def __hash__(self):
        return hash((self.recordType, self.CNID))
    
    def getAbsT(self):
        return {'type':'file',"ID" : self.CNID}
    
class CatalogThread(namedtuple("CatalogThread", ['recordType', 'reserved', 'parentID', 'nodeName'])):
    __slots__ = ()
    def __len__(self):
        return 8+2+2*self.nodeName.nameLen
    
    def __eq__(self, other):
        return ((self.recordType == other.recordType) and (self.nodeName == other.nodeName))
    
    def __hash__(self):
        return hash((self.recordType, self.nodeName))
    
    def getAbsT(self):
        return {'type': 'thread', "parID" : self.parentID, "nodeName" : self.nodeName.nodeUnicode}
    
'''
Extents Overflow Files
'''
class ExtentsKey(namedtuple('ExtentKey',["keyLength",'forkType','pad','fileID','startBlock'])):
    __slots__ = ()
    def __len__(self):
        return 2 + self.keyLength
    def __eq__(self, other):
        return (self.forkType == other.forkType) and (self.fileID == other.fileID)
    def __hash__(self):
        return hash((self.forkType, self.fileID))
    def getAbsT(self):
        return {"forkType":self.forkType, "fileID" : self.fileID}

class ExtentsDataRec(namedtuple('ExtentsDataRec',['extent0','extent1','extent2','extent3',
                                                  'extent4','extent5','extent6','extent7',])):
    __slots__ = ()
    def __len__(self):
        return 64
    def __eq__(self, other):
        return True
    def __hash__(self):
        return 1
    def getAbsT(self):
        return {}

'''
Attribute Files
'''

class AttrKey(namedtuple('AttrKey',["keyLength",'pad','fileID','startBlock','attrNameLen','attrName'])):
    __slots__ = ()
    def __len__(self):
        return 2+self.keyLength
    def __eq__(self, other):
        kL = (self.keyLength == other.keyLength)
        fI = (self.fileID == other.fileID)
        sB = (self.startBlock == other.startBlock)
        aN = (self.attrName == other.attrName)
        return kL and fI and sB and aN
    def __hash__(self):
        return hash((self.keyLength, self.fileID, self.startBlock, self.attrName))
    
    def getAbsT(self):
        return {"fileID": self.fileID, "attrName": self.attrName}
    
class AttrForkData(namedtuple('AttrForkData',['recordType','reserved','theFork'])):
    __slots__ = ()
    def __len__(self):
        return 88
    def __eq__(self, other):
        return (self.recordType == other.recordType)
    def __hash__(self):
        return hash(self.recordType)
    def getAbsT(self):
        return {'type': 'Fork'}

class AttrExtents(namedtuple('AttrExtents',['recordType','reserved', 'extents'])):
    __slots__ = ()
    def __len__(self):
        return 72
    def __eq__(self, other):
        return (self.recordType == other.recordType)
    def __hash__(self):
        return hash(self.recordType)
    def getAbsT(self):
        return {'type': "extents"}

class AttrData(namedtuple('AttrData',['recordType', 'reserved', 'attrSize', 'attrData'])):
    __slots__ = ()
    def __len__(self):
        return 16 + self.attrSize + self.attrSize%2
    def __eq__(self, other):
        return (self.recordType == other.recordType) and (self.attrSize == other.attrSize) and (self.attrData == other.attrData)
    def __hash__(self):
        return hash((self.recordType, self.attrSize, self.attrData.tobytes()))
    def getAbsT(self):
        return {'type' :"InlineData"}

# User data structure
    
LeafNode = namedtuple("LeafNode", ['NodeDescriptor', 'LeafRecList','recOffList'])
HeaderNode = namedtuple("HeaderNode", ['NodeDescriptor', 'BTHeaderRec', 'UserDataRec', 'MapRec'])
IndexNode = namedtuple("IndexNode", ['NodeDescriptor', 'PointerRecList','recOffList'])
MapNode = namedtuple('MapNode', ['NodeDescriptor', 'MapRecord'])
class UniChar(namedtuple("UniChar", ['nameLen', 'nodeUnicode'])):
    __slots__ = ()
    
    def __eq__(self, other):
        lenComp = (self.nameLen == other.nameLen)
        nameComp = (self.nodeUnicode == other.nodeUnicode)
        return (lenComp and nameComp)

