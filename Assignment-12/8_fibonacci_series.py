n=int(input("Enter a number which you want to print fibonacci series:"))
i=0
j=1
if n==1:
    print(i)
else:
    print(i,j,end=' ')
    while n>2:
        x=i+j
        i=j
        j=x
        print(x,end=' ')
        n=n-1
