print("Enter two numbers:")
a,b=int(input()),int(input())
H=a if a<b else b
while H>1:
    if a%H==0 and b%H==0:
        break
    H-=1
print("HCF of",a,"and",b,"is",H)
