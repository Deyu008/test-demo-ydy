# 三行四列
for i in range(1,4):
    for j in range(1,5):
        print('*',end='') # 结束符为空，不换行
    print() # 用于换行

print('-'*20)

# 直角三角形
for i in range(1,6):
    for j in range(1,i+1):
        print('*',end='')
    print()