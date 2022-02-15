'''
7-10 统计指定数量学生的平均成绩与不及格人数 (10 分)
本题要求编写程序，计算学生们的平均成绩，并统计不及格（成绩低于60分）的人数。题目保证输入与输出均在双精度范围内。

输入格式:
输入在第一行中给出非负整数n，即学生人数。第二行给出n个非负实数，即这n位学生的成绩，其间以空格分隔。

输出格式:
average = 成绩均值

count = 不及格人数

其中平均值精确到小数点后两位，等号的左右各有一个空格。

输入样例1:
4
60 54 95 73
输出样例1:
average = 70.50
count = 1
输入样例2:
0
输出样例2:
average = 0.00
count = 0
'''
n=int(input())
if n==0:
    print("average = 0.00")
    print("count = 0")
    exit(0)
else:
    c=0
    s=list(map(int,input().split()))
    average=sum(s)/n
    for ch in s:
      if ch<60:
        c=c+1
print("average = %.2f"%average)
print("count = %d"%c)
