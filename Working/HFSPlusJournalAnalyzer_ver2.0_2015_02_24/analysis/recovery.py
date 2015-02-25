from lib.etc_util import DiskDump

def recovery(disk,path,target,jParseList,vh):
    d=target.find(',')
    CNID=int(target[1:d])
    nodeName=target[d+1:-1]
    for i in range(len(jParseList)-1,0,-1):

        blocks=jParseList[i][2]
        for j in range(len(blocks)-1,-1,0):
            
            try:

                records=blocks[j].LeafRecList

                if 'Catalog'==records[0].getType():

                    for k in xrange(len(records)):

                        if records.key.nodeName.nodeUnicode==unicode(nodeName) and records.record.CNID==CNID:

                            dataFork=[]
                            extents=records.record.dataFork.extents
                            for l in extents._asdict().itervalues():
                                dataFork.append(DiskDump(disk,'',vh.blockSize,l.startBlock,l.blockCount))
                            dataFork=''.join(dataFork)
                            f=open('{0}/{1}_DataFork'.format(path,nodeName),'wb')
                            f.write(dataFork)
                            f.close()

                            resourceFork=[]
                            extents=records.record.resourceFork.extents
                            for l in extents._asdict().itervalues():
                                resourceFork.append(DiskDump(disk,'{0}/{1}'.format(path,nodeName),vh.blockSize,l.startBlock,l.blockCount))
                            resourceFork=''.join(resourceFork)
                            f=open('{0}/{1}_ResourceFork'.format(path,nodeName),'wb')
                            f.write(resourceFork)
                            f.close()

                            return


            except AttributeError:
                pass