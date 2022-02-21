'''
6-5 完数统计 (10 分)
完数定义：一个数的所有因子（包括1）之和等于它自身，这个数就是完数。比如6=1+2+3，6是完数。 本题要求编写程序,计算所有N位完数的个数与列表显示。

函数接口定义：
def wan(n):
在这里解释接口参数。n是一个大于0的正整数。表示几位数。

裁判测试程序样例：
import math

/* 请在这里填写答案 */

n=int(input())
x,lst=wan(n)
print(x)
print(lst)
输入样例：
在这里给出一组输入。例如：

2
输出样例：
在这里给出相应的输出。例如：

1
[28]
'''
import math
def wan(y):
    lst=[]
    c=0
    for n in range(int(math.pow(10,y-1)),int(math.pow(10,y))):
        s=1
        for i in range(2,n):
            if n % i==0:
                s=s+i
        if s==n:
            lst.append(s)
            c=c+1
    return c,lst
n=int(input())
x,lst=wan(n)
print(x)
print(lst)    