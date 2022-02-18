'''
7-3 找列表中最大元素的下标（高教社，《Python编程基础及应用》习题4-7 (10 分)
输入一个整数列表，找出整数列表中最大元素的下标，如果最大元素的个数超过1，那么请打印输出所有的下标。

输入格式:
数字1,数字2,数字3,....,数字n

输出格式:
下标1 下标2 ... 下标k

输入样例:
3,2,3
输出样例:
0
2
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