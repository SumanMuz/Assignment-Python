n=int(input("Enter a number whereas sum of natural no:"))
s=0
for i in range(1,n+1,1):
    i=i*2
    s=s+i
print("Sum of first {} even natural number is {}".format(n,s))
