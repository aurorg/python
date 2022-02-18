'''
7-4 列表插入 (14 分)
输入一个字符串 s 和一个非负整数 i, 列表 ls = ['2', '3', '0', '1', '5']，在指定的位置 i 和 列表末尾分别插入用户输入的字符串 s。当 i >=5 时，相当于在列表末尾插入两次字符串 s 。

输入格式:
第一行输入一个字符串

第二行输入一个非负整数

输出格式:
插入新数据后的列表

输入样例:
在这里给出一组输入。例如：

a
2
输出样例:
在这里给出相应的输出。例如：

['2', '3', 'a', '0', '1', '5', 'a']
'''
alist=list(map(int,input().split(',')))
max=alist[0]
for i in range(len(alist)):
    if alist[i]>max:
        max=alist[i]
        m=i
for j in range(len(alist)):
           if alist[j]==max:
               m=j
               print(j)
        