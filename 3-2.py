'''
7-2 骑车还是走路？ (15 分)
在校园里，没有自行车，上课办事会很不方便。但实际上，并非去办任何事情都是骑车快。因为骑车总要找车、开锁、停车、锁车等，这要耽误一些时间。假设找到自行车，开锁并骑上自行车的时间为27秒；停车锁车的时间为23秒；步行每秒行走1.2米，骑车每秒行走3.0米。 编写程序判断走不同的距离去办事，是骑车快还是走路快。

输入格式:
输入一个数，表示距离

输出格式:
如果输入的距离骑车快，输出"Bike"；如果是走路快，输出"Walk"；如果一样快，输出"All"。

输入样例:
120
输出样例:
Bike

'''
n=eval(input())
t1=27+23+n/3.0
t2=n/1.2
if t1<t2:
    print("Bike")
elif t1==t2:
    print("All")
else:
    print("Walk")