#输入一个列表，要求列表中的每个元素都为整数；
#将列表中的所有元素按照它们的绝对值大小进行排序，绝对值相同的还保持原来的相对位置，打印排序后的列表（绝对值大小仅作为排序依据，打印出的列表中元素仍为原列表中的元素）。

alist = list(map(int,input().split()))

print(sorted(alist, key=abs))