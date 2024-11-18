import random
rand=random.randint(1,100) # 产生1-100之间的随机数

s=1
while s<=10:
    num=eval(input('在我心中有个数,1-100之间,请你猜一猜:'))
    if num>rand:
        print('大了,还有',10-s,'次机会')
        s+=1
    elif num<rand:
        print('小了,还有',10-s,'次机会')
        s+=1
    else:
        print('猜对了!')
        break
if s<=3:
    print('真聪明,一共猜了',s,'次')
elif s<=6:
    print('还可以,一共猜了',s,'次')
elif s<=10:
    print('一般,一共猜了',s,'次')
else:
    print('超过10次啦,重新来吧!')
