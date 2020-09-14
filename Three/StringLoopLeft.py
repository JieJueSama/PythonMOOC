#给定一个字符串S，要求把S的前k个字符移动到S的尾部，如把字符串“abcdef”前面的2个字符‘a’、‘b’移动到字符串的尾部，得到新字符串“cdefab”，称作字符串循环左移k位。
#输入一个字符串和一个非负整数N，要求将字符串循环左移N次。

s = str(input("输入一串英文字母"))
n = int(input("输入非负整数"))
new_s = s[n : len(s)]
wait_s = s[0 : n]
end_str = new_s.__add__(wait_s)
print(end_str)
