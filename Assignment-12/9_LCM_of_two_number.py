print("Enter two numbers")
a,b=int(input()),int(input())
L=a if a>b else b
while L<=a*b:
    if L%a==0 and L%b==0:
        break
    L=L+b
print("LCM of {} and {} is {}".format(a,b,L))
