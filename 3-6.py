'''
7-6 象限的判断 (10 分)
输入一对坐标，输出它在直角坐标系中的象限。

象限的判断.JPG

输入格式:
输入坐标(x,y)，（假设输入的x或y坐标值一定不会为0）如：(3.5,-2)。

输出格式:
输出对应的象限，如：第四象限

输入样例:
在这里给出一组输入。例如：

(3.5,-2)
输出样例:
在这里给出相应的输出。例如：

第四象限
'''
x,y = eval((input("")))
if x>0 and y>0:
    print("第一象限")
elif x<0 and y>0:
    print("第二象限")
elif x<0 and y<0:
    print("第三象限")
else:
    print("第四象限")
          