'''
斐波拉契数列：这个数列从第三项开始，每一项都等于前两项之和。
'''
n = int(input())

def fbnq(n):
    a, b = 1, 1
    i = 0
    list = [a, b]
    while i < n:
        list.append(list[-1] + list[-2])
        i += 1
    return list
print(fbnq(n-2)[-1])