'''
6-8 使用递归法对整数进行因数分解，输出成其质因数相乘的形式。 (10 分)
本题要求实现一个函数，可将任一正整数分解为其质因数相乘的形式。

函数接口定义：
在这里描述函数接口。例如：
def factors(num):
num是用户传入的参数。 num的值是正整数。 注意：这里函数只有一个参数。

裁判测试程序样例：
在这里给出函数被调用进行测试的例子。例如：


你写的函数在这里


facs=[]
n=int(input())
factors(n)
result='*'.join(map(str,facs))
if n==eval(result):
    print(n,'='+result)
输入样例：
在这里给出一组输入。例如：

1001
输出样例：
在这里给出相应的输出。例如：

1001 =7*11*13
'''
def factors(n):
    for j in range (2,n):
        if n%j==0:
            facs.append(j)
            n=n//j
            return factors(n)
    facs.append(n)
facs=[]
n=int(input())
factors(n)
result='*'.join(map(str,facs))
if n==eval(result):
    print(n,'='+result)