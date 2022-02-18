'''7-1 合并两个列表并去重 (10 分)
输入两个列表alist和blist，要求列表中的每个元素都为正整数且不超过10； 合并alist和blist，并将重复的元素去掉后输出一个新的列表clist。 可以使用以下实现列表alist的输入： alist=list(map(int,input().split())) 同时为保证输出结果一致，请将集合内元素排序之后再输出。 如对于列表alist，可输出sorted(alist)。

输入格式: 共两行，每一行都用来输入列表中的元素值，以空格隔开(可能不至一个空格 ）。

输出格式： 共一行，以列表形式打印输出。

输入样例:
在这里给出一组输入。例如：

1 2 3
4 3 2
输出样例:
在这里给出相应的输出。例如：

[1, 2, 3, 4]
'''
alist=list(map(int,input().split()))
blist=list(map(int,input().split()))
print(sorted(list(set(alist+blist))))