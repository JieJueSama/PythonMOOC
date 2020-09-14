'''
打印一个n层金字塔
题目内容：
打印一个n层（1<n<20）金字塔，金字塔由“+”构成，塔尖是1个“+”，下一层是3个“+”，居中排列，以此类推。
注意：每一行的+号之后均无空格，最后一行没有空格。
'''
n = int(input())
num = 1
while num <= n:
#控制输出空格
    for i in range(n - num):
        print(' ', end='')
#控制输出加号
    for i in range(2 * num - 1):
        print('+', end='')
    num += 1
    if num <= n:
        print('')