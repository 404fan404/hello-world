#!/usr/bin/env python3
import sys
import os

path_list = ( x for x in os.environ.get('PATH').split(':') if x != '')
num = 0
files = sys.argv[1]

for i in path_list:
    try:
        str = open(i + '/' + files,'r')
    except:
        continue
    else:
        print(i + '/' + files)
        num += 1
        break
if num == 0:
    print(files,'not found')
