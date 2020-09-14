#接受一个由字母和数字组成的字符串，和一个字符，然后输出输入的字符串中含有该字符的个数。不区分大小写。

s = str(input("输入一个由字母和数字组成的字符串，和一个字符，以空格隔开:"))
new_s = s.split(' ')
first_str = new_s[0]
char = new_s[1]
num = 0
for letter in first_str:
    if char == letter:
        num += 1
print(num)