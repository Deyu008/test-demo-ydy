s=0 # 储存累加和
i=1
while i<11:

    s+=i
    if s>20:
        print('累加和大于20的当前数是:',i)
        break
    i+=1

print('------------------------')
i=0 # 统计登录的次数
while i<3:

    user_name=input('user name:')
    pwd=input('password:')
    if user_name=='ydy' and pwd=='888888':
        print('loding')
        break
    else:
        if i<2:
            print('用户名不正确,您还有',2-i,'次机会')
    i+=1
else:
    print('三次均输入错误!')