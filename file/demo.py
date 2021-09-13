# 日期 : 2021/9/8
# 时间 : 23:20
# 作者 : kiritio
with open('demo.txt') as file_demo:
    contents=file_demo.read()
    print(contents)#读取时会将所有的符号读取，换行符也不例外
    print('-----------------------------------')
    print(contents.rstrip())#.rstip()函数的作用是去掉数据末尾的空格

file_path='demo.txt'
with open(file_path) as fd:
    for i in fd:
        #print(i)
        print(i.rstrip())

print('------------------------------')

with open(file_path) as fd:
    lines=fd.readlines()
    whloe_line = ''
    for line in lines:
        whloe_line+=line.strip()
    print(whloe_line)
    print(len(whloe_line))