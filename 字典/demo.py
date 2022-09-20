# 日期 : 2021/8/27
# 时间 : 17:12
# 作者 : kiritio
user={}#添加新元素时需要一个创建一个新的空字典
user['username']='asuna'
user['age']=21
user['salary']='10k'
print(user)
for i,j in user.items():#字典本身不能直接用于循环，使用.items函数来完成对字典的遍历；
    print('\nKey:'+str(i))
    if i=='username':
        print('Value:'+str.title(j))
    else:
        print('Value:'+str(j))
print('-------------------------------------------------------')

for key in user.keys():#.keys()返回值为一个列表，包含了字典username中的所有的键值
    print(key)



