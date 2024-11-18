# 大小写转换
s1='Helloworld'
new_s2=s1.lower()
print(s1,new_s2)

new_s3=s1.upper()
print(new_s3)

# 字符串的分割
e_mail='ydy@123.com'
lst=e_mail.split('@')
print('邮箱名:',lst[0],'邮箱服务器域名:',lst[1])

#
print(s1.count('o')) # o在字符串s1中出现了两次

# 检索操作
print(s1.find('o')) # o在字符串s1中首次出现的位置
print(s1.find('1')) # -1,没有找到

print(s1.index('o'))
# print(s1.index('1')) # ValueError: substring not found     find命令没找到字符会回复-1,index命令会报错

# 判断前缀和后缀

print(s1.startswith('H'))
print(s1.startswith('P'))

print('demo.py'.endswith('.py')) # True
print('text.txt'.endswith('.txt')) # True

