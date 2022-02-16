'''
7-5 显示指定范围内的素数 (15 分)
输入整数m，将所有大于1小于整数m的素数存入所指定的数组中(数组最多只存放100个素数，超过则提示“OVERFLOW”)，输出各素数——若输入的m≤2，则提示“NO”，程序终止。注：素数(Prime Number)，亦称质数，指在一个大于1的自然数中，除了1和此整数自身外，没法被其他自然数整除的数。

输入格式:
输入一个非0的整数。

输出格式:
素数的输出格式为每个素数5列宽、右对齐、每行显示15个。

输入样例:
100
输出样例:
    2    3    5    7   11   13   17   19   23   29   31   37   41   43   47
   53   59   61   67   71   73   79   83   89   97
输入样例:
568
输出样例:
OVERFLOW
输入样例:
1
输出样例:
NO
'''
x=int(input())
arry=[]
s=0
if x<=2:
    print("NO")
else:
    for i in range(2,x):
        c=1
        for j in range(2,i):
            if i%j==0:
                c=0
                break
        if c==1:
            arry.append(i)
    if len(arry)>100:
            print("OVERFLOW")
    else:
        for i in range (0,len(arry)):
            d=arry[i]
            s=s+1
            print('%5d'%d,end='' )
            if s==15:
               s=0
               print("")
