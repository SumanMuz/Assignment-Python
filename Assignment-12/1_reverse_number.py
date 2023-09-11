n=int(input("Enter a number:"))
y=0
while n:
    x=n%10
    y=y*10+x
    n=n//10
print(y)
    
