n=int(input("Enter a number to find next prime number:"))
while n:
    i=2
    while i<=n+1:
        if (n+1)%i==0:
            break
        i+=1
    if i==n+1:
        print(i)
        break
    else:
        n=n+1
        
