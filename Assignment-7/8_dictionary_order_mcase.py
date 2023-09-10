a=input("Enter first string")
b=input("Enter second string")
match (a,b):
    case (a,b)if a==b:
        print("Identical string")
    case (a,b) if a>b:
        print("{} comes after {}".format(a,b))
    case (a,b) if a<b:
        print("{} comes before {}".format(a,b))
