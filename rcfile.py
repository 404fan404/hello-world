#!/usr/bin/env python3
import argparse
from random import choice,randint
'''
产生一个随机文件
'''
parser = argparse.ArgumentParser()

parser.add_argument('file')
parser.add_argument('-s','--size',type=int,default=-1)
args = parser.parse_args()
myfile = args.file
char_size = args.size

a = [chr(i) for i in range(32,127)]
tmp1 = [chr(i) for i in range(161,255) if i != 173]

a = ''.join(a) + '\n\t '+ ''.join(tmp1)

if myfile:
    temp = myfile
else:
    temp = []
    for i in range(randint(1,10)):
        temp.append(a[randint(0,len(a)-1)])
    temp = ''.join(temp) + '.txt'
files = open(temp,'w')
if char_size <= 0:
    num = randint(1,2**16)
else:
    num = char_size
for i in range(num):
    files.write(choice(a))    
files.close()
