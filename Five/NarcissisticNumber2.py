#水仙花数是指一个n位数 (n≥3)，它的每个位上的数字的n次幂之和等于它本身。
#例如：153是一个“水仙花数”，因为 153 是个 3位数，而1**3+5**3+3**3==153。
#输入一个正整数max，输出100到max之间的所有水仙花数（包括max）。
max1 = int(input())
for flower in range(100, max1 + 1):
    tally = 0
    length = 0
    a = flower
#判断整数位数
    while a != 0:
        length += 1
        a = a // 10
#判断水仙花数
    for y in range(length):
        tally += int(str(flower)[y]) ** length
    if tally == flower:
        print(flower)