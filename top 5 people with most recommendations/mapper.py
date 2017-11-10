#!/usr/bin/env python2

import itertools
import sys

for line in sys.stdin:
    line = line.strip()
    line = line.split("\t")
    key = int(line[0])
    if len(line)>1:
        friends = line[1]
        if friends!='':
            friends = line[1].split(",")
            friends = sorted(map(int,friends))
            for friend in friends:
                pair = tuple(sorted([key,friend]))
                pair = ','.join(map(str,pair))
                print pair,"\t",1
            for pair in itertools.combinations(friends,2):
                pair = ','.join(map(str,pair))
                print pair,"\t",0
