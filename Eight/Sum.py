'''
两数求和问题
题目内容：
给定一个列表和一个整数目标，其中列表中的元素都为整数，要求返回列表中的两个元素的索引编号（以列表形式打印,为确保结果唯一，小的编号在前），使这两个元素的和为这个特定的目标。
(只对应确定的唯一一组解，并且不能使用同一个元素两次。)
'''
lst = list(map(int, input().split()))
s= int(input())
def select(lst, s):
    for a in lst:
        for b in lst:
            if a != b and s == a+b:
                return sorted([lst.index(a), lst.index(b)])
print(select(lst, s))