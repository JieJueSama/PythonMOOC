'''
求两个数的最大公约数
题目内容：
输入两个正整数num1和num2（不超过1000），求它们的最大公约数并输出。
'''
#欧几里得算法
def hcf(num1, num2):
    if num2 == 0:
        return num1
    else:
        num3 = num1 % num2
        num1 = num2
        num2 = num3
        return hcf(num1, num2)


num1=int(input(""))
num2=int(input(""))

a = hcf(num1,num2)
print(a)