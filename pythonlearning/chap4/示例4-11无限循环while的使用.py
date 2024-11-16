# (1)初始化变量
answer=input('今天要上课吗？\n')
while answer=='y': # (2)条件判断
    print('good good study day day up') # (3)语句块
    # （4）改变变量，若还是y，则继续循环，若不等于y，则停止循环
    answer=input('今天要上课吗？\n')

# 1-100之间的累加和
s=0 # 存储累加和
i=1 # (1)初始化变量
while i<=100: # （2）条件判断
    s+=i # （3）语句块
    # （4）改变变量
    i+=1
print('1-100之间的累加和',s)