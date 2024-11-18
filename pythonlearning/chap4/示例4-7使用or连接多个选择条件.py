score=eval(input('请输入您的成绩：'))
if score<0 or score>100:
    print('error')
else:
    print('你的成绩为：',score)