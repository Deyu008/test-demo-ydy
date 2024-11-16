score=eval(input('please enter your score:'))
# 多分支结构
if score<0 or score>100:
    print('error')
elif 0<=score<60:
    print('E')
elif 60<=score<70:
    print('D')
elif 70<=score<80:
    print('C')
elif 80<=score<90:
    print('B')
else:
    print('A')