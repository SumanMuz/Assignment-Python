n=int(input("Enter a number:"))
i=2
for i in range(2,n+1,1):
    if n%i==0:
        break
if i==n:
    print("{} is prime Number".format(n))
else:
    print("{} is not prime number".format(n))
                    
