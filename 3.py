'''
7-3 交换两个整数 (10 分)
输入两个整数，交换位置后输出。

输入格式:
在一行中用空格分隔输入两个整数a，b。

输出格式:
交换a，b的值后，按“a=? b=?”的格式输出

输入样例:
在这里给出一组输入。例如：

3 5
输出样例:
在这里给出相应的输出。例如：

a=5 b=3
'''
a,b=map(int,input().split())#输入空格的形式
t=a
a=b
b=t
print("a=%d b=%d"%(a,b))