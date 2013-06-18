#!/usr/bin/env python

import sys
import time

def tail_f (logfile):
    logfile.seek (0,2) # .seek (offset, origion) -> 0 is is in characters and is measured from the beginning; 2 is (from the end of the file)
    while True:
        line = logfile.readline()
        if not line:
            time.sleep (0.5)
            continue
        yield line

logfile = sys.argv[1] # take parameters from comandline
logfile = open ('security.log','r')
for line in tail_f (logfile):
    print line
