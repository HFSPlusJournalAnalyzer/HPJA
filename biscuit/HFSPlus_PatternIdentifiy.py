'''
Created on 2015. 2. 16.

@author: biscuit
'''
from HFSPlus_JournalTrack import *
from HFSPlus_ParseModule import *
from collections import namedtuple

CatalogPatVector = namedtuple("CatalogPatVector", ['contModDate', 'attrModDate', 'accessDate', 
                                                   'logicalSize', 'totalBlocks',
                                                   'remove', 'insert',
                                                   'thID'])



class JournalPattern:
    def __init__(self, patternName, pattern):
        self.patternName = patternName
        self.pattern = CatalogPatVector(*pattern)
        
    def __eq__(self, other):
        return self.pattern == other.pattern
    
    def hasPattern(self, dataChange):
        return self.pattern == getCatalPattern(dataChange)

PatternSet = [JournalPattern('Insert', [0,0,0,0,0,0,1,0]),
              JournalPattern('Remove', [0,0,0,0,0,1,0,0]),
              JournalPattern('Read/Modify', [1,1,1,0,0,0,0,0]),
              JournalPattern('Read/Modify', [1,1,1,0,1,0,0,0]),
              JournalPattern('Read/Modify', [1,1,1,0,-1,0,0,0]),
              JournalPattern('Modify(no size change)', [1,1,0,0,0,0,0,0]),
              JournalPattern('Modify(size extended)', [1,1,0,1,1,0,0,0]),
              JournalPattern('Modify(size extended)', [1,1,0,1,0,0,0,0]),
              JournalPattern('Read', [0,0,1,0,0,0,0,0]),
              JournalPattern('Read/Modify', [0,0,1,-2,-2,0,0,0])
              ]    

def getCatalPattern(CataldataChange):
    initvec = [0]*8
    setCatPatVect(CataldataChange, initvec)
    return CatalogPatVector(*initvec)

def setCatPatVect(change, catVector):
    if change.__class__ == renewalChangeInfo:
        dateType = ['contentModDate', 'attributeModDate', 'accessDate']
        if change.__name__ in dateType:
            catVector[dateType.index(change.__name__)] = 1
        return
    if change.__class__ == objectChangeInfo:
        if change.chType == 'Insert':
            catVector[6] = 1
        if change.chType == 'Remove':
            catVector[5] = 1
        return
    if change.__class__ == valueChangeInfo:
        if change.__name__ == 'logicalSize':
            if change.diff != 0:
                catVector[3] = change.diff / abs(change.diff)
            if change.after == 0:
                catVector[3] = -2
        if change.__name__ == 'totalBlocks':
            if change.diff != 0:
                catVector[4] = change.diff / abs(change.diff)
            if change.after == 0:
                catVector[4] = -2
        if change.__name__ == "parentID":
            catVector[7] = 1
        return
    for i in change.chList:
        setCatPatVect(i, catVector)

def refineTrack(journalTrack):
    refPass1 = []
    for i in journalTrack:
        temp = [j for j in i if j.__class__ == dataChangeHead]
        if temp != []:
            refPass1.append(temp)
    
    refPass2 = []
    for i in refPass1:
        temp = [j for j in i if j.type == "CatalogFile"]
        if temp != []:
            refPass2.append(temp)
            
    return refPass2

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
                        type = r.absData['type']
                        if type == "thread":
                            ID = r.object.key.parentID
                        else:
                            ID = r.object.record.CNID
                    try:
                        temp = IDdict[ID]
                    except(KeyError):
                        IDdict[ID] = []
                        temp = IDdict[ID]
                    temp.append(r)
        result.append(IDdict)
    return result


def inspectPattern(journalTrack):
    #for tBucket in journalTrack:
    
    pass

def main():
    global PatternSet
    f = open(r"C:\Users\user\Desktop\Journal_2", 'rb')
    s = f.read()
    jPList, pInfo = journalParser(s)[:2]
    jT = journalTrack(jPList, pInfo)
    r = refineTrack(jT)
    c = catalogGrouping(r)
    
    g = open(r"C:\TEMP\result_2.txt", 'w')
    for i,j in enumerate(c):
        g.write("%d====\n" %i)
        for x, k in j.iteritems():
            for p in k:
                a = 0
                for Pat in PatternSet:
                    if Pat.hasPattern(p):
                        try:
                            g.write("[%s] %s\n" %(Pat.patternName, p.nData))
                            a = 1
                            break
                        except(AttributeError):
                            g.write("[%s] %s\n" %(Pat.patternName, p.absData))
                            a = 1
                            break
                if a == 0:
                    print "Unknown"
                    print p
                    print '---------'
                
    
    f.close()
    
if __name__ == '__main__':
    main()