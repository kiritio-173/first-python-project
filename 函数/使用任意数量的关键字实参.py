# 日期 : 2021/9/6
# 时间 : 11:05
# 作者 : kiritio
def build_profile(first,last,**user_info):
    '''**代表的是建立一个空的字典，用于你知道需要从外部接收信息但是不知道信息的类型'''
    profile={}
    profile['fiestname']=first
    profile['lastname']=last
    for key,value in user_info.items():#遍历所输入的字典格式的变量，将其整合到上述创建的新字典中.
        #print(key,value)
        profile[key]=value
   # print(profile)
    return profile
user_profile=build_profile('albert','einstein',location='princeton',field='physics')
print(user_profile)