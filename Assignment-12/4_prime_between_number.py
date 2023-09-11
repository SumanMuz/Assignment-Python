print("Enter two numbers which you find all prime numbers between them :")
n,m=int(input()),int(input())
for i in range(n,m+1,1):
    if i>1:
        for j in range(2,i+1,1):
            if i%j==0:
                break
        if i==j:
            print(i,end=' ')
                    
