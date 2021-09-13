<<<<<<< HEAD
# 日期 : 2021/8/27
# 时间 : 9:37
# 作者 : kiritio
lst=[7,6,5,4,3,2,1]
print('sort前的列表',lst,id(lst))#[7, 6, 5, 4, 3, 2, 1] 2085866712704
lst.sort()
print('sort后的列表',lst,id(lst))#[1, 2, 3, 4, 5, 6, 7] 2085866712704;两列表id相同为同一个列表
lst.sort(reverse=True)
print(lst)#[7, 6, 5, 4, 3, 2, 1];指定reverse=True可以进行降序排列，同理False为升序；
print('-----------------还可以使用sorted内置函数--------------------')
decr_list=sorted(lst,reverse=True)#降序
print(decr_list)#升序同理
=======
# 日期 : 2021/8/27
# 时间 : 9:37
# 作者 : kiritio
lst=[7,6,5,4,3,2,1]
print('sort前的列表',lst,id(lst))#[7, 6, 5, 4, 3, 2, 1] 2085866712704
lst.sort()
print('sort后的列表',lst,id(lst))#[1, 2, 3, 4, 5, 6, 7] 2085866712704;两列表id相同为同一个列表
lst.sort(reverse=True)
print(lst)#[7, 6, 5, 4, 3, 2, 1];指定reverse=True可以进行降序排列，同理False为升序；
print('-----------------还可以使用sorted内置函数--------------------')
decr_list=sorted(lst,reverse=True)#降序
print(decr_list)#升序同理
>>>>>>> 7c42a3698e469b7170dbcb4ace1c4d125ee5b040
