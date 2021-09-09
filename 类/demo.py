# 日期 : 2021/9/7
# 时间 : 10:06
# 作者 : kiritio
class Dog():
    '''第一次模拟小狗的简单尝试'''

    def __init__(self,name,age):
        '''初始化属性姓名和年龄'''
        self.name=name
        self.age=age

    def sit(self):
        '''模拟小狗被命令时蹲下'''
        print(self.name.title()+" is now sitting.")

    def roll_over(self):
        '''模拟小狗打滚'''
        print(self.name.title()+" roll over!")

my_dog=Dog('willie',6)
print("My dog's name is "+my_dog.name.title()+'.')
print(my_dog.name.title()+' is '+str(my_dog.age)+' years old')

my_dog.sit()
my_dog.roll_over()