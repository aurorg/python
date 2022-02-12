'''
7-7 jmu-python-回文数判断（5位数字） (10 分)
本题目要求输入一个5位自然数n，如果n的各位数字反向排列所得的自然数与n相等，则输出‘yes’，否则输出‘no’。

输入格式:
13531

输出格式:
yes

输入样例1:
13531
输出样例1:
yes
输入样例2:
13530
输出样例2:
no
'''
n = int(input())
s = 0
t=n
while t>0:
    s *= 10
    s += t%10
    t //= 10
if n == s:
    print("yes")
else:
     print("no")