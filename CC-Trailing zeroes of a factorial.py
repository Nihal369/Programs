t=input()
n=[ ]
for i in range(0,t):
    temp=input()
    n.append(temp)
for i in n:
    fact=1
    for j in range(1,i+1):
        fact*=j
    count=0
    while fact>0:
        if((fact%10)==0):
            count+=1
            fact=fact/10
        else:
            break
    print count

        
    
