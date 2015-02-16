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
        if self.absData == None:
            return self.object.__class__.__name__
        return str(self.absData)


cursur = {}

def journalTrack(j_parseList, pInfo):
    transList = j_parseList[1:]
    changeLog = []
    
    for trans in transList:
        ch_bucket = transTrack(trans, pInfo)
        changeLog.append(ch_bucket)
        
    return changeLog

def transTrack(trans, pInfo):
    blockListHeader, bi_List, data_List = trans
    changes = []
    for i in range(len(data_List)):
        changes.extend(block_check(bi_List[i], data_List[i], pInfo))
    return changes

def block_check(b_info, data, pInfo):
    global cursur
    try:
        p_data = cursur[b_info.bnum]
    except KeyError:
        cursur[b_info.bnum] = data
        curSType = None
        data_sNum = b_info.bnum / pInfo.blockMag
        for s in pInfo.sfLoc:
            for e in pInfo.sfLoc[s]:
                if e.isIn(data_sNum):
                    curSType = s
                    break
            if curSType != None:
                break
            
        d_chInfo = objectChangeInfo(data, curSType)
        j_ch = JournalChange("Insert", '', hex(b_info.bnum), d_chInfo)
        return [j_ch]
    classType = data.__class__.__name__
    cursur[b_info.bnum] = data
    return data_diff(p_data, data, hex(b_info.bnum), classType)
    
def data_diff(original, changed, parType='', curType=''):
    
    try:
        assert original.__class__ == changed.__class__
    except(AssertionError):
        o_chInfo = objectChangeInfo(original, original.__class__.__name__)
        o_j_ch = JournalChange("Remove", parType, curType, o_chInfo)
        c_chInfo = objectChangeInfo(changed, changed.__class__.__name__)
        c_j_ch = JournalChange("Insert", parType, curType, c_chInfo)
        return [o_j_ch, c_j_ch]
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
        return [j_ch]
    
    if dType == tuple:
        count = 0
        for i, j in zip(original, changed):
            result.extend(data_diff(i, j, curType, curType + "_%d" % count))
            count += 1
        return result
    
    if dType == list:
        result.extend(compCatalog(original, changed, parType, curType))
        return result
    
    if dType == memoryview:
        if original == changed: return []
        r_chInfo = renewalChangeInfo(original, changed)
        j_ch = JournalChange("Renewal", parType, curType, r_chInfo)
        return [j_ch]
    
    if dType in [unicode, str]:
        return []
    
    attList = original._fields
    for att in attList:
        next = att
        try:
            if getattr(getattr(original,att), 'getAbs'):
                next = getattr(original,att).getAbs()
        except(AttributeError):
            pass        
        result.extend(data_diff(getattr(original,att), getattr(changed, att), parType+"\\"+str(curType), next))
    return result
    
    
def compCatalog(original, changed, parType, curType):
    orgSet = set(original)
    chgSet = set(changed)
    insList = chgSet - orgSet
    modList = orgSet & chgSet
    remList = orgSet - chgSet
    result = []
            
    for i in insList:
        chInfo = objectChangeInfo(i, i.getAbs())
        j_ch = JournalChange("Insert", parType+"\\"+curType, "", chInfo)
        result.append(j_ch)
    
    for r in remList:
        chInfo = objectChangeInfo(r, r.getAbs())
        j_ch = JournalChange("Remove", parType+"\\"+curType, "", chInfo)
        result.append(j_ch)
        
    for m in modList:
        m_org = [x for x in original if m == x][0]
        m_chg = [x for x in changed if m == x][0]
        result.extend(data_diff(m_org, m_chg, parType+"\\"+curType, m_org.getAbs()))
        
    return result

def main():
    f = open(r"C:\Users\user\Desktop\Journal=t", 'rb')
    s = f.read()
    jPList, pInfo = journalParser(s)
    jT = journalTrack(jPList, pInfo)
    g = open(r"C:\TEMP\result_2.txt", 'w')
    for i in jT:
        g.write("-----------\n")
        for j in i:
            g.write(str(j)+"\n")
    
    g.close()
    f.close()
    
if __name__ == '__main__':
    main()
    