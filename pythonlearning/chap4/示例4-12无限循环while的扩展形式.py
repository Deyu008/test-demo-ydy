# 1-100之间的累加和
s=0 # 储存累加和
i=1 # (1)初始化变量
while i<=100: #(2)条件判断
    s+=i # (3)语句块
    # (4)改变变量
    i+=1
else:
    print('1-100之间的累加和：',s)
