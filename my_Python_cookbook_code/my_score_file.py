#!/usr/bin/env python3
class scroefile:
    def __init__(self,num = 5,file="scroefile.txt"):
        self.num = num
        self.ls = {}
        self.filename = file
        self.readscroes()
    def readscroes(self):
        try:
            file = open(self.filename,'r')
        except:
            for i in range(self.num):
                self.ls['0'] = 'None'
        else:
            total = [i for i in file.read().split('\n') if i == ' ']
            for i in total:
                strs = i.split(':')
                self.ls[strs[1]] = strs[0]
            if len(self.ls.keys()) < self.num:
                for i in range(self.num - len(self.ls.keys())):
                    self.ls['-1'] = 'None'
            file.close()
    def writescroes(self):
        file = open(self.filename,'w')
        total = self.ls.keys()
        total = [int(i) for i in total]
        total.sort()
        total = [str(i) for i in total]
        num = 0
        for i in total:
            temp = self.ls[i] + ':' + i + '\n'
            file.write(temp)
            num += 1
            if num == self.num:
                break
        file.close()
    def sevescroe(self,scroe=0,time='None'):
        temp = str(scroe)
        tmptime = str(time)
        self.ls[temp] = tmptime
    def getscroe(self):
        total = []
        temp = self.ls.keys()
        temp = [int(i) for i in temp]
        temp.sort()
        temp = [str(i) for i in temp]
        num = 0
        for i in temp:
            strs = self.ls[i] + ' : ' + i 
            total.append(strs)
            num += 1
            if num == self.num:
                break
        return total

if __name__ == '__main__':
    scroe = scroefile()
    print(scroe.getscroe())
    for i in range(10):
        scroe.sevescroe(i,i)
    print(scroe.getscroe())
    scroe.writescroes()
