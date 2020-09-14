#输入一个列表，将其反转后输出新的列表。

alist = list(map(int,input().split()))
blist = reversed(alist)
for i in blist:
    print(i, end='')
