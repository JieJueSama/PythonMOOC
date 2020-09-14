class Car:
    def __init__(self, name):
        self.name = name
        self.remain_mile = 0

    #加燃料里程
    def fill_fuel(self, miles):
        self.remain_mile = miles

    #跑miles英里
    def run(self, miles):
        print(self.name, end=': ')
        if self.remain_mile >= miles:
            self.remain_mile -= miles
            print("run %d miles!" % (miles,))
        else:
            print("fuel out!")

class GasCar(Car):

    #名称和排量
    def __init__(self, name, capacity):
        super().__init__(name) #父类初始化方法，只有名称
        self.capacity = capacity #增加了排量属性

    #加汽油gas升
    def fill_fuel(self, gas):
        #每升跑6英里
        self.remain_mile = gas * 6.0

class ElecCar(Car):
    #充电power度
    def fill_fuel(self, power):
        #每度电跑3英里
        self.remain_mile = power * 3.0


gcar = GasCar("BWM")
gcar.fill_fuel(50.0)
gcar.run(200.0)


ecar = ElecCar("Tesla")
ecar.fill_fuel(60.0)
ecar.run(200.0)