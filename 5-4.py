'''
7-4 穷举问题-搬砖 (15 分)
某工地需要搬运砖块，已知男人一人搬3块，女人一人搬2块，小孩两人搬1块。如果想用n人正好搬n块砖，问有多少种搬法？

输入格式:
输入在一行中给出一个正整数n。

输出格式:
输出在每一行显示一种方案，按照"men = cnt_m, women = cnt_w, child = cnt_c"的格式，输出男人的数量cnt_m，女人的数量cnt_w，小孩的数量cnt_c。请注意，等号的两侧各有一个空格，逗号的后面也有一个空格。

如果找不到符合条件的方案，则输出"None"

输入样例:
45
输出样例:
men = 0, women = 15, child = 30
men = 3, women = 10, child = 32
men = 6, women = 5, child = 34
men = 9, women = 0, child = 36
'''
n=int(input())
c=0
for men in range(0,n+1):
    for women in range(0,n+1):
      for child in range(0,n+1):
          if men+women+child==n and men*3+women*2+child*0.5==n:
           c=1
           print("men = %d, women = %d, child = %d"%(men,women,child))
if(c==0):
  print("None")