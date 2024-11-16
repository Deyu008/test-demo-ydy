# (1)创建字典
d={10:'cat',20:'dog',30:'pet',20:'zoo'}
print(d) # key相同时,value值进行覆盖

# (2)zip函数
lst1=[10,20,30,40]
lst2=['cat','dog','pet','zoo','cat']
zipobj=zip(lst1,lst2)
print(zipobj) # <zip object at 0x000001BBCB623FC0>
# print(list(zipobj)) # 转成列表类型 ---> [(10, 'cat'), (20, 'dog'), (30, 'pet'), (40, 'zoo')]
d=dict(zipobj) # 转成字典形式
print(d) # {10: 'cat', 20: 'dog', 30: 'pet', 40: 'zoo'}

# 使用参数创建字典
d=dict(cat=10,dog=20) # 左侧cat时key,右侧的时value
print(d)

t=(10,20,30) # 元组
print({t:10}) # t时key,10是value,元组是可以作为字典中的key

# lst=[10,20,30] # 列表
# print({lst:10}) #TypeError: unhashable type: 'list'          列表是可变数据类型,不能作为字典的键(key)

# 字典属于序列
print('max:',max(d))
print('min:',min(d))
print('len:',len(d))
# 字典的删除
del d
# print(d)
