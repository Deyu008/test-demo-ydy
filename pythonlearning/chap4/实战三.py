for i in range(1,10):
    for j in range(1,i+1):
        print(str(j)+'*'+str(i)+'='+str(i*j),end='\t')  # \t是制表位
    print()