#!/usr/bin/env python3
import os
import sys
__doc__='''
一个简单的脚本，模拟tree命令，但没有tree命令的功能那么多。
列举目录下的所有文件，目录，和软链接以及软链接所指向的文件
或目录一并打印，如果软链接所指向的是一个目录，则把那个目录
下的目录，文件和列表一起列出。
'''

def filetest(num1,filename):
    if os.path.isfile(filename):
        tm = '|   ' * num1
        order_filename = os.path.split(filename)[-1]
        print(tm + '|---' + order_filename)
def linktest(num1,filename):
    if os.path.islink(filename):
        orthers= os.readlink(filename)
        orther_filename = os.path.split(filename)[-1]
        tm = '|   ' * num1
        num2 = num1 + 1
        print(tm + '|---' + orther_filename + ' -> '+ orthers)
        if os.path.isdir(orthers):
            total_dir_file = os.listdir(orthers)
            #print(total_dir_file)
            for i in total_dir_file:
                filenames = os.path.join(orthers,i)
                #print(filenames)
                if os.path.islink(filenames):
                    linktest(num2,filenames)
                elif os.path.isfile(filenames):
                    filetest(num2,filenames)
                elif os.path.isdir(filenames):
                    dirtest(num2,filenames)
def dirtest(num1,filename):
    if os.path.isdir(filename):
        if num1 != -1:
            tm = '|   ' * num1
        num2 = num1 + 1
        order_filename = os.path.split(filename)[-1]
        if num1 != -1:
            print(tm + '|---' + order_filename)
        else:
            print(order_filename )
        total_dir_file = os.listdir(filename)
        #print(total_dir_file)
        for i in total_dir_file:
            filenames = os.path.join(filename,i)
            #print(filenames)
            if os.path.islink(filenames):
                linktest(num2,filenames)
            elif os.path.isfile(filenames):
                filetest(num2,filenames)
            elif os.path.isdir(filenames):
                dirtest(num2,filenames)
if __name__ == '__main__':
    if len(sys.argv) == 1:
        dirtest(-1,'.')
    else:
        if '--help' in sys.argv:
            print('python3 tree.py <directory list>')
        elif '--version' in sys.argv:
            print('tree-deta 0.0.1')
        else:
            for i in sys.argv[1:]:
                if i[0] == '~':
                    i = os.path.expanduser(i)
                dirtest(-1,i)
                print('')
