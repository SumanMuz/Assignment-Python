n=int(input("Enter a decimal number:"))
octal=0
i=1
while n>0:
    octal=octal+((n%8)*i)
    n=n//8
    i=i*10
print("Equivalent octal is",octal)
