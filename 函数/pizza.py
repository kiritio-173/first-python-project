# 日期 : 2021/9/6
# 时间 : 12:51
# 作者 : kiritio
def make_pizza(size,*toppings):
    '''介绍索要制作的披萨'''
    print("\nMaking a "+str(size)+"-inch pizza with the following toppings:")
    for topping in toppings:
        print('-'+topping)