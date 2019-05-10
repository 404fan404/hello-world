#!/usr/bin/env python3
# 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
# 暂时没有优化，勉强能用
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        numdict = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        num1len,num2len = len(num1),len(num2)
        totallen = num1len+num2len
        sumlist = [[0 for i in range(totallen + 1)] for j in range(num2len)]
        for i in range(num2len):
            n2 = numdict[num2[num2len - i - 1]]
            lestnum = 0
            for j in range(num1len):
                n1 = numdict[num1[num1len - j -1]]
                nownum = n1 * n2 + sumlist[i][i+j]
                firstnum = nownum % 10
                sumlist[i][i+j] = firstnum
                if (nownum - firstnum) > 0:
                    lestnum = int((nownum - firstnum) / 10)
                    sumlist[i][i+j+1] += lestnum
                else:
                    lestnum = 0
        rlist = [0 for i in range(totallen + 1)]
        for i in range(totallen):
            nownum = rlist[i]
            for j in range(num2len):
                nownum += sumlist[j][i]
            firstnum = nownum % 10
            rlist[i] = firstnum
            if (nownum - firstnum) > 0:
                lestnum = int((nownum - firstnum) / 10)
                rlist[i+1] = lestnum
        maxnuml = totallen
        for i in range(totallen+1):
            nowindex = totallen-i
            if (rlist[nowindex]) != 0:
                maxnuml = nowindex
                break
        r = ''.join([str(i) for i in rlist[0:maxnuml+1]][::-1])
        return r
            
