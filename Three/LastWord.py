#计算字符串最后一个单词的长度，单词以空格隔开。

s = str(input("输入单词，以空格隔开"))
new_s = s.split(' ')
length = len(new_s)
print(len(new_s[length - 1]))
