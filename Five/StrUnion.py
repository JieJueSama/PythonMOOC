#输入两个字符串，输出两个字符串集合的并集。
#为保证输出结果一致，请将集合内元素排序之后再输出

str_1 = input()
str_2 = input()
str_1 = str_1.join(str_2)
unionStr = set(str_1)
finalStr = sorted(unionStr)
print(finalStr)

