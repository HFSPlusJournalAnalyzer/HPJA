from collections import namedtuple


JournalHeader = namedtuple("JournalHeader", ['magic','endian','start','end','size','blhdr_size','checksum','jhdr_size'])
# endian contains '>' or '<' (instead of 0x12345678; the original value) 

BlockListHeader = namedtuple("BlockListoHeader", ['max_blocks','num_blocks','bytes_used','checksum','pad','binfo0'])
BlockInfo = namedtuple("BlockInfo", ['bnum', 'bsize', 'next'])
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

ExtentDescriptor = namedtuple("ExtentDescriptor", ['startBlock','blockCount'])
ForkData = namedtuple("ForkData", ['logicalSize','clumpSize','totalBlocks','extents'])
sBTKeyedRec = namedtuple("BTKeyedRec", ['keyLength','key'])

class BTKeyedRec(sBTKeyedRec):
    def __len__(self):
        return 2 + len(self.key)

BSDInfo = namedtuple("BSDInfo", ['ownerID', 'groupID', 'adminFlags', 'ownerFlags', 'fileMode', 'special'])

'''
Finder
'''
Point = namedtuple('Point', ["v", "h"])
Rect = namedtuple('Rect', ['top', 'left', 'bottom', 'right'])
FileInfo = namedtuple('FileInfo', ['fileType', 'fileCreator', 'finderFlags', 'location', 'reservedField'])
ExtendedFileInfo = namedtuple("ExtendedFileInfo", ['reserved1', 'extendedFinderFlags', 'reserved2', 'putAwayFolderID'])
FolderInfo = namedtuple('FolderInfo', ['windowBounds', 'finderFlags', 'location', 'reservedField'])
ExtendedFolderInfo = namedtuple("ExtendedFolderInfo", ['scrollPosition', 'reserved1', 'extendedFinderFlags', 'reserved2', 'putAwayFolderID'])

'''
Catalog Records 
'''
CatalogLeafRec = namedtuple("CatalogLeafRec", ['key', 'record'])

sCatalogKey = namedtuple("CatalogKey", ["parentID", "nodeName"])

class CatalogKey(sCatalogKey):
    def __len__(self):
        return 4+2+2*self.nodeName[0]

CatalogFolder = namedtuple('CatalogFolder', ['recordType', 'flags', 
                                             'valence', 'folderID', 
                                             'createDate', 'contentModDate', 'attributeModDate', 'accessDate', 'backupDate', 
                                             'permissions','userInfo','finderInfo',
                                             'textEncoding', 'reserved'])

CatalogFile = namedtuple('CatalogFolder', ['recordType', 'flags', 
                                             'reserved1', 'fileID', 
                                             'createDate', 'contentModDate', 'attributeModDate', 'accessDate', 'backupDate', 
                                             'permissions','userInfo','finderInfo',
                                             'textEncoding', 'reserved2',
                                             'dataFork', 'resourceFork'])

CatalogThread = namedtuple("CatalogThread", ['recordType', 'reserved', 'parentID', 'nodeName'])

