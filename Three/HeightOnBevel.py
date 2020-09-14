#输入直角三角形两直角边a,b的值，输出斜边上的高


import math

a = int(input("输入a直角边的长度"))
b = int(input("输入b直角边的长度"))
c = math.sqrt(a ** 2 + b ** 2)
end = round(a * b / c, 2)
print(end)