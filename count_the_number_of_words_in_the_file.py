#统计文件中每个单词个数（按空格分割），最后按词频降序打印
with open('words.txt','r') as f:[print("{},{}".format(*i)) for i in sorted([(key,value) for key,value in __import__('collections').Counter([w for l in f.readlines() for w in l.split()]).items()],key=lambda a:a[1],reverse=True)]
