print("Enter two numbers:")
a,b=int(input()),int(input())
m=a if a<b else b
i=2
while i<=m:
    if a%i==0 and b%i==0:
        break
    i+=1
if i==m+1:
    print("Co-prime")
else:
    print("Not co-prime")


    
