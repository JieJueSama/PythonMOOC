'''
公式求值（10分）
题目内容：

接受一个正整数输入x，打印上述公式的输出值。
'''

from math import *
x = int(input())
y = sin(15/180*pi) + (e ** x - 5 * x) / sqrt(x ** 2 + 1) - log(3 * x)
print('%.10f'%y)