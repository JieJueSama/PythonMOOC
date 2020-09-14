'''
约瑟夫环问题
题目内容：
已知n个人（以编号0，1，2，3...n-1分别表示）围坐在一张圆桌周围。
从编号为0的人开始报数1，数到m的那个人出列；他的下一个人又从1开始报数，数到m的那个人又出列；依此规律重复下去，直到圆桌周围的人全部出列。
'''

n = int(input())
m = int(input())
lst = list(range(n))
result = []
for i in range(n):
    for j in range(m-1):
        lst.append(lst.pop(0))
    result.append(lst.pop(0))
print(result)
