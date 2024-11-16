num=eval(input('请输入一个四位整数:'))      # 用算数运算来求
print('个位上的数:',num%10)
print('十位上的数:',num//10%10)
print('百位上的数:',num//100%10)
print('千位上的数:',num//1000)

print('-'*40)
num=input('请输入一个四位的整数:')          # 用字符串索引
print('个位上的数:',num[3])
print('十位上的数:',num[2])
print('百位上的数:',num[1])
print('千位上的数:',num[0])

