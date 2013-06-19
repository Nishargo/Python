#!/usr/bin/env python
# -*- coding: utf-8

# Написать реализацию tail -f, используя ключевое слово yield. 
# Реализовать функцию-генератор tailf, которая выдает следующую строку по запросу, а не все сразу.


import sys,os, time

def tail_f (logfile):
    while True:
        with f as myfile:
            myfile.seek(0,2)
            myfilesize = myfile.tell() # Get Size
            myfile.seek(max(myfilesize-1024,0),0)
            line = myfile.readline() # Read to end
        line = line[-10:] # Get last 10 lines
        if not line:
            time.sleep(0.5)
            continue
        yield line

#def tail_f (logfile):
#    logfile.seek (0,0)
#    while True:
#        line = logfile.readline()
#        if not line:
#            time.sleep (0.5)
#            continue            
#        yield line

logfile = sys.argv[1] # take parameters from comandline
f = open (logfile)
for line in tail_f (f):
    print line
