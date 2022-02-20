'''
7-4 jmu-python-重复元素判定 (20 分)
每一个列表中只要有一个元素出现两次，那么该列表即被判定为包含重复元素。
编写函数判定列表中是否包含重复元素，如果包含返回True，否则返回False。
然后使用该函数对n行字符串进行处理。最后统计包含重复元素的行数与不包含重复元素的行数。

输入格式:
输入n，代表接下来要输入n行字符串。
然后输入n行字符串，字符串之间的元素以空格相分隔。

输出格式:
True=包含重复元素的行数， False=不包含重复元素的行数
,后面有空格。

输入样例:
5
1 2 3 4 5
1 3 2 5 4
1 2 3 6 1
1 2 3 2 1
1 1 1 1 1
输出样例:
True=3, False=2
'''
x = int(input())
true = false = 0
for i in range(x):
    m = input()
    m = list(m.split())
    if len(list(m)) == len(set(m)):
        false +=1
    else:
        true +=1
print('True=%d, False=%d'%(true,false))