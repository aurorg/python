'''
7-2 三角形判定并计算面积 (20 分)
请根据给定的三条边长a、b、c判断能否构成三角形，若能构成三角形则计算出它的面积。（提示：三角形面积=sqrt(s(s-a)(s-b)(s-c)），其中s=(a+b+c)/2。)

输入格式:
在一行内输入三个正整数表示三条边长，中间用空格分隔。

输出格式:
若能构成三角形则输出其面积，保留2位小数，否则输出"Not A Valid Triangle!"。

输入样例1:
在这里给出一组输入。例如：

3 4 5
输出样例1:
在这里给出相应的输出。例如：

area=6.00
输入样例2:
在这里给出一组输入。例如：

3 2 1
输出样例2:
在这里给出相应的输出。例如：

Not A Valid Triangle!
'''
a,b,c= map(int,input().split())
s=(a+b+c)/2
if a+b>c and a+c>b and b+c>a:
    x=s-a
    y=s-b
    z=s-c
    area=(s*x*y*z)**0.5
    print("area=%.2f"%(area))
else:
    print("Not A Valid Triangle!")