'''
6-4 使用函数求素数和 (20 分)
使用函数求素数和

prime(p), 其中函数prime当用户传入参数p为素数时返回True，否则返回False. PrimeSum(m,n),函数PrimeSum返回区间[m, n]内所有素数的和。题目保证用户传入的参数1<=m<n。

函数接口定义：
在这里描述函数接口：
prime(p)，返回True表示p是素数，返回False表示p不是素数
PrimeSum(m,n)，函数返回素数和
裁判测试程序样例：

/* 请在这里填写答案 */

m,n=input().split()
m=int(m)
n=int(n)
print(PrimeSum(m,n))
输入样例：
在这里给出一组输入。例如：

1 10
输出样例：
在这里给出相应的输出。例如：

17
'''
def PrimeSum(m,n):
    s=0
    if m==1:
        m+=1
    for i in range(m,n):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            s=s+i
    return s
    