'''
回文数判断
题目内容：
给一个5位数，判断它是不是回文数，是则输出yes，不是则输出no。
例如12321是回文数，它的个位与万位相同，十位与千位相同。
'''

n = int(input())
length = len(str(n))
num = 0
flag = True
while num < length // 2:
    if str(n)[num] != str(n)[length-num-1]:
        flag = False
    num += 1
if flag == True:
    print('yes')
else:
    print('no')