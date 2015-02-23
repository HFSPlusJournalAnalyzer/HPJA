# -*- coding:utf-8 -*-
'''
Created on 2015. 2. 16.

@author: biscuit
'''
from HFSPlus_JournalTrack import *
from HFSPlus_ParseModule import *
from collections import namedtuple
import codecs

class CatalObjPatVec(namedtuple("CatalObjPatVec", ['Insert', 'Remove'])):
    def __str__(self):
        str_o = ""
        for i, j in zip(self, self._fields):
            str_o += j*i
        return str_o

class CatalFilePatVec(namedtuple("CatalFilePatVec", ['modDate', 'Access', 'sizeChange', 'parentID'])):
    def __hash__(self):
        return hash(("CatalFilePatVec", self.modDate, self.accessDate, self.size))
    def __str__(self):
        str_o = ""
        for i, j in zip(self, self._fields):
            str_o += (j+"/")*i
        return str_o[:-1]
class CatalFoldPatVec(namedtuple("CatalFoldPatVec", ['modDate', 'Access', 'valence', 'parentID'])):
    def __hash__(self):
        return hash(("CatalFoldPatVec", self.modDate, self.accessDate, self.valence))
    def __str__(self):
        str_o = ""
        for i, j in zip(self, self._fields):
            str_o += (j+"/")*i
        return str_o[:-1]
    
CatalThreadPatVec = namedtuple("CatalThreadPatVec", ['parentID'])

class CatalPattern:
    def __init__(self, patName, type, patTime, data, recName):
        self.patName, self.type = patName, type
        self.patTime = patTime
        self.data, self.recName = data, recName
    
    def __eq__(self, other):
        return (self.patName == other.patName) and (self.type == other.type)
    
    def __repr__(self):
        return "[%s] %s / %s / %s\n" %(self.patName, self.type, self.recName, getHFSTime(self.patTime))

    def __str__(self):
        return "[%s] %s / %s / %s\n" %(self.patName, self.type, self.recName.encode('utf8'), getHFSTime(self.patTime))
        
    def hasPattern(self, dataChange):
        return self == CatalRecPattern(dataChange)


#Update
#

def CatalRecPattern(CataldataChange):
    if CataldataChange.__class__ == objectChangeInfo:
        chType = CataldataChange.chType
        vec = [(0,1), (1,0)][chType == 'Insert']
        Pvec =  CatalObjPatVec(*vec)
        rType = CataldataChange.absData['type']
        if rType == "thread":
            rTime = 0
            nodeName = CataldataChange.object.record.nodeName.nodeUnicode
        else:
            rTime = [0, CataldataChange.object.record.createDate][chType == 'Insert']
            nodeName = CataldataChange.object.key.nodeName.nodeUnicode
        
        return CatalPattern(Pvec, rType, rTime, CataldataChange.object, nodeName)
    type = CataldataChange.nData['type']
    vecSetDict = {'file': setFileVec, 'folder': setFoldVec, 'thread': setThreadVec}
    vecDict = {'file':CatalFilePatVec, 'folder': CatalFoldPatVec, 'thread': CatalThreadPatVec}
    vec, rTime = vecSetDict[type](CataldataChange, [])
    Pvec = vecDict[type](*vec)
    return CatalPattern(Pvec, type, rTime, CataldataChange, CataldataChange.nData['nodeName'])

def setFileVec(CataldataChange, initvec):
    if initvec == []:
        initvec = [0]*4
        
    if CataldataChange.__class__ == renewalChangeInfo:
        if CataldataChange.__name__ in ['contentModDate', 'attributeModDate']:
            initvec[0] = 1
            time = CataldataChange.after
        if CataldataChange.__name__ == 'accessDate':
            initvec[1] = 1
            time = CataldataChange.after
        return (initvec, time)
    
    if CataldataChange.__class__ == valueChangeInfo:
        if CataldataChange.__name__ == 'logicalSize':
            if CataldataChange.diff != 0:
                initvec[2] = 1
        if CataldataChange.__name__ == 'totalBlocks':
            if CataldataChange.diff != 0:
                initvec[2] = 1
        if CataldataChange.__name__ == 'parentID':
            if CataldataChange.diff != 0:
                initvec[3] = 1
        return (initvec, 0)
    
    time = 0
    for i in CataldataChange.chList:
        initvec, tTime = setFileVec(i, initvec)
        if tTime != 0:
            time = tTime
    
    return initvec, time

def setFoldVec(CataldataChange, initvec):
    if initvec == []:
        initvec = [0]*4
        
    if CataldataChange.__class__ == renewalChangeInfo:
        if CataldataChange.__name__ in ['contentModDate', 'attributeModDate']:
            initvec[0] = 1
            time = CataldataChange.after
        if CataldataChange.__name__ == 'accessDate':
            initvec[1] = 1
            time = CataldataChange.after
        
        return (initvec, time)
    
    if CataldataChange.__class__ == valueChangeInfo:
        if CataldataChange.__name__ == 'valence':
            if CataldataChange.diff != 0:
                initvec[2] = 1
        if CataldataChange.__name__ == 'parentID':
            if CataldataChange.diff != 0:
                initvec[3] = 1
        return (initvec, 0)

    time = 0
    for i in CataldataChange.chList:
        initvec, tTime = setFoldVec(i, initvec)
        if tTime != 0:
            time = tTime
    
    return initvec, time

def setThreadVec(CataldataChange, initvec):
    return ([1], 0)

def getCatPatSet(catGroup):
    result = []
    threadStream = []
    for catDict in catGroup:
        patDict = {}
        temp2 = []
        for key, chList in catDict.iteritems():
            temp1 = []
            for r in chList:
                p = CatalRecPattern(r)
                if p.patName == CatalThreadPatVec(1):
                    temp2.append(p)
                else: temp1.append(CatalRecPattern(r))
            if temp1 != []:
                patDict[key] = temp1
        result.append(patDict)
        threadStream.append(temp2)
    return result, threadStream

def cleanPatSet(cPatset):
    for i, j in enumerate(cPatSet):
        cPatSet[i] = dict((k, v) for k, v in j.iteritems() if v != [])
    return cPatSet

def threadHandle(cPatSet, thStream):
    for cPatDict, thList in zip(cPatSet, thStream):
        if thList == []:
            continue
        for th in thList:
            id_ch = th.data.chList[0].chList[0]
            before, after = id_ch.before, id_ch.after
            try:
                bef_log = cPatDict[before]
                aft_log = cPatDict[after]
            except(KeyError):
                continue
            
            done = 0
            for i in bef_log:
                if i.patName == CatalObjPatVec(0,1):
                    done += 1
                    break
            for j in aft_log:
                if j.patName == CatalObjPatVec(1,0):
                    done += 1
                    break
            if done == 2:
                bef_log.remove(i)
                aft_log.remove(j)
                aft_log.append(CatalPattern("Update", i.type, j.data.record.createDate, [i,j,th], j.recName))
                
    
    return cPatSet

def Create(cPatSet):
    for cPatDict in cPatSet:
        for k, v in cPatDict.iteritems():
            fPart = None
            tPart = None
            for l in v:
                if l.patName == CatalObjPatVec(1,0):
                    if l.type in ['file', 'folder']:
                        fPart = l
                    if l.type == 'thread':
                        tPart = l
            if (fPart != None) and (tPart != None):
                v.remove(fPart)
                v.remove(tPart)
                v.append(CatalPattern("Create", fPart.type, fPart.data.record.createDate, [fPart, tPart], fPart.recName))
    
    return cPatSet

def Delete(cPatSet):
    for cPatDict in cPatSet:
        for k, v in cPatDict.iteritems():
            fPart = None
            tPart = None
            for l in v:
                if l.patName == CatalObjPatVec(0,1):
                    if l.type in ['file', 'folder']:
                        fPart = l
                    if l.type == 'thread':
                        tPart = l
            if (fPart != None) and (tPart != None):
                v.remove(fPart)
                v.remove(tPart)
                v.append(CatalPattern("Delete", fPart.type, fPart.data.record.createDate, [fPart, tPart], fPart.recName))

    return cPatSet

def refineTrack(journalTrack):
    refPass1 = []
    for i in journalTrack:
        temp = [j for j in i if j.__class__ == dataChangeHead]
        if temp != []:
            refPass1.append(temp)
    
    refPass2 = []
    for i in refPass1:
        temp = [j for j in i if j.type == "Catalog"]
        if temp != []:
            refPass2.append(temp)
    
    refPass3 = []
    for i in refPass2:
        temp = []
        for j in i:
            try:
                for k in j.chList:
                    k.nData
                temp.append(j)
            except(AttributeError):
                continue
            
        if temp != []:
            refPass3.append(temp)
            
    refPass4 = []
    for i in refPass3:
        temp = []
        for j in i:
            check = False
            for k in j.chList:
                if k.nData == 'PointerRecList':
                    check = True
            if not check:
                temp.append(j)
                
        if temp != []:
            refPass4.append(temp)
            
    return refPass4

def catalogGrouping(refineCatalog):
    result = []
    for i in refineCatalog:
        IDdict = {}
        for dChHead in i:
            for dCh in dChHead.chList:
                try:
                    if dCh.nData != 'LeafRecList':
                        continue
                except(AttributeError):
                    continue
                RecCh = dCh.chList
                for r in RecCh:
                    if r.__class__ == dataChange:
                        try:
                            ID = r.nData['ID']
                        except(KeyError):
                            ID = r.nData['parID']
                    if r.__class__ == objectChangeInfo:
                        try:
                            ID = r.object.record.CNID
                        except(AttributeError):
                            ID = r.object.key.parentID
                    try:
                        temp = IDdict[ID]
                    except(KeyError):
                        IDdict[ID] = []
                        temp = IDdict[ID]
                    temp.append(r)
        result.append(IDdict)
    return result

def printCatalPatSet(cPatSet, fd):
    count = 1
    for i in cPatSet:
        fd.write("trans_%d=================================\n" %count)
        for cNum, chList in i.iteritems():
            fd.write("@%s\n" %cNum)
            for k in chList:
                fd.write(" "+str(k))
        count += 1

def main():
    f = open(r"C:\Users\user\Desktop\Journal_2222", 'rb')
    s = f.read()
    jPList, pInfo = journalParser(s)[:2]
    jT = journalTrack(jPList, pInfo)
    r = refineTrack(jT)
    h = open(r"C:\TEMP\result_mal_init_1.txt", 'w')
    journalTrackPrint(r, h)
    h.close()
    c = catalogGrouping(r)
    
    p, t = getCatPatSet(c)
    P = threadHandle(p, t)
    P = Create(P)
    P = Delete(P)
    
    g = open(r"C:\TEMP\result_mal_init_2.txt",'w')
    
    printCatalPatSet(P, g)
    
    f.close()
    
if __name__ == '__main__':
    main()