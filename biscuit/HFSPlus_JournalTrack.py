'''
Created on 2015. 2. 8.

@author: biscuit
'''
from HFSPlus_ParseModule import *

class JournalChange:
    changeType = None
    parAtt = None
    curAtt = None
    changeInfo = None
    
    def __init__(self, changeType, parAtt=None, curAtt=None, changeInfo=None):
        typeList = ["Insert", "Remove", "Modify", "Date"]
        infoDict = {'Insert':objectChangeInfo, 'Remove':objectChangeInfo,
                    'Modify':valueChangeInfo, 'Date':dateChangeInfo}
        self.changeType = changeType
        self.parAtt = parAtt
        self.curAtt = curAtt
        self.changeInfo = changeInfo
        assert changeType in typeList
        assert type(changeInfo) == infoDict[changeType]
    
class valueChangeInfo:
    before = 0
    after = 0
    diff = 0
    def __init__(self, before, after):
        self.before = before
        self.after = after
        self.diff = self.after - self.before
        
class dateChangeInfo:
    before = 0
    after = 0
    renewal = False
    def __init__(self, before, after):
        self.before = before
        self.after = after
        if before != after:
            self.renewal = True

class objectChangeInfo:
    object = None
    absData = None
    def __init__(self, object, absData):
        self.object = object
        self.absData = absData

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
        d_chInfo = objectChangeInfo(data, None)
        j_ch = JournalChange("Insert", None, hex(b_info.bnum), d_chInfo)
        return [j_ch]
    classType = data.__class__.__name__
    return data_diff(p_data, data, None, classType)
    
def data_diff(original, changed, parType=None, curType=None):
    assert type(original) == type(changed)
    result = []
    
    if type(original) in [int, long]:
        v_chInfo = valueChangeInfo(original, changed)
        j_ch = JournalChange("Modify", parType, curType, v_chInfo)
    
    if type(original) == tuple:
        count = 0
        for i, j in zip(original, changed):
            result.extend(data_diff(i, j, curType + "_%d" % count))
        return
    
    
        
    
    attList = original._fields
    for att in attList:
        result.extend(data_diff(getattr(original,att), getattr(changed, att), curType, att))
    
    
        
        
        

        
    
    
    
    
    
    