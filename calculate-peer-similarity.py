#!/usr/bin/env python
import sys
import pickle
import gzip
import time

#implementing jaccard
def jaccard(a, b):
    c = a.intersection(b)
    return float(len(c)) / (len(a) + len(b) - len(c))

### pickle the datastruct
print >>sys.stderr, "start loading"
st = time.time()
#dbfile = gzip.open(sys.argv[1],'rb')
dbfile = open(sys.argv[1],'rb')
p = pickle.load( dbfile )
dbfile.close()
et = time.time()
print >>sys.stderr, "finish loading in %s secs." % ( et - st )

print "#af peer1 peer2 #links1 #links2 jaccard-sim"
# sort keys
for af in (4,6):
        peers = sorted( p[af].keys() )

        for idx1,peer1 in enumerate( peers ):
            as_links1 = p[af][ peer1 ]
            for peer2 in peers[idx1+1:]:
                as_links2 = p[af][ peer2 ]
                try:
                    j = jaccard( as_links1, as_links2 )
                    print "%s %s %s %s %s %0.8f" % ( af, peer1, peer2, len( as_links1), len( as_links2), j )
                except:
                    print "#### %s %s %s %s %s" % ( af, peer1, peer2, len( as_links1), len( as_links2) )
