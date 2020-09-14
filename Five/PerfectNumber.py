'''
打印完数：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如 6 = 1＋2＋3。
题目内容：
输入一个正整数n（n<1000），输出1到n之间的所有完数（包括n）。
'''
n = int(input())

for num in range(1,n+1):
    factor = 1
    sum = 0
    while factor < num:
        if num % factor == 0:
            sum += factor
        factor += 1
    if sum == num:
        print(num)