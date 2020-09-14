'''
输入年月日，判断这一天是这一年的第几天？
题目内容：
给定年月日，如2019/1/8，打印输出这一天是该年的第几天
'''
from datetime import *

d = input()
d1 = datetime.strptime(d[:4] + '/1/1', '%Y/%m/%d')
d2 = datetime.strptime(d, '%Y/%m/%d')
print((d2 - d1).days + 1)