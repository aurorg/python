'''
7-5 求分数序列前N项和 (10 分)
本题要求编写程序，计算序列 2/1+3/2+5/3+8/5+... 的前N项之和。注意该序列从第2项起，每一项的分子是前一项分子与分母的和，分母是前一项的分子。

输入格式:
输入在一行中给出一个正整数N。

输出格式:
在一行中输出部分和的值，精确到小数点后两位。题目保证计算结果不超过双精度范围。

输入样例:
20
输出样例:
32.66

'''
a=int(input())
s=0
i=2
j=1
for b in range (a):
     s=s+i/j
     i=i+j
     j=i-j
print("%.2f"%s)
 