# 日期 : 2021/9/9
# 时间 : 18:22
# 作者 : kiritio
'''try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
  #  print(4/0)'''

print('please enter two words:')
print("enter 'q' to quit.")

while True:
    first_number=input('\nFirst number:')
    if first_number=='q':
        print('goodbey!')
        break
    seconed_number=input('\nSecond number:')
    try:
        answer=int(first_number)/int(seconed_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    except ValueError:#同时处理两个异常不可直接用两个try函数，需要在一个大的try函数下使用多个except函数。
        print('Please input at least one value')
    else:
        print(answer)
