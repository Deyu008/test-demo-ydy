for i in 'hello':
    if i=='e':
        break
    print(i)

print('-----------------------')
for i in range(3):
    user_name=input('user name:')
    pwd=input('password:')
    if user_name=='ydy' and pwd=='888888':
        print('loding')
        break
    else:
        if i<2:
            print('用户名不正确,您还有',2-i,'次机会')
else:
    print('三次均输入错误！')