# 日期 : 2021/8/27
# 时间 : 18:48
# 作者 : kiritio
favorite_languages={
    'jen':'python',
    'mick':'c',
    'edward':'c#',
    'phil':'python'
}

for name in sorted(favorite_languages.keys(),reverse=True):#倒序遍历
    print(name)
print('\n')
for name in sorted(favorite_languages.keys(),reverse=False):#正序遍历
    print(name)

print('-----------------------------------------------------')

