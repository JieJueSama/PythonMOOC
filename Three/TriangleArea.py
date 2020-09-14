#由三角形的三边长，求其面积。
#规定：输入的三条边一定能构成三角形，不用进行判定。
#提示：a,b,c小于1000由三角形的三边a,b,c求面积可以用如下的公式：
#其中p=(a+b+c)/2
#面积=S=√[p(p-a)(p-b)(p-c)]

import math

a = int(input())
b = int(input())
c = int(input())
p = (a + b + c) / 2

s = math.sqrt(p * (p - a) * (p - b) * (p - c))
print("三角形的面积是%.2f" %s)