#水仙花数是指一个n位数 (n≥3)，它的每个位上的数字的n次幂之和等于它本身。
#例如：153是一个“水仙花数”，因为 153 是个 3位数，而1**3+5**3+3**3==153。
#输入一个正整数max，输出100到max之间的所有水仙花数（包括max）。
x = int(input())
for s in range(100, int(x)+1):
    y = 0
    for n in range(len(str(s))):
        y += int(str(s)[n]) ** len(str(s))
    if s == y:
        print(s)