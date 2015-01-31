from struct import *

existentExtent=[0]
nameAndParent=[{},{}]

class DataStructure:

    def __str__(self):

        temp=[]
        for i in self.__slots__:
            temp.append('{0},'.format(getattr(self,i)))

        return u''.join(temp).replace(',','","').replace('[','').replace(']','')


class TranBlock(DataStructure):

    __slots__=['journalOffset','tranNum','blockNum','blockType','offset','size','content']

    def __init__(self,journalOffset,tranNum,blockNum,bnum,bsize,sectorSize,content):

        self.journalOffset=journalOffset
        self.tranNum=tranNum
        self.blockNum=blockNum
        self.offset=bnum*sectorSize
        self.size=bsize
        self.content=content
        self.blockType=[]

    def __str__(self):

        areaType=['Al','E','C','At','V']
        nodeType=['L','I','H','M']

        temp=[]

        for i in self.__slots__[:3]:
            temp.append('{0},'.format(getattr(self,i)))

        if self.blockType<4:
            temp.append('{0}{1},'.format(areaType[self.blockType[0]],nodeType[self.blockType[1]]))

        else:
            temp.append('{0},'.format(areaType[self.blockType[0]]))

        temp.append('{0},{1},'.format(self.offset,self.content))

        return u''.join(temp)


class ExtentDescriptor(DataStructure):

    __slots__=['startBlock','blockCount','state']

    def __init__(self,binary):

        self.startBlock,self.blockCount=unpack('>LL')

    def __str__(self):

        if self.startBlock!=0 or self.blockCount!=0:
            return u'({0}","{1}) '.format(self.startBlock,self.blockCount)


class Fork(DataStructure):

    __slots__=['logicalSize','clumpSize','totalBlocks','extents']

    def __init__(self,binary):

        self.logicalSize,self.clumpSize,self.totalBlocks=unpack('>QLL',binary)

        extents=[]
        for i in range(2,10):
            self.extents.append(ExtentDescriptor(binary[8*i:8*(i+1)]))


class BTreeNode(DataStructure):

    __slots__=['fLink','bLink','kind','height','numRecords','reserved','records']

    def __init__(self,binary):

        self.fLink,self.bLink,self.kind,self.height,self.numRecords,reserved=unpack('>LLbBHH',binary)
        self.records=[]

    def __str__(self):
        return '{0},'.format(self.numRecords)


class BTHeaderRec(DataStructure):

    __slots__=['treeDepth','rootNode','leafRecords','firstLeafNode','lastLeafNode','nodeSize','maxKeyLength','totalNodes','freeNodes','reserved1','clumpSize','btreeType','keyCompareType','attributes','reserved3']

    def __init__(self,binary):

        self.treeDepth,self.rootNode,self.leafRecords,self.firstLeafNode,self.lastLeafNode,self.nodeSize,self.maxKeyLength,self.totalNodes,self.freeNodes,self.reserved1,self.clumpSize,self.btreeType,self.keyCompareType,self.attributes=unpack('>HLLLLHHLLHLBBL',binary)
        
        reserved3=[]
        for i in range(16):
            self.reserved3.append(unpack_from('>L',binary,i*4+42))


class BTHeaderNode(BTreeNode):

    def __init__(self,binary,size):

        BTreeNode.__init__(self,binary)
        self.records.append(BTHeaderRec(binary[unpack_from('>H',binary,size-2):unpack_from('>H',binary,size-4)]))
        self.records.append(Bitmap([binary[unpack_from('>H',binary,size-6):unpack_from('>H',binary,size-8)]]))


class BTKeyedRec(DataStructure):

    __slots__=['keyLength','key']

    def __init__(self,binary):

        self.keyLength=unpack('>H',binary)
        self.key=binary[2:self.keyLength+2]


class BTPointerRec(BTKeyedRec):

    __slots__=['nodeNumber']

    def __init__(self,binary):

        BTKeyedRec.__init__(self,binary)
        self.nodeNumber=unpack_from('>L',binary,self.keyLength+2)


class BTIndexNode(BTreeNode):

    def __init__(self,binary,size):

        BTreeNode.__init__(self,binary)

        for i in range(self.numRecords):

            start=unpack_from('>H',binary,size-2*i)
            end=unpack_from('>H',binary,size-2*(i+1))
            
            self.records.append(BTPointerRec(binary[start:end]))


class CatalogDataRec(BTKeyedRec):

    __slots__=['nodeNameLen','recordType','CNID','nodeName','parentID','fullPath','unidentifiedAncestor']

    def __init__(self,binary):

        BTKeyedRec.__init__(self,binary)
        self.recordType=unpack_from('>h',binary,self.keyLength+2)


class CatalogNonThreadRec(CatalogDataRec):

    __slots__=['flags','createDate','contentModDate','attributeModDate','accessDate','backupDate','ownerID','groupID','adminFlags','ownerFlags','fileMode','special','userInfo','finderInfo','textEncoding']

    def __init__(self,binary):

        CatalogDataRec.__init__(self,binary)
        self.parentID,self.nodeNameLen=unpack('>LH',self.key)

        nodeName=[]
        for i in range(self.nodeNameLen):
            nodeName.append('\u{0}{1}'.format(self.key[2*i+6].encode('hex'),self.key[2*i+7].encode('hex')).decode('unicode-escape'))
        self.nodeName=u''.join(nodeName)
        self.nodeName=nodeName.replace('/',':')

        self.flags,temp1,self.CNID,self.createDate,self.contentModDate,self.attributeModDate,self.accessDate,self.backupDate,self.ownerID,self.groupID,self.adminFlags,self.ownerFlags,self.fileMode,self.special=unpack_from('>HLLLLLLLLLBBHL',binary,self.keyLength+4)
        self.userInfo=unpackLarge_from('>16',binary,self.keyLength+50)
        self.finderInfo=unpackLarge_from('>16',binary,self.keyLength+66)
        self.textEncoding=unpack_from('>L',binary,self.keyLength+82)


class CatalogFolderRec(CatalogNonThreadRec):

    __slots__=['valence','folderCount']

    def __init__(self,binary):

        CatalogNonThreadRec.__init__(self,binary)
        self.valence=unpack_from('>L',binary,self.keyLength+6)
        self.folderCount=unpack_from('>L',binary,self.keyLength+86)


class CatalogFileRec(CatalogNonThreadRec):

    __slots__=['reserved1','reserved2','dataFork','resourceFork']

    def __init__(self,binary):

        CatalogNonThreadRec.__init__(self,binary)
        self.reserved1=unpack_from('>L',binary,self.keyLength+6)
        self.reserved2=unpack_from('>L',binary,self.keyLength+86)
        self.dataFork=Fork(binary[self.keyLength+90:self.keyLength+170])
        self.resourceFork=Fork(binary[self.keyLength+170:self.keyLength+250])


class CatalogThreadRec(CatalogDataRec):

    __slots__=['reserved']

    def __init__(self,binary):

        CatalogDataRec.__init__(self,binary)
        self.CNID=unpack('>L',self.key)
        self.reserved,slef.parentID,self.nodeNameLen=unpack_from('>hhLH',binary,self.keyLength+4)

        nodeName=[]
        for i in range(self.nodeNameLen):
            nodeName.append('\u{0}{1}'.format(binary[self.keyLength+2*i+12].encode('hex'),binary[self.keyLength+2*i+13].encode('hex')).decode('unicode-escape'))
        self.nodeName=u''.join(nodeName)
        self.nodeName=self.nodeName.replace('/',':')


class CatalogLeafNode(BTreeNode):

    def __init__(self,binary,size):

        CatalogDataRecords=[CatalogFolderRec,CatalogFileRec,CatalogThreadRec,CatalogThreadRec]
        
        BTreeNode.__init__(self,binary)

        for i in range(self.numRecords):

            start=unpack_from('>H',binary,size-2*i)
            end=unpack_from('>H',binary,size-2*(i+1))
            
            self.records.append(CatalogDataRecords[unpack_from('>h',binary,start+unpack_from('>H',binary,start)+2)-1](binary[start:end]))


class ExtentsDataRec(BTKeyedRec):

    __slots__=['extents']

    def __init__(self,binary):

        self.forkType,self.pad,self.fileID,self.startBlock=unpack('>HBBLL',self.key)

        self.extents=[]
        for i in range(8):
            self.extents.append(ExtentDescriptor(binary[self.keyLength+8*i+2:self.keyLength+8*i+10]))


class ExtentsLeafNode(BTreeNode):

    def __init__(self,binary,size):

        BtreeNode.__init__(self,binary)

        for i in range(self.numRecords):

            start=unpack_from('>H',binary,size-2*i)
            end=unpack_from('>H',binary,size-2*(i+1))

            self.records.append(ExtentsDataRecord(binary[start:end]))


class AttrDataRec(BTKeyedRec):

    __slots__=['pad','fileID','startBlock','attrNameLen','attrName','recordType','reserved']

    def __init__(self,binary):

        BTKeyedRec.__init__(self,binary)
        self.pad,self.fileID,self.startBlock,self.attrNameLen=unpack('>HLLH',self.key)

        attrName=[]
        for i in range(self.attrNameLen):
            nodeName.append('\u{0}{1}'.format(binary[2*i+14].encode('hex'),binary[2*i+15].encode('hex')).decode('unicode-escape'))
        self.attrName=u''.join(attrName)

        self.recordType,self.reserved=unpack_from('>LL',binary,self.keyLength+2)


class AttrForkData(AttrDataRec):

    __slots__=['theFork']

    def __init__(self,binary):

        AttrDataRec.__init__(self,binary)
        self.theFork=Fork(binary[self.keyLength+10:self.keyLength+90])


class AttrExtents(AttrDataRec):

    __slots__=['extents']

    def __init__(self,binary):

        AttrDataRec.__init__(self,binary)

        self.extents=[]
        for i in range(8):
            self.extents.append(ExtentDescriptor(binary[self.keyLength+8*i+10:self.keyLength+8*i+18]))


class AttrData(AttrDataRec):

    __slots__=['reserved2','attrSize','attrData']

    def __init__(self,binary):

        AttrDataRec.__init__(self,binary)
        self.reserved2,self.attrSize,self.attrData=unpack_from('>LLL',self.keyLength+10)


class AttrLeafNode(BTreeNode):

    def __init__(self,binary,size):

        AttrDataRecords=[AttrData,AttrForkData,AttrExtents]

        BtreeNode.__init__(self,binary)

        for i in range(self.numRecords):

            start=unpack_from('>H',binary,size-2*i)
            end=unpack_from('>H',binary,size-2*(i+1))

            self.records.append(AttrDataRecords[(unpack_from('>L',binary,start+unpack_from('>H',binary,start)+2)/16)-1](binary[start:end]))


class VolumeHeader(DataStructure):

    __slots__=['signature','version','attributes','lastMountedVersion','journalInfoBlock','createDate','modifyDate','backupDate','checkedDate','fileCount','folderCount','blockSize','totalBlocks','freeBlocks','nextAllocation','rsrcClumpSize','dataClumpSize','nextCatalogID','writeCount','encodingsBitmap','finderInfo','specialFileFork']

    def __init__(self,binary,size):

        self.signature,self.version,self.attributes,self.lastMountedVersion,self.journalInfoBlock,self.createDate,self.modifyDate,self.backupDate,self.checkedDate,self.fileCount,self.folderCount,self.blockSize,self.totalBlocks,self.freeBlocks,self.nextAllocation,self.rsrcClumpSize,self.dataClumpSize,self.nextCatalogID,self.writeCount,self.encodingsBitmap=unpack('>HHLLLLLLLLLLLLLLLLLQ',block)

        self.finderInfo=[]
        for i in range(32):
            self.finderInfo.append(unpack_from('>B',binary,80+i))

        self.specialFileFork=[]
        for i in range(5):
            self.specialFileFork.append(Fork(binary[112:112+24*i]))


class BTMapNode(BTreeNode):

    __slots__=['content']

    def __init__(self,binary,size):

        BTreeNode.__init__(binary)
        self.content=binary[14:size]

    def __str__(self):

        return self.content



