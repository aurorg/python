'''
6-6 编写函数，判断用户传入的列表长度并完成切片 (5 分)
编写一个函数，判断用户传入的列表长度是否大于2，如果大于2，只保留前两个，并将新内容返回给调用者。

函数定义：
def func(list1)
裁判测试程序样例：
/* 请在这里填写答案 */

print(func([1, 2, 3, 4]))
print(func([5, 6]))
输入样例：
无
输出样例：
在这里给出相应的输出。

[1, 2]
[5, 6]
'''
def func(list):
    l=len(list)
    if len(list)>2:
        a=[list[0],list[1]]
    else:
        a=list
    return a