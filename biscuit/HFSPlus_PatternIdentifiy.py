'''
Created on 2015. 2. 16.

@author: biscuit
'''
from HFSPlus_JournalTrack import *
from HFSPlus_ParseModule import *

class JournalPattern:
    pass

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
    f = open(r"C:\Users\user\Desktop\Journal_2", 'rb')
    s = f.read()
    jPList, pInfo = journalParser(s)[:2]
    jT = journalTrack(jPList, pInfo)
    r = refineTrack(jT)
    c = catalogGrouping(r)
    
    g = open(r"C:\TEMP\result_2.txt", 'w')
    for i,j in enumerate(c):
        g.write("%d=====\n"%i)
        for x, k in j.iteritems():
            g.write("%d---\n" %x)
            for p in k:
                g.write("%s" %p)
    
    
    f.close()
    
if __name__ == '__main__':
    main()