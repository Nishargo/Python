#!/usr/bin/env python
# -*- coding: utf-8

# Написать реализацию tail -f, используя ключевое слово yield. 
# Реализовать функцию-генератор tailf, которая выдает следующую строку по запросу, а не все сразу.


import sys, os, time

def tail_f (logfile):
   logfile.seek (0,2)
    while True:
        line = logfile.readline()
        if not line:
            time.sleep (0.5)
            continue
        yield line

logfile = sys.argv[1] # take parameters from comandline

for line in tail_f (logfile):
    print line
