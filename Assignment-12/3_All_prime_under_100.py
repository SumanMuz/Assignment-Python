for i in range(2,100,1):
    for j in range(2,i+1,1):
        if i%j==0:
            break
    if i==j:
        print(i,end=' ')
