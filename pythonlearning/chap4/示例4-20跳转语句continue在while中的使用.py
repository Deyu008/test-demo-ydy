s=0
i=1
while i <=100:
    if i%2==1: # 奇数
        i+=1
        continue # 不再执行后面的代码了，相当于跳过了奇数
    # 偶数进行累加求和
    s+=i
    i+=1
print('1-100之间的偶数和：',s)