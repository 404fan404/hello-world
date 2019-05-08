#统计文件中每个单词个数（按空格分割），最后按词频降序打印
for i in sorted([(key,value) for key,value in __import__('collections').Counter([w for l in open('words.txt','r').readlines() for w in l.split()]).items()],key=lambda a:a[1],reverse=True):print("{} {}".format(i[0],i[1]))
