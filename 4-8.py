'''
7-8 求N的阶乘 (10 分)
本题要求编写程序，计算N的阶乘。

输入格式:
输入在一行中给出一个非负整数N（0≤N≤21）。

输出格式:
在一行中按照“product = F”的格式输出阶乘的值F，请注意等号的左右各有一个空格。题目保证计算结果不超过双精度范围。

输入样例:
5
输出样例:
product = 120
'''
n=int(input())
p=1
for i in range (1,n+1):
    p=p*i
    i=i+1
print("product = %d"%p)
