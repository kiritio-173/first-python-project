# 日期 : 2021/8/30
# 时间 : 15:18
# 作者 : kiritio

def greet_user():#def定义函数，其后为函数名
    '''显示问候语'''
    print('hello!')

greet_user()

def describe_pet(animal_type,pet_name):
    print("\nI have a "+animal_type+".")
    print("\nMy "+animal_type+"'s name is "+pet_name+".")

describe_pet('cat','ww')
print('--------------------------------------------')

def build_person(first_name,last_name,age=''):
    '''返回一个字典，其中包含有一个人的信息'''
    person={'first':first_name,'last':last_name}

    age=input('age?:')
    if age:
        person['age']=age
    return person
musician=build_person('jimi','hendrix',age=27)
print(musician)