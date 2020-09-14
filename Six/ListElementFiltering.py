'''
列表元素筛选
题目内容：
已知输入为一个列表，列表中的元素都为整数，我们定义元素筛选函数为foo，
功能是检查获取传入列表对象的所有奇数位索引（注意列表的索引是从0开始的）对应的元素，并将其作为新列表返回给调用者。
'''
def foo(alist):
    blist = []
    length = int(len(alist))
    for i in range(1, length, 2):
        blist.append(alist[i])
    return blist

alist=list(map(int,input().split()))
print(foo(alist))