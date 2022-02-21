'''
6-2 使用函数求余弦函数的近似值 (15 分)
本题要求实现一个函数，用下列公式求cos(x)近似值，精确到最后一项的绝对值小于eps（绝对值小于eps的项不要加）：

看pta


函数接口定义：funcos(eps,x ),其中用户传入的参数为eps和x；函数funcos应返回用给定公式计算出来，保留小数4位。

函数接口定义：
函数接口:
funcos(eps,x ),返回cos(x)的值。
裁判测试程序样例：
在这里给出函数被调用进行测试的例子。例如：


/* 请在这里填写答案 */

eps=float(input())
x=float(input())
value=funcos(eps,x )
print("cos({0}) = {1:.4f}".format(x,value))
输入样例：
0.0001 -3.1
输出样例：
cos(-3.1) = -0.9991
'''
def fun(n):
    m=1
    if n==0:
        return m
    for j in range(1,n+1):
        m*=j
    return m
def funcos(eps,z):
    sum=0
    x=0
    m=1
    while True:
        y=z**x/fun(x)
        if y<eps:
            break
        else:
            sum+=m*y
            m=-m
        x=x+2
    return sum