#!/bin/env python

import sys
import itertools
import operator
from collections import defaultdict, namedtuple

TRESHOLD_NODECOUNT = 6
job_info = namedtuple('job_info', ["partition", "user", "status", "nodecount"])

if __name__ == "__main__":
    running_nodecount = defaultdict(lambda: 0)
    pending_nodecount = defaultdict(lambda: 0)
    all_jobs = []
    for line in sys.stdin:
        tokens = line.split()
        j = job_info(
            partition=tokens[0],
            user=tokens[1],
            status=tokens[2],
            nodecount=tokens[3]
        )
        all_jobs.append(j)
        if j.status == 'RUNNING':
            running_nodecount[j.user] += int(j.nodecount)
        elif j.status == 'PENDING': # Not used currently
            pending_nodecount[j.user] += int(j.nodecount)

    groups, uniquekeys = [], []
    kva = sorted(all_jobs, key=operator.attrgetter('user'))
    for k, g in itertools.groupby(kva, key=operator.attrgetter('user')):
        groups.append(list(g))
        uniquekeys.append(k)
        
    # TODO: should use Counter class instead
    i = 0

    while i < len(groups):
        u = groups[i][0].user
        info = (len(groups[i]), running_nodecount[u], u)
        if not (running_nodecount[u] < TRESHOLD_NODECOUNT):
            print("%2s jobs occupying %3d nodes by %-20s " % info)
        i += 1
