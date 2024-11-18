# (1)初始化变量
i=0
while i<3:

    user_name=input('请输入用户名：')
    pwd=input('请输入密码：')

    if user_name=='ydy' and pwd=='888888':
        print('loging')

        i=8
    else:
        if i<2:
            print('用户名或密码不正确，您还有',2-i,'次机会')
        i+=1
# 单分支判断
if i==3: # 当用户名或密码输入三次不正确后，循环执行结束，i的最大值为3
    print('对不起，三次均错误')
