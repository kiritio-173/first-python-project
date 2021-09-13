# 日期 : 2021/9/9
# 时间 : 19:01
# 作者 : kiritio
import re
file='a,b c d,f'
'''只需要用空格做分隔符则只用file.split()函数即可
若是需要多个分隔符，则需要引入re模块，使用re.split('分隔符|分隔符'，file)，来进行分割'''
a=re.split(' |,',file)
print(a)
print(len(a))