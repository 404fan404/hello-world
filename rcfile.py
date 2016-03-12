#!/usr/bin/env python3
from random import choice,randint
a = '''qwertyuiopasdfghjkl;zxcvbnm,./\'
[]\\1234567890-=`~!@#$%^&*()_+
{}|:"<>?QWERTYUIOPASDFGHJKLZXCVBNM'''
temp = []
for i in range(randint(1,10)):
    temp.append(a[randint(0,len(a)-1)])
files = open(''.join(temp)+'.txt','w')
for i in range(randint(1,2**16)):
    files.write(choice(a))
files.close()
