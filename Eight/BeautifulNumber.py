'''
"精致"的数
题目内容：
给定两个非负整数x和y，如果某一整数等于x^i+y^j，其中整数i>= 0且j>=0，那么我们认为该整数是一个"精致"的数。返回值小于或等于n(n<=200)的所有精致的数组成的列表。
结果列表中每个值最多出现一次，同时请使用sorted保证结果唯一。
'''
x,y,n = int(input()), int(input()), int(input())
def select(x, y, n):
    r = set()
    for i in range(n):
        for j in range(n):
            l = x ** i + y ** j
            if l <= n:
                r.add(l)
    return sorted(r)

print(select(x, y, n))