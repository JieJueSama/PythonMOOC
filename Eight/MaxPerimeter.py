'''
最大的周长
题目内容：
给定一个列表alist，alist由一些正整数（代表长度）组成，返回由alist中的三个长度组成的有效三角形的最大周长。如果所有的长度组合都不能构成有效三角形，则返回 0。
'''
lst = list(map(int, input().split()))
def select(lst):
    tmax = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            for k in range(j+1, len(lst)):
                tri = sorted([lst[i], lst[j], lst[k]])
                if tri[0] + tri[1] > tri[2] and sum(tri) > tmax:
                    tmax = sum(tri)
    return tmax
print(select(lst))