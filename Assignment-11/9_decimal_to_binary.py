n=int(input("Enter a number:"))
l1=[]
b='0'
while n:
    i=n%2
    l1.append(i)
    n=n//2
    b=b+str(i)
print(b)
