'''
打印一定范围内的素数
题目内容：
给定一个大于2的正整数n，打印出小于n（不包括n且n不大于100）的所有素数。
要求将符合条件的输出填入一个列表中，打印的结果为该列表。
'''
primeList = []
n = int(input())
for num in range(2, n):
    flag = False
    for i in range(2, num):
        if (num != i) and (num % i == 0):
            flag = True
    if flag:
        continue
    primeList.append(num)
print(primeList)
