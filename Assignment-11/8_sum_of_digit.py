n=int(input("Enter a number :"))
s=0
while n:
    i=n%10
    s=s+i
    n=n//10
print("sum=",s)
