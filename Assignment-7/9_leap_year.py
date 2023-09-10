x=int(input("Enter a year:"))
match x:
    case x if x%100==0:
        if x%400==0:
            print("Leap Year")
        else:
            print("Non leap year")
    case x:
        if x%4==0:
            print("Leap year")
        else:
            print("Non leap year")
