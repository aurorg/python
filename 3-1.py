'''
7-1 企业根据利润提成发放奖金问题 (15 分)
企业根据利润提成发放奖金问题。利润低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%； 20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%； 60万到100万之间时，高于60万元的部分，可提成1.5%； 高于100万元时，超过100万元的部分按1%提成。从键盘输入当月利润，求应发放奖金总数？

输入格式:
输入一个利润整数。例如：输入120000。

输出格式:
输出一个实数。例如：11500.0。

输入样例:
在这里给出一组输入。例如：

120000
输出样例:
在这里给出相应的输出。例如：

11500.0
'''
w=float(input())
if w<=0:
   j=0
   print("0")
elif w>0 and w<=100000:
  j=w*0.1
  print("%.1f"%(j))
elif w>100000 and w<200000:
  j=100000*0.1+(w-100000)*0.075
  print("%.1f"%(j))
elif w>200000 and w<400000:
  j=100000*0.1+100000*0.075+(w-200000)*0.05
  print("%.1f"%(j))
elif w>400000 and w<600000:
  j=100000*0.1+100000*0.075+200000*0.05+(w-400000)*0.03
  print("%.1f"%(j))
elif w>600000 and w<1000000:
  j=100000*0.1+100000*0.075+200000*0.05+200000*0.03+(w-600000)*0.015
  print("%.1f"%(j))  
else:
  j=100000*0.1+100000*0.075+200000*0.05+200000*0.03+400000*0.015+(w-1000000)*0.01
  print("%.1f"%(j))