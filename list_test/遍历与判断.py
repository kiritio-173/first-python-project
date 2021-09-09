<<<<<<< HEAD
# 日期 : 2021/8/26
# 时间 : 20:23
# 作者 : kiritio
print('p' in 'python')#true
print('k' in 'python')#false

lst=[10,20,'ok','python']
print('l'in lst)#f

print(10 in lst)#T；not in 为F
print('-----------------------------------------')

for i in lst:
    print(i)
print('-----------------遍历操作--------------------')
lst2=[1,2,3,4,5,6,7,8,9]
a=lst2[:]
=======
# 日期 : 2021/8/26
# 时间 : 20:23
# 作者 : kiritio
print('p' in 'python')#true
print('k' in 'python')#false

lst=[10,20,'ok','python']
print('l'in lst)#f

print(10 in lst)#T；not in 为F
print('-----------------------------------------')

for i in lst:
    print(i)
print('-----------------遍历操作--------------------')
lst2=[1,2,3,4,5,6,7,8,9]
a=lst2[:]
>>>>>>> 7c42a3698e469b7170dbcb4ace1c4d125ee5b040
print(a)#[1, 2, 3, 4, 5, 6, 7, 8, 9],[:]遍历了整个列表，相当于复制了列表；