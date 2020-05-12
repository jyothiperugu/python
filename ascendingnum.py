n=int(input("enter a num:"))
a=0
d=0
k=n%10
n=n//10
while n:
    r=n%10
    n=n//10
    if(a==0 and d==0):
        if k>r:
            a=1
        else:
            d=1
    else:
        if (k<r and a==1) or (k>r and d==1):
            print("mixed")
            a=0
            d=0
            break
    k=r
if d==1:
    print("desending")
elif a==1:
    print("ascending")
        
