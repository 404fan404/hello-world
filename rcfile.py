#!/usr/bin/env python3
from random import choice
a = '''qwertyuiopasdfghjkl;zxcvbnm,./\'
[]\\1234567890-=`~!@#$%^&*()_+
{}|:"<>?QWERTYUIOPASDFGHJKLZXCVBNM'''
files = open('tmp.txt','w')
for i in range(2500):
    files.write(choice(a))
files.close()
