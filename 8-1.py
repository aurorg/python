'''
6-1 jmu-java&python-统计字符个数 (15 分)
编写程序统计1行字符串中：

不同字符的个数。
每种字符出现的次数。
函数接口定义：
Freq(line) 
函数功能：该函数统计不同字符出现的次数，并最后按照字符升序进行输出。输出格式见输出样例。
参数说明：line为需要统计的字符串。

裁判测试程序样例：
/* 请在这里填写答案 */
line = input()
Freq(line)
输入样例：
abc 123 adex!!!
输出样例：
11
  = 2
! = 3
1 = 1
2 = 1
3 = 1
a = 2
b = 1
c = 1
d = 1
e = 1
x = 1
输出格式说明：
第1行输出不同字符的个数。
**=**两边应有空格。
上述输出样例中第2行的字符是空格。
输出按照字符升序排列。
'''
def Freq(line):
    a={}
    m=set(line)
    n=list(m)
    y=len(n)
    print(y)
    for ch in m:
        strlen=line.count(ch)
        a[ch]=strlen
    items=list(a.items())
    items.sort(key=lambda x:x[0])
    for j in range(y):
        key, val = items[j]
        print("{} = {}".format(key,val))