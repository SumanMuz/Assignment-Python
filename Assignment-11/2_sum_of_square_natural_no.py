n=int(input("Enter a number whereas sum of natural no:"))
s=0
for i in range(1,n+1,1):
    s=s+i**2
print("Sum of square of {} natural number is {}".format(n,s))
