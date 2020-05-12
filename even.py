n=int(input("enter a num:"))
ec=0
oc=0
zc=0
while n:
    r=n%10
    n=n//10
    if r==0:
        zc+=1
    elif r%2==0:
        ec+=1
    else:
        oc+=1
print(ec,oc,zc)        
        
        
            
    
