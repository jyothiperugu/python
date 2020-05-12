
n=int(input("enter a num:"))
c=0
for i in range(1,n+1):
    r=n%i
    if (r==0):
        print(i)
        c=c+1
if c==2:
    print("prime")
else:
    print("not prime")
