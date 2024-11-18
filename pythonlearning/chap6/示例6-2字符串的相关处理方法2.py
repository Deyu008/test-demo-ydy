s='HelloWorld'
# 字符串的替换
new_s=s.replace('o','你好',1) # 最后一个参数是替换次数,默认是全部替换
print(new_s)

# 字符串在指定的宽度范围居中
print(s.center(20))
print(s.center(20,'*')) # 剧中后,空的地方用*填充

# 去掉字符串左右的空格
s='    Hello    World    '
print(s.strip())
print(s.lstrip()) # 只去掉左边的空格
print(s.rstrip()) # 只去掉右边的空格

# 去掉指定的字符
s3='dl-Helldoworld'
print(s3.strip('ld')) # 与顺序无关,把ld和dl都去掉了
print(s3.lstrip('ld')) # 去掉左侧出现的第一个ld
print(s3.rstrip('dl')) # 去掉右侧出现的第一个ld


