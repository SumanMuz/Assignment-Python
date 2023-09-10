x=int(input("Enter your age in year:"))
if x<10:
    print("Kid")
elif x<20:
    print("Teen")
elif x<40:
    print("Young")
elif x<60:
    print("Experienced")
else:
    print("Senior Citizen")


match(x):
    case x if x<10:
        print("Kid")
    case x if x<20:
        print("Teen")
    case x if x<40:
        print("Young")
