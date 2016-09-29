#!/bin/env python

import sys
import itertools
import operator

SKIP_SINGLES = False

if __name__ == "__main__":
    jobs = []
    for line in sys.stdin:
        tokens = line.split()
        j = {
            'id': tokens[0],
            'partition': tokens[1],
            'name': tokens[2],
            'user': tokens[3],
            'status': tokens[4],
        }
        jobs.append(j)
    groups, uniquekeys = [], []
    kva = sorted(jobs, key=operator.itemgetter('name'))
    for k, g in itertools.groupby(kva, key=operator.itemgetter('name')):
        groups.append(list(g))
        uniquekeys.append(k)
        
    i = 0
    def f(x):
        return tuple([len(groups[x]), groups[x][0]['name']])
    if SKIP_SINGLES:
        groups = [x for x in filter(lambda x: len(x) > 1, groups)]
    while i < len(groups):
        try:
            print("%2s %-20s %2s %-20s %2s %s" % (f(i) + f(i + 1) + f(i + 2)))
        except IndexError:
            if i + 2 == len(groups):
                print("%2s %-20s %2s %s" % (f(i) + f(i + 1)))
            else:
                print("%2s %s" % f(i))
        i += 3
