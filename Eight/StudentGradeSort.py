'''
学生成绩排序（类与对象练习）
题目内容：
设计一个学生类(Student)，其中的数据成员有：字符串类型sname表示录入的学生姓名，整型值mscore代表学生的数学成绩，整型值cscore代表学生的语文成绩，整型值escore代表学生的英语成绩。
然后要求根据录入的学生成绩（各不相同），输出总分最高的学生姓名和各科目成绩。
'''
class Student:
    def __init__(self, sname, mscore, cscore, escore):
        self.sname = sname
        self.mscore = mscore
        self.cscore = cscore
        self.escore = escore
        self.total = mscore + cscore + escore
    def __lt__(self, other):
        return self.total<other.total
    def __str__(self):
        return '%s %d %d %d' %(self.sname, self.mscore, self.cscore, self.escore)

names = input().split()
mscores = list(map(int, input().split()))
cscore = list(map(int, input().split()))
escore = list(map(int, input().split()))
s = []
for i in range(len(names)):
    s.append(Student(names[i], mscores[i], cscore[i], escore[i]))
s.sort()
print(s[-1])

