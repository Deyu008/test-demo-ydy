x=20 # 直接赋值，直接将20赋值给左侧的变量x
y=10
x=x+y # 将x+y的和赋值给x，x的值为30
print(x)

x+=y # 30+10=40
print(x)

x-=y # 40-10=30
print(x)

x*=y # 30*10=300
print(x)

x/=y # 300/10=30
print(x)

x%=2 # x=x2
print(x) # 0

z=3
y//=z # y=y//z
print(y) # 3

y**=2 # y=y**2  即y的两次幂，y=y*y
print(y) # 3*3=9

# python支持链式赋值
a=b=c=100 # 相当于执行 a=100 b=100 c=100
print(a,b,c)

# python支持系列解包赋值
a,b=10,20 # 相当于执行了 a=10 b=20
print(a,b)

print('------如何交换两个变量的值呢？------')
a,b=b,a
print(a,b)

