number=eval(input('请输入您的6位中奖号码:'))
# if...else
if number==987654:
    print('congratulation')
else:
    print('regret')

print('------以上代码可以用条件表达式进行简化------')
result='congratulation' if number==987654 else 'regre'
print(result)

print('congratulation' if number==987654 else 'regre')