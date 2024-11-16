row=eval(input('请输入菱形的行数:'))
while row%2==0: # 判断行数的奇偶性,行数是偶数,重新输入行数
    print('请重新输入菱形行数!')
    row=eval(input('请输入菱形的行数:'))
# 输出菱形的
top_row=(row+1)//2 # 上半部分的行数
# 上半部分
for i in range(1,top_row+1):
    # 倒三角形
    for j in range(1,top_row+1-i):
        print(' ',end='')

    for k in range(1,i*2):
        if k==1 or k==i*2-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()

# 下半部分
bottom_row=row//2
for i in range(1,bottom_row+1):
    # 直角三角形
    for j in range(1,i+1):
        print(' ',end='')

    # 倒三角
    for k in range(1,2*bottom_row-2*i+2):
        if k == 1 or k == 2*bottom_row-2*i+2 - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()

