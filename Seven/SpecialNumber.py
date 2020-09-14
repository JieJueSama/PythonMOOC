'''
特殊的数
题目内容：
一个特殊的正整数，它加上150后是一个完全平方数，再加上136又是一个完全平方数，求符合条件的最小的一个数。
'''

import math
n = 0
count = 0
while True:
    first = n + 100
    second = n + 168
    first_sqrt = int(math.sqrt(first))
    second_sqrt = int(math.sqrt(second))
    if (first_sqrt ** 2 == first) and (second_sqrt ** 2 == second):
        print(n)
        break
    n = n + 1