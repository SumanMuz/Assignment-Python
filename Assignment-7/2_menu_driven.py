print("Enter two numbers:")
a=int(input())
b=int(input())
print("Select Choice :")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")

while 1:
    x=int(input("Enter your choice:"))
    match(x):
        case 1:
            print("Addition=",a+b)
        case 2:
            print("Subtraction=",a-b)
        case 3:
            print("Multiplication=",a*b)
        case 4:
            print("Division=",a/b)
        case 5:
            exit(0)
    print("")
