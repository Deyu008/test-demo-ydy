s='helloworldhelloworldadfdfdeoodllffe'
# (1)字符串拼接及not in
new_s=''
for item in s:
    if item not in new_s:
        new_s+=item # 拼接操作
print(new_s)


# (2)使用索引+not in
new_s2=''
for i in range(len(s)):
    if s[i] not in new_s2:
        new_s2+=s[i]
print(new_s2)

# (3)通过集合去重+列表排序'
new_s3=set(s)
lst=list(new_s3)
print(lst) # 顺序被打乱了,要先排序
lst.sort(key=s.index) # s.index后面不能接小括号,因为接了就是调用了
print(''.join(lst))
