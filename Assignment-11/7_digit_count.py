n=int(input("Enter a number :"))
c=0
#for i in str(n):
 #   c+=1
#print("Number of digit =",c)
while n:
    n=n//10
    c+=1
print(c)
