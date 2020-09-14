'''
与7相关的数：如果一个正整数，它能被7整除或者它的十进制表示法中某个位数上的数字为7，则称之为与7相关的数。
题目内容：
现在我们给定一个正整数n（n<1000），求所有小于等于n的与7无关的正整数的平方和。
'''
n = int(input())
sum = 0
for num in range(1, n+1):
#先判断各个位数上有没有7
    flag = False
    for n in range(len(str(num))):
        test = str(num)[n]
        if int(str(num)[n]) == 7:
            flag = True
            break
    if flag == True:
        continue
#判断能否被7整除
    if num % 7 == 0:
        continue
    sum += num * num
print(sum)