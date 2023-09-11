n=int(input("Enter a number whereas sum of natural no:"))
s=0
for i in range(1,n+1,1):
    s=s+i**3
print("Sum of cube of {} natural number is {}".format(n,s))
