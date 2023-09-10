a=input("Enter your favorite colour :")
list1=["yellow","blue","orange","white","black","red"]
for color in list1:
    if color in a:
        c=color
        break
else:
    c="other"
match(c):
    case c if c=='yellow':
        print("Yellow-Monday")
    case c if c=='blue':
        print("Blue-Tuesday")
    case c if c=='orange':
        print("Orange-Wednesday")
    case c if c=='white':
        print("White-Thursday")
    case c if c=='black':
        print("Black-Friday")
    case c if c=='red':
        print("Red-Saturday")
    case c:
        print("All other colours-Sunday")
                    
                    
                
                
                





        

    
