#!/usr/bin/env python
# -*- coding: utf-8

# Написать реализацию tail -f, используя ключевое слово yield. 
# Реализовать функцию-генератор tailf, которая выдает следующую строку по запросу, а не все сразу.

import sys, time

def tail_f (logfile):    
    while True:
        lines = logfile.readlines()
        last_10_lines = lines[-10:]          
        if not lines:
            time.sleep (0.5)
            continue            
        yield last_10_lines

logfile = sys.argv[1] 
f = open (logfile)
for last_10_lines in tail_f (f):
    print last_10_lines

# Просто прочиает файл и выведет его на экран
#logfile = sys.argv[1]
#f = open (logfile)
#for line in f:
#    print line.rstrip('\n')

# либо же выведет файл как список (list) и последние 10 элементов
#logfile = sys.argv[1]
#f = open (logfile)
#lines = f.readlines()
#last_10_lines = lines[-10:]
#print last_10_lines

# вывести последние 10 элементов из списка без срезов, с помощью цикла
#logfile = sys.argv[1]
#f = open (logfile)
#lines = f.readlines()
#len_list = len(lines)
#for line in range(len_list-10, len_list):    
#    print lines[line]
