'''
7-5 半圆弧的长度 (15 分)
输入圆的半径，求半圆弧的长度（使用math库的pi常量）

输入格式:
输入圆的半径，可以是小数，也可以是整数。

输出格式:
输出结果，要求面积保留2位小数。输出格式为：L=×××

输入样例:
在这里给出一组输入。例如：

2
输出样例:
在这里给出相应的输出。例如：

L=6.28
'''
import math
r = eval(input())
print("L=%.2f"%(r*math.pi)) 