# 日期 : 2021/8/12
# 时间 : 14:05
# 作者 : kiritio
fl=open('C:/Users/85495/Desktop/text.txt','a+')#a+为以读写的方式打开文件，没有则创建，有则添加。
print('hello world',file=fl)
fl.close()

#不进行换行输出用“,”隔开
print('hello\n\rworld')