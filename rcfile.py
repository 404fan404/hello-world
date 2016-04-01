#!/usr/bin/env python3
import argparse
from random import choice,randint

parser = argparse.ArgumentParser()

parser.add_argument('file')
parser.add_argument('-s','--size',type=int,default=-1)
args = parser.parse_args()
myfile = args.file
char_size = args.size

a = 'qwertyuiopasdfghjkl;zxcvbnm,./\'[]\\1234567890-=`~!@#$%^&*()_+{}|:"<>?QWERTYUIOPASDFGHJKLZXCVBNM'
if myfile:
    temp = myfile
else:
    temp = []
    for i in range(randint(1,10)):
        temp.append(a[randint(0,len(a)-1)])
    temp = ''.join(temp) + '.txt'
files = open(temp,'w')
if char_size == -1:
    num = randint(1,2**16)
else:
    num = char_size
for i in range(num):
    files.write(choice(a))    
files.close()
