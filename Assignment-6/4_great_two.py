a=int(input("Enter first Number :"))
b=int(input("Enter second Number :"))
if a>b:
    print("%d is greater",a)
elif b>a:
    print("%d is greater",b)
else:
    if a%2==0 and b%2==0:
        print("%d and %d are equal and even number"%(a,b))
    else:
        print("Both number are equal but not both are even")
