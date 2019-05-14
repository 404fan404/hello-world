#!/usr/bin/env python3
#统计文件中每个单词个数（按空格分割），最后按词频降序打印
#with open('words.txt','r') as f:[print("{},{}".format(*i)) for i in sorted([(key,value) for key,value in __import__('collections').Counter([w for l in f.readlines() for w in l.split()]).items()],key=lambda a:a[1],reverse=True)]

import sys
import re

def sortkey(item):
  return item[1]

argv = [i for i in sys.argv[1:]]
if len(argv) < 1:
  #若未传入参数则默认统计文件名为words.txt文件中的单词
  argv.append('./words.txt')

worddict = {}

for filename in argv:
  with open(filename ,'r') as f:
    for line in f:
      wordlist = [i for i in re.split(r'''[.,;:'"?/!@#$%^&*()_+-=\[\]{}\s]+''',line) if i != '']
      for word in wordlist:
        wordnum = worddict.get(word,0)
        worddict[word] = wordnum + 1

worddictitem = [(key,value) for key,value in worddict.items()]
worddictitem.sort(key=sortkey,reverse=True)

print("word\tnum")
for item in worddictitem:
  print("{}\t{}".format(*item))
