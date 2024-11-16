answer='y'
while answer=='y':
    print('---------------欢迎使用10086查询功能------------------')
    print('1.查询当前余额\n2.查询当前的剩余流量\n3.查询当前剩余的通话时长\n0.退出系统')
    num=eval(input('请输入您要执行的操作:'))
    if num==1:
        print('当前余额为234.5元')
    elif num==2:
        print('当前的剩余流量为4GB')
    elif num==3:
        print('当前剩余的通话时长为0分钟')
    elif num==0:
        print('程序退出,欢迎您下次使用')
        break
    else:
        print('对不起,您的输入有误,请重新输入!')
    answer=input('按任意键键退出,若您还需要继续查询请按y:')
else:
    print('程序退出,欢迎您下次使用')