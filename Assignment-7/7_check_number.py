a=int(input("Enter a number :"))
match a:
    case a if a>0:
        print("Positive Number")
    case a if a<0:
        print("Negitive Number")
    case a if a==0:
        print("Zero")
