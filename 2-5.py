'''
7-6 温度转换 (20 分)
温度刻画存在不同体系，摄氏度以1标准大气压下水的结冰点为0度，沸点为100度，将温度进行等分刻画。华氏度以1标准大气压下水的结冰点为32度，沸点为212度，将温度进行等分刻画。

根据华氏和摄氏温度定义，转换公式如下：

C = ( F – 32 ) / 1.8 F = C * 1.8 + 32

输入格式:
输入一个实数表示温度，后面的字母表示温度体系：F或f表示华氏温度，而C或c表示摄氏温度，实数与字母间无分隔符。

输出格式:
输出转换后的温度(保留两位小数，且后面有温度体系说明符，大写字母表示）；若输入的数据格式有误（未有效标示温度体系），输出Error

输入样例:
在这里给出一组输入。例如：

36.8C
输出样例:
在这里给出相应的输出。例如：

98.24F
输入样例:
在这里给出一组输入。例如：

10f
输出样例:
在这里给出相应的输出。例如：

-12.22C
输入样例:
在这里给出一组输入。例如：

78.2#
输出样例:
在这里给出相应的输出。例如：

Error
'''
a=input()
if a[-1] in ['F','f']:
    C=(eval(a[0:-1])-32)/1.8
    print('%.2fC'%C)
elif a[-1] in ['C','c']:
    F=1.8*eval(a[0:-1])+32
    print('%.2fF'%F)
else :
    print('Error')