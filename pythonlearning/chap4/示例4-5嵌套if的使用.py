answer=input('请问，您喝酒了吗？')
if answer=='y': # answer的值为y表示喝酒了
    proof=eval(input('请输入酒精含量:'))
    if proof<20:
        print('well')
    elif proof<80:  # 20<=proof<80
        print('酒驾')
    else:
        print('醉驾')
else:
    print('well,you can go')