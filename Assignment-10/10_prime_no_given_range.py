print("Enter two numbers to print all prime number from these range:")
a,b=int(input()),int(input())
for i in range(a,b+1,1):
    if i>1:
        for j in range(2,i+1,1):
            if i%j==0:
                break
        if i==j:
            print(i)
