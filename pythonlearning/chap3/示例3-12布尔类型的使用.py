x=True # True代表1，False代表0
print(x)
print(type(x))
print(x+10) # 11 ----> 1+10
print(False+10) # 10 ------> 0+10
print('---------------------------')
print(bool(18)) # 测试一下整数18的布尔值
print(bool(0),bool(0.0)) # 测试一下整数0和0.0的布尔值
# 总结，非0的整数的布尔值都是True
print(bool('北京欢迎你')) # Ture
print(bool('')) # False
# 总结，所有非空字符串的布尔值都是True
print(bool(False)) # False
print(bool(None)) # False
# 空字符串，空元组，空列表，空字典，空集合的布尔值都是False
