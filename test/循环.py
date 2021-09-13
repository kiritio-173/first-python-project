# 日期 : 2021/8/30
# 时间 : 15:01
# 作者 : kiritio
unconfirmed_uesrs=['alice','mike','john']
confirmed_users=[]

while unconfirmed_uesrs:
    confirmed_user=unconfirmed_uesrs.pop()
    print(unconfirmed_uesrs)
    print(confirmed_user+'通过验证')
    confirmed_users.append(confirmed_user)

for confirmed_user in confirmed_users:
    print(confirmed_user.title())
