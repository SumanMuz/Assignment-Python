month=int(input("Enter month number :"))
if month in (1,3,5,7,8,10,12):
    print("31 Days")
elif month in (4,6,9,11):
    print("30 Days")
elif month==2:
    print("28 or 29 Days")
else:
    print("Invalid month number")


"""
n=1
while n:
    a=int(input("enter month number :"))
    match(a):
        case 1:
            print("January-31")
        case 2:
            print("Febuaray-28")
        case 3:
            print("March-31")
        case 4:
            print("April-30")
        case 5:
            print("May-31")
        case 6:
            print("June-30")
        case 7:
            print("July-31")
        case 8:
            print("August-31")
        case 9:
            print("September-30")
        case 10:
            print("October-31")
        case 11:
            print("November-30")
        case 12:
            print("December-31")
        case 13:
            n=0
"""
            
