n=int(input("Enter a number whereas you want to print first prime number:"))
i=2
count=0
while i:
    if count==n:
        break
    j=2
    while j:
        if i%j==0:
            break
        j+=1
    if i==j:
        print(i)
        count+=1
    i+=1

        
       
