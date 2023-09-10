import math
print("Quadratic Equation")
a=int(input("Enter co-officient of x^2 :"))
b=int(input("Enter co-officient of x :"))
c=int(input("Enter constant term:"))
d=(b**2)-4*a*c
if d==0:
    x1=-b/(2*a)
    print("Real and equal roots:",x1)
elif d>0:
    x1=(-b+math.sqrt(d))/2*a
    x2=(-b-math.sqrt(d))/2*a
    print("Real and distinct roots:",x1,x2)
else:
    print("Imaginary roots")

