# 日期 : 2021/8/27
# 时间 : 9:51
# 作者 : kiritio
#[i*i for i in range()]
lst=[i*i for i in range(1,7)]
print(lst)#[1, 4, 9, 16, 25, 36]；使用生成式需要列表中的元素有一定的规律
lst2=[i*2 for i in range(1,6)]
print(lst2)
lst3=[i for i in range(2,11,2)]
print(lst3)