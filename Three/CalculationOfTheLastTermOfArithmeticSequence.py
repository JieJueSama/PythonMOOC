#给出一个等差数列的前两项a1，a2，求第n项是多少

a1 = int(input("请输入等差数列第一项："))
a2 = int(input("请输入等差数列第二项："))
n = int(input("要得到第几项："))
gap = a2 - a1
n = n - 2
end = a2 + n * gap
print(end)