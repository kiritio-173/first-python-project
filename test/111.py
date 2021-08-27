# 日期 : 2021/8/12
# 时间 : 17:35
# 作者 : kiritio
s=float(input("输入一个数："))
if s%2==0 :
    print(int(s),"为整数")
elif s%2==1 :
    print(int(s),"为奇数")
else :
    print(s,"不为整数")