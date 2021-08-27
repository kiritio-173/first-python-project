# 日期 : 2021/8/26
# 时间 : 23:18
# 作者 : kiritio
lst=[1,2,3,4,5,5,5,6,7]
lst.remove(5)#删除单个元素，有重复的删除第一个
print(lst)
lst.pop()#不指定位置则移除最后一个;其中这个lst.pop()的值为7.
print(lst.pop())
print(lst)#[1, 2, 3, 4, 5, 5, 6]
lst.pop(1)
print(lst)#[1, 3, 4, 5, 5, 6]
print('------------------切片删除--------------------')
lst[1:3]=[]#列表索引的范围为左闭右开[a,b)；
print(lst)
lst.clear()
print(lst)#[]，列表被清空
del lst
#print(lst),NameError: name 'lst' is not defined,列表被删除