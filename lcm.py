n1=int(input("enter the numbers"))
n2=int(input("enter the numbers"))
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
        print(res*n1*n2)
        break
    
