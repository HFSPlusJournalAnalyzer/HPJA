'''
Created on 2015. 2. 8.

@author: biscuit
'''
from HFSPlus_ParseModule import *
    

class JournalChange:
    changeType = None
    parAtt = ''
    curAtt = ''
    changeInfo = None
    
    def __init__(self, changeType, parAtt='', curAtt='', changeInfo=None):
        typeList = ["Insert", "Remove", "Modify", "Renewal"]
        infoDict = {'Insert':objectChangeInfo, 'Remove':objectChangeInfo,
                    'Modify':valueChangeInfo, 'Renewal':renewalChangeInfo}
        self.changeType = changeType
        self.parAtt = parAtt
        self.curAtt = curAtt
        self.changeInfo = changeInfo
        assert changeType in typeList
        assert changeInfo.__class__ == infoDict[changeType]
        
    def __str__(self):
        return self.changeType+ " " + self.parAtt + " " + self.curAtt + " " + str(self.changeInfo)
    
class valueChangeInfo:
    before = 0
    after = 0
    diff = 0
    def __init__(self, before, after):
        self.before = before
        self.after = after
        self.diff = self.after - self.before
        
    def __str__(self):
        return "%d -> %d" % (self.before, self.after)
        
class renewalChangeInfo:
    before = 0
    after = 0
    renewal = False
    def __init__(self, before, after):
        self.before = before
        self.after = after
        if before != after:
            self.renewal = True
    
    def __str__(self):
        return "renewal"

class objectChangeInfo:
    object = None
    absData = None
    def __init__(self, object, absData):
        self.object = object
        self.absData = absData
        
    def __str__(self):
        return absData

def journalTrack(j_parseList):
    transList = j_parseList[1:]
    changeLog = []
    cursur = {}
    for trans in transList:
        ch_bukket = transTrack(trans, cursur)
        changeLog.append(ch_bukket)
        
    return changeLog

def transTrack(trans, cursur):
    blockListHeader, bi_List, data_List = trans
    changes = []
    for i in range(blockListHeader.num_blocks-1):
        changes.extend(block_check(bi_List[i], data_List[i], cursur))
    return changes

def block_check(b_info, data, cursur):
    try:
        p_data = cursur[b_info.bnum]
    except KeyError:
        cursur[b_info.bnum] = data
        d_chInfo = objectChangeInfo(data, data.__class__.__name__)
        j_ch = JournalChange("Insert", '', hex(b_info.bnum), d_chInfo)
        return [j_ch]
    classType = data.__class__.__name__
    cursur[b_info.bnum] = data
    return data_diff(p_data, data, '', classType)
    
def data_diff(original, changed, parType='', curType=''):
    assert original.__class__ == changed.__class__
    dType = original.__class__
    result = []
    
    if dType in [int, long]:
        if original == changed: return []
        if "Date" in curType:
            r_chInfo = renewalChangeInfo(original, changed)
            j_ch = JournalChange("Renewal", parType, curType, r_chInfo)
        else:
            v_chInfo = valueChangeInfo(original, changed)
            j_ch = JournalChange("Modify", parType, curType, v_chInfo)
        result.append(j_ch)
        return result
    
    if dType in [tuple, list]:
        if curType == 'LeafRecList':
            result.extend(compCatalog(original, changed, parType, curType))
            return result
        count = 0
        for i, j in zip(original, changed):
            result.extend(data_diff(i, j, curType, curType + "_%d" % count))
            count += 1
        return result
    
    if dType == memoryview:
        if original == changed: return []
        r_chInfo = renewalChangeInfo(original, changed)
        j_ch = JournalChange("Renewal", parType, curType, r_chInfo)
        result.append(j_ch)
        return result
    
    if dType in [unicode, str]:
        return []
    
    attList = original._fields
    for att in attList:
        result.extend(data_diff(getattr(original,att), getattr(changed, att), parType+"\\"+curType, att))
    return result
    
    
def compCatalog(original, changed, parType, curType):
    orgSet = set(original)
    chgSet = set(changed)
    insList = chgSet - orgSet
    modList = orgSet & chgSet
    remList = orgSet - chgSet
    result = []
            
    for i in insList:
        chInfo = objectChangeInfo(i, None)
        j_ch = JournalChange("Insert", parType, curType, chInfo)
        result.append(j_ch)
    
    for r in remList:
        chInfo = objectChangeInfo(r, None)
        j_ch = JournalChange("Remove", parType, curType, chInfo)
        result.append(j_ch)
        
    for m in modList:
        m_org = [x for x in original if m == x][0]
        m_chg = [x for x in changed if m == x][0]
        result.extend(data_diff(m_org, m_chg, parType, curType))
    
    return result

def main():
    f = open(r"C:\Users\user\Desktop\Untitled2", 'rb')
    s = f.read()
    jParseList = journalParser(s)
    jT = journalTrack(jParseList)
    g = open(r"C:\result2.txt", 'w')
    for i in jT:
        g.write("-----------\n")
        for j in i:
            g.write(str(j)+"\n")
    
    g.close()
    f.close()

        
if __name__ == '__main__':
    main()