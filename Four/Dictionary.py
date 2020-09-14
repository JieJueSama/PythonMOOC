#输入一个列表，要求列表中的每个元素都为正整数且列表包含的元素个数为偶数；
#将列表中前一半元素保存至字典的第一个键值1中，后一半元素保存至第二个键值2中。

alist = list(map(int,input().split()))
n = int(len(alist)/2)
be = alist[0:n]
af = alist[n:]
dic = {"1" : be, "2" : af}
print(dic)