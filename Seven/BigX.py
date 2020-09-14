'''
大大的叉
题目内容：
打印出n阶的“叉”，这个叉图案由字符‘+’和‘X’构成，n越大，这个图案也就越大
'''
n = int(input())
for i in range(0, 2 * n - 1):
    for m in range(0, 2 * n - 1):
        if m == i or m == 2 * n - 2 - i:
            print('X', end='')
        else:
            print('+',end='')
    print()