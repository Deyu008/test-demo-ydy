# 个数可变的位置参数
def fun(*para): # 个数可变的位置参数是在参数前加一颗星，调用时可接受到的任意个数的实际参数，并放到一个元组中 *
    print(type(para))
    for item in para:
        print(item)

# 调用
fun(10,20,30,40)
fun(10)
fun(20,30)
fun([11,22,33,44]) # 实际上传递的是一个参数，
 # 在调用时，参数前加一颗星，会将列表进行解包
fun(*[11,22,33,44])

# 个数可变的关键字参数
def fun2(**kwpara): # 个数可变的关键字参数是在参数前面加两颗星，调用时可接受任意多个“参数=值”形式的参数，并放到一个字典中 *
    print(type(kwpara))
    for key,value in kwpara.items():
        print(key,'-----',value)

# 调用
fun2(name='娟子姐',age=18,height=170) # 关键字参数

d={'name':'娟子姐','age':18,'height':170}
#fun2(d) # TypeError: fun2() takes 0 positional arguments but 1 was given

fun2(**d) #系列解包操作
