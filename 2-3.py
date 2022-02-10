'''
7-4 sdut-计算分段函数 (20 分)
计算下列分段函数g(x)的值：

f(x)=0         x=0
f(x)=1/(2x)    x!=0

输入格式:
在一行中输入实数x。

输出格式:
在一行中按“g(x) = result”的格式输出，其中x与result都保留3位小数。

输入样例1:
500
输出样例1:
g(500.000) = 0.001
输入样例2:
0
输出样例2:
g(0.000) = 0.000
'''
a=float(input())
b=float()
if a!=0:
    b=(2*a)**(-1)
    print("g(%.3f) = %.3f"%(a,b))
else:
    b=0
    print("g(%.3f) = %.3f"%(a,b))
