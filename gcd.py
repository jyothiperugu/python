n1=int(input("enter a num:"))
n2=int(input("enter a num:"))
t=2
res=1
while True:
    if n1%t==0 and n2%t==0:
        n1=n1//t
        n2=n2//t
        res=res*t
    else:
        t=t+1
        if t>n1 or t>n2:
            print(res)
            break
