# 日期 : 2021/9/10
# 时间 : 16:23
# 作者 : kiritio
'''将前几个程序文件中的功能整合到函数中，使得程序的结构更加清晰'''
import json
'''将greet_useer分解成了三个函数模块
分别为储存姓名，创建姓名，主程序'''
def get_store_username():#储存姓名模块，包含了储存过程中可能遇到的异常处理
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username=json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username
       # print('Hello!'+username+'!Nice to meet you!')

def get_new_username():#首次执行程序时的创建姓名模块，
    filename = 'username.json'
    username=input('Please enter your name:')
    with open(filename,'w') as f_obj:
        json.dump(username,f_obj)
    return username

def greet_user():#主程序
    username=get_store_username()
    if username:#若是首次执行程序get_store_username返回值为NONE为空自动执行else块
        print('Hello ' + username + '!Nice to meet you again!')
    else:
        username=get_new_username()
        print(username+"I'll origanized you next time!")

greet_user()
