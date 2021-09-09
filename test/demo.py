# 日期 : 2021/8/12
# 时间 : 21:36
# 作者 : kiritio
#会员m>=200八折 100 九折 否则不打折
#非m>=200 九五折，否则不打折

answer=input('是否为会员  y/n')
m=int(input("消费金额为："))
if answer=='y':
    if m>=200:
        w=0.8*(m-200)+190
        print("此时的价格为：",w)
    elif 100<=m<=200:
        w=0.9*(m-100)+100
        print("此时的价格为：", w)
    elif 0<=m<=100:
        w=m
        print("此时的价格为：", w)
    else:
        print("价格错误！")
elif answer=='n':
    if m>=200:
        w=0.9*(m-200)+200
        print("此时的价格为：", w)
    elif 0 <= m <= 200:
        w = m
        print("此时的价格为：", w)
    else:
        print("价格错误！")