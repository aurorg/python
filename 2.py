'''
7-2 求圆面积 (15 分)
输入圆的半径，求圆的面积（使用math库的pi常量）

输入格式:
输入圆的半径，可以是小数，也可以是整数。

输出格式:
输出结果，要求面积保留2位小数。输出格式为：圆面积是×××

输入样例:
在这里给出一组输入。例如：

2
输出样例:
在这里给出相应的输出。例如：

圆面积是12.57
'''
import math
r = eval(input())
print("圆面积是%.2f"%(r**2*math.pi)) 