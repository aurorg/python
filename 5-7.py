'''
7-7 泰勒展开式求sinx近似值 (10 分)
用泰勒展开式求sinx近似值的多项式为：

。

输入x求sinx的近似值，要求误差不大于0.00001。

输入格式:
直接输入一个实型数据。没有其它任何附加字符。

输出格式:
直接输出保留3位小数的实型结果。

输入样例:
2.5
输出样例:
0.598
'''
m=eval(input())
s=0
for i in range(1,10):
    a=1
    for j in range (1,2*i):
        a*=j
    b=(m**(2*i-1)/a)*((-1)**(i-1))
    s=s+b
print("%.3f"%(s))