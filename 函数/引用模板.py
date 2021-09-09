# 日期 : 2021/9/6
# 时间 : 13:01
# 作者 : kiritio
#使用模板需要现将工作目录变为当前目录，然后将文件夹设置为源文件
import pizza#全部引用
from pizza import make_pizza#部分引用引用特定的函数

pizza.make_pizza(16,'pepperoni')
pizza.make_pizza(20,'mushrooms','green peppers','extra cheese')