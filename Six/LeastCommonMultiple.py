'''
求两个数的最小公倍数。
题目内容：
输入两个正整数num1和num2（不超过500），求它们的最小公倍数并输出。
最小公倍数：最小公倍数=两整数的乘积÷最大公约数
'''

#先求最大公约数
def gcd(num1, num2):
    if num2 == 0:
        return num1
    else:
        num3 = num1 % num2
        num1 = num2
        num2 = num3
        return gcd(num1, num2)

def lcm(num1, num2):
    num3 = gcd(num1, num2)
    return num1 * num2 // num3


num1=int(input(""))
num2=int(input(""))
print(lcm(num1,num2))

