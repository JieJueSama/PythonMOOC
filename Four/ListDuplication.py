#输入两个列表alist和blist，要求列表中的每个元素都为正整数且不超过10；
#合并alist和blist，并将重复的元素去掉后输出一个新的列表clist。

alist = list(map(int,input().split()))
blist = list(map(int,input().split()))

new_list = set(alist + blist)
print(sorted(new_list))