#!/usr/bin/env python
import sys
import pickle


#implementing jaccard
def jaccard(a, b):
    c = a.intersection(b)
    return float(len(c)) / (len(a) + len(b) - len(c))

p = {
    4: {},
    6: {}
}

peer2asn = {} # for convenience

for line in sys.stdin:
    pcs = line.split('|')
    peer = pcs[3]
    pfx = pcs[5]
    af = 4
    if ':' in pfx:
        af = 6

    #if not peer in fullfeeds[ af ]:
    #    continue # not a full feed!

    #if not af == 6: # we only look into v6 in this script
    #    continue

    if not peer in p[af]:
        p[af][ peer ] = set()
        peer_asn = pcs[4]
        peer2asn[ peer ] = peer_asn
    aspath = pcs[6].split(' ')
    plen = len( aspath )
    #TODO remove path-poisoning?
    for idx,asn in enumerate( aspath ):
        if idx + 1 == plen:
            break
        nxt_asn = aspath[ idx + 1 ]
        if asn != nxt_asn:
            p[af][ peer ].add( ( asn, nxt_asn ) )

#TODO remove AS-es that are stub?

### pickle the datastruct
dbfile = open('./as-links.pcl','wb')
pickle.dump( p, dbfile )
dbfile.close()

sys.exit(0)

# sort keys
print "#af peerasn1 peerasn2 peer1 peer2 #links1 #links2 jaccard"
for af in (4,6):
        peers = sorted( p[af].keys() )

        for idx1,peer1 in enumerate( peers ):
            as_links1 = p[af][ peer1 ]
            for peer2 in peers[idx1+1:]:
                as_links2 = p[af][ peer2 ]
                try:
                    j = jaccard( as_links1, as_links2 )
                    print "%s %s %s %s %s %s %s %0.8f" % ( af, peer2asn[ peer1 ], peer2asn[ peer2 ], peer1, peer2, len( as_links1), len( as_links2), j )
                except:
                    print "#### %s %s %s %s %s %s" % ( peer2asn[ peer1 ], peer2asn[ peer2 ], peer1, peer2, len( as_links1), len( as_links2) )
