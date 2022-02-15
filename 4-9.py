'''
7-9 jmu-python-偶数之积 (10 分)
求1到n中所有偶数的积。

输入格式:
输入整数n。

输出格式:
1到n中偶数积。

输入样例:
5
输出样例:
8
'''
n=int(input())
p=1
for i in range(1,n+1):
    if i%2==0 :
       p=p*i
       i=i+1
print(p)
