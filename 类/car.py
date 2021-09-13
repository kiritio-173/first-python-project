# 日期 : 2021/9/7
# 时间 : 16:05
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


'''my_new_car=Car('aodi','a6',2016)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometers(20000)
print(my_new_car.odometers_reading)

my_new_car.increment_odometer(100)
print(my_new_car.odometers_reading)'''