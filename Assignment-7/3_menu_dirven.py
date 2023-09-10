print("Select your choice")
print("Press 1: To check Right angled triangle or not")
print("Press 2: To check Isosceles triangle or not")
print("Press 3: To check Equilateral triangle or not")
print("Press 4: Exit")
m=int(input("Enter your choice:"))
match(m):
    case 1:
        print("Enter All three sides of triangle :")
        a,b,c=float(input()),float(input()),float(input())
        if a**2==b**2+c**2 or b**2==a**2+c**2 or c**2==a**2+b**2:
            print("Right angled triangle")
        else:
            print("Not right angle triangle")
    case 2:
        print("Enter All three sides of triangle :")
        a,b,c=float(input()),float(input()),float(input())
        if a==b or b==c or a==c:
            print("Isosceles Triangle")
        else:
            print("Not Isoceles Triangle")
    case 3:
        print("Enter All three sides of triangle :")
        a,b,c=float(input()),float(input()),float(input())
        if a==b==c:
            print("Equlateral Triangle")
        else:
            print("Not equlateral Triangle")
    case 4:
        exit()
    case _:
        print("Invalid choice")
        
