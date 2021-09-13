# 日期 : 2021/9/8
# 时间 : 15:13
# 作者 : kiritio

class Car():
    '''一次模拟汽车的简单尝试'''

    def __init__(self,style,model,year):
        self.style=style
        self.model=model
        self.year=year
        self.odometers_reading=0

    def get_descriptive_name(self):
        wholename=self.style+' '+self.model+' '+str(self.year)
        return wholename

    def update_odometers(self,mileage):
        '''将里程表设置为指定值'''
        if mileage >= self.odometers_reading:
            self.odometers_reading+=mileage
        else:
            print('无法将数值回调')

    def increment_odometer(self,miles):
        '''miles为增加的里程数'''
        if miles>=0:
            self.odometers_reading+=miles
        else:
            print('请输入有效的里程')

class ElectricCar(Car):
    '''电动车类的独特之处'''

    def __init__(self,style,model,year):
        '''初始化父类属性'''
        super().__init__(style,model,year)#super()是一个特殊的函数，将子类与父类联系起来，相当于将父类中的目标属性复制到子类中
        self.battery_size=80#这个属性在Car大类中不存在，只存在于子类中

    def get_battery_size(self):
        print('This car has a '+str(self.battery_size)+'kwh battery')


my_tesla=ElectricCar('tesla','model Y',2020)#调用类中的函数或者变量时需要用变量.function()的格式
print(my_tesla.get_descriptive_name())
my_tesla.get_battery_size()