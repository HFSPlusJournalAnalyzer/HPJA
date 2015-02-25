'''
Created on 2015. 2. 8.

@author: biscuit
'''
from analysis.hfs_parse import *
    
'''
Classes
'''

class newObjectInfo:
    def __init__(self, object, bNum, name):
        self.object = object
        self.bNum = bNum
        self.__name__ = name
    
    def __str__(self):
        return "[NEW] %s %s\n" %(hex(self.bNum), self.__name__)
    
    def getStr(self, tabCount):
        return " "*tabCount + "[NEW] %s %s\n" %(hex(self.bNum), self.__name__)
    
class dataChangeHead:
    def __init__(self, bNum, type, chList):
        self.bnum, self.type = bNum, type
        self.chList = chList
        
    def __str__(self):
        str_ch = "@%s %s-----------------------------\n" %(hex(self.bnum), self.type)
        for i in self.chList:
            str_ch += "%s" %str(i)
        return str_ch
        
class dataChange:
    def __init__(self, nData, chList, parent):
        self.nData, self.chList, self.parent = nData, chList, parent
    
    def __str__(self):
        return self.getStr(1)
        
    def getStr(self, tabCount):
        str_ch = " "*tabCount + "%s\n" %str(self.nData)
        for i in self.chList:
            str_ch += "%s" %i.getStr(tabCount+1)
        return str_ch
    
class valueChangeInfo:
    def __init__(self, attName, before, after):
        self.__name__ = attName
        self.before = before
        self.after = after
        self.diff = self.after - self.before
    
    def __str__(self):
        return "[Modify] %s\t%d -> %d\n" % (self.__name__, self.before, self.after)
        
    def getStr(self, tabCount):
        return " "*tabCount + "[Modify] %s\t%d -> %d\n" % (self.__name__, self.before, self.after)
        
class renewalChangeInfo:
    renewal = False
    def __init__(self, attName, before, after):
        self.__name__ = attName
        self.before = before
        self.after = after
        if before != after:
            self.renewal = True
    
    def __str__(self):
        if "Date" in self.__name__:
            return "[Renewal] %s\t%s -> %s\n" %(self.__name__ , getHFSTime(self.before), getHFSTime(self.after)) 
        return "[Renewal] %s\n" %self.__name__
    
    def getStr(self, tabCount):
        if "Date" in self.__name__:
            return " "*tabCount + "[Renewal] %s\t%s -> %s\n" %(self.__name__ , getHFSTime(self.before), getHFSTime(self.after)) 
        return " "*tabCount + "[Renewal] %s\n" %self.__name__

class objectChangeInfo:
    def __init__(self, chType, object, absData=None):
        assert chType in ['Insert', 'Remove']
        self.chType = chType
        self.object = object
        self.absData = absData
        
    def __str__(self):
        if self.absData == None:
            return "[%s] %s\n" %(self.chType, self.object.__class__.__name__)
        return "[%s] %s\n" %(self.chType, str(self.absData)) 
    
    def getStr(self, tabCount):
        if self.absData == None:
            return " "*tabCount + "[%s] %s\n" %(self.chType, self.object.__class__.__name__)
        return " "*tabCount + "[%s] %s\n" %(self.chType, str(self.absData))
    
'''
Main Tracking function
'''
cursur = {}

def journalTrack(j_parseList, pInfo):
    transList = j_parseList[1:]
    changeLog = []
    
    for trans in transList:
        ch_bucket = transTrack(trans, pInfo)
        changeLog.append(ch_bucket)
            
    return changeLog

'''
auxiliary functions
'''
def transTrack(trans, pInfo):
    blockListHeader, bi_List, data_List = trans
    changes = []
    for i in range(len(data_List)):
        temp = block_check(bi_List[i], data_List[i], pInfo)
        if temp != None: changes.append(temp)
    return changes

def block_check(b_info, data, pInfo):
    global cursur
    data_sNum = b_info.bnum / pInfo.blockMag
    curSType = detBlockType(data_sNum, pInfo.sfLoc)
    if curSType == "":
        curSType = "VolumeHeader"
    try:
        p_data = cursur[b_info.bnum]
    except KeyError:
        cursur[b_info.bnum] = data
        
        d_chInfo = newObjectInfo(data, b_info.bnum, curSType)
        return d_chInfo
    
    cursur[b_info.bnum] = data
    
    if (data.__class__ == Binary) and (p_data != data):
        return renewalChangeInfo(data.__name__, p_data, data)
    
    try:
        assert p_data.__class__.__name__ == data.__class__.__name__
    except(AssertionError): 
        return newObjectInfo(data, b_info.bnum, data.__class__.__name__ )
    
    attList = data._fields
    curCh = []
    chHead = dataChangeHead(b_info.bnum, curSType, curCh)
    for att in attList:
        temp = getDataDiff(getattr(p_data, att), getattr(data, att), att, chHead)
        if temp != None: curCh.append(temp)
    if len(curCh) == 0: return None
    return chHead

def getDataDiff(orgBlock, chgBlock, attName, parent):
    bType= orgBlock.__class__
    result = []
    
    if bType in [str, unicode]: return None
    
    if bType in [int, long]:
        if orgBlock == chgBlock: return None 
        if "Date" in attName:
            chInfo = renewalChangeInfo(attName, orgBlock, chgBlock)
        else:
            chInfo = valueChangeInfo(attName, orgBlock, chgBlock)
        return chInfo
    
    if bType == Binary:
        if orgBlock == chgBlock: return None
        chInfo = renewalChangeInfo(chgBlock.__name__, orgBlock, chgBlock)
        return chInfo
    
    if bType == tuple:
        count = 0
        cList = []
        for i, j in zip(orgBlock, chgBlock):
            temp = getDataDiff(i, j, attName+"_%d" %count, parent)
            if temp != None:
                cList.append(temp)
            count += 1
        if len(cList) == 0:
            return None
        return dataChange(attName, cList, parent)
    
    if bType == list:
        temp = compCatalog(orgBlock, chgBlock, parent)
        if len(temp) == 0:
            return None
        return dataChange(attName, temp, parent)
    
    attList = orgBlock._fields
    for att in attList:
        next = att
        try:
            if getattr(getattr(orgBlock,att), 'getAbs'):
                next = getattr(orgBlock,att).getAbs()
        except(AttributeError):
            pass
        temp = getDataDiff(getattr(orgBlock,att), getattr(chgBlock, att), next, parent)
        if temp != None: result.append(temp)
    if len(result) == 0: return None
    return dataChange(attName, result, parent)

def compCatalog(original, changed, parent):
    orgSet = set(original)
    chgSet = set(changed)
    insList = chgSet - orgSet
    modList = orgSet & chgSet
    remList = orgSet - chgSet
    result = []
            
    for i in insList:
        chInfo = objectChangeInfo("Insert", i, i.getAbs())
        result.append(chInfo)
    
    for r in remList:
        chInfo = objectChangeInfo("Remove", r, r.getAbs())
        result.append(chInfo)
        
    for m in modList:
        m_org = [x for x in original if m == x][0]
        m_chg = [x for x in changed if m == x][0]
        temp = getDataDiff(m_org, m_chg, m_chg.getAbs(), parent)
        if temp != None:
            result.append(temp)
            
    return result

def journalTrackPrint(journalTrack, outputPath):
    with open(outputPath, 'w') as fd:
        count = 1
        for i in journalTrack:
            fd.write("trans_%d=================================\n" %count)
            for j in i:
                fd.write(str(j).encode('utf8'))
            count += 1
    
'''
main
'''

def main():
    f = open(r"C:\Users\user\Desktop\Journal_2", 'rb')
    s = f.read()
    jPList, pInfo = journalParser(s)[:2]
    jT = journalTrack(jPList, pInfo)
    journalTrackPrint(jT, r"C:\TEMP\result_2.txt")
    
    f.close()
    
if __name__ == '__main__':
    main()
    