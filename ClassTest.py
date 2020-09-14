class Force:
    def __init__(self, x, y):
        self.fx, self.fy = x, y

    def show(self):
        print("Force<%s, %s>" % (self.fx, self.fy))

    def add(self, force2):
        x = self.fx + force2.fx
        y = self.fy + force2.fy
        return Force(x, y)

    __add__ = add

    def __str__(self):
        return "F<%s,%s>" % (self.fx, self.fy)

    def __mul__(self, n):
        x, y = self.fx * n, self.fy * n
        return Force(x, y)

    def __eq__(self, force2):
        return (self.fx == force2.fx) and (self.fy == force2.fy)

#生成一个力对象
f1 = Force(0, 1)
f1.show()

#生成另一个力对象
f2 = Force(3, 4)
#合成为新的力
f3 = f1.add(f2)
f3.show()