'''
列表元素改写
题目内容：
输入一个列表alist，要求列表中的每个元素都为正整数且不超过10；
将列表中的奇数变为它的平方，偶数除以2后打印新的列表（新的列表中所有元素仍都为整数）。
'''
alist = list(input().split(' '))
length = len(alist)
num = 0
while num < length:
    if int(alist[num]) % 2 == 0:
        alist[num] = int(alist[num]) // 2
    else:
        alist[num] = int(alist[num]) ** 2
    num += 1
print(sorted(alist))