class Student:
    def __init__(self, name, grade):
        self.name, self.grade = name, grade

    #内置sort函数只引用 < 比较符来判断前后
    def __lt__(self, other):
        #成绩比other高的，排在他前面
        return self.grade > other.grade
        return self.grade > other.grade

    #Student的易读字符串表示
    def __str__(self):
        return "(%s, %d)" % (self.name, self.grade)

    #Student的正式字符串表示，我们让它跟易读表示相同
    __repr__ = __str__

# 构造一个Python list对象
s = list()

#添加Student对象到List中
s.append(Student("Jack", 80))
s.append(Student("Jane", 75))
s.append(Student("Smith", 82))
s.append(Student("Cook", 90))
s.append(Student("Tom", 70))
print("Original:", s)

# 对List进行排序，注意这是内置sort方法
#实际上调用__lt__方法
s.sort()

#查看结果，已经按照成绩排好序了
print("Sorted:", s)