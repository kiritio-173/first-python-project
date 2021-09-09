# 日期 : 2021/8/26
# 时间 : 20:35
# 作者 : kiritio
lst=[1,2,3,4,5,6]
#添加元素append添加元素为单个
lst.append(10)
print(lst)
lst2=['hello','world']
lst.append(lst2)
print(lst)#[1, 2, 3, 4, 5, 6, 10, ['hello', 'world']],将列表当作元素；
print('--------------------------')
lst.extend(lst2)
print(lst)#[1, 2, 3, 4, 5, 6, 10, ['hello', 'world'], 'hello', 'world']将元素分别加入；

'''append添加一个ID；extend添加一组ID'''
lst[1:2:]=lst2
print(lst)