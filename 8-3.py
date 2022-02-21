'''
6-3 jmu-python-计算薪资 (15 分)
某公司销售员底薪为5000，销售业绩与利润提成的关系如下表所示（计量单位：元）

看+pta

编写函数，计算员工月薪。

函数接口定义：
bonus(sales)
其中 sales 是参数，表示员工的月销售业绩。

裁判测试程序样例：
/* 请在这里填写答案 */
sales=eval(input())
print("%.2f"%bonus(sales))
输入样例1：
50800
输出样例1：
15160.00
输入样例2：
35000
输出样例2：
10250.00
'''
def bonus(sales):
    if sales <= 10000:
        sales=5000
    if sales >10000 and sales <=20000:
        sales=5000+sales*0.1
    if sales >20000 and sales <=50000:
        sales=5000+sales*0.15
    if sales >50000 and sales <=100000:
        sales=5000+sales*0.2
    if sales >100000:
        sales=5000+sales*0.25
    return sales