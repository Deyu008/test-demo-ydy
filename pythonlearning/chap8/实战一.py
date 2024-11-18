import random
def get_max(lst):
    x=lst[0] # x存储的是元素的最大值，先假设lst[0]是最大值
    # 遍历
    for i in range(1,len(lst)):
        if lst[i]>x:
            x=lst[i] # 对最大值进行重新赋值
    return x

# 调用
lst=[ random.randint(1,100)  for item in range(10)]  # random.randint()用来控制随机数生成的范围, for item in range(10)用来控制生成多少个随机数
print(lst)
# 计算列表元素的最大值
max=get_max(lst)
print(max)
