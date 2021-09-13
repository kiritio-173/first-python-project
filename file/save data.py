# 日期 : 2021/9/10
# 时间 : 10:53
# 作者 : kiritio
import json

filename='username.json'
try:
    with open(filename) as file_object:
        username=json.load(file_object)
except FileNotFoundError:
    username = input('please input your name:')
    with open(filename,'w') as file_object:
        json.dump(username,file_object)
        print('I will remember you next time!')
else:
    print('Hello!'+username)

