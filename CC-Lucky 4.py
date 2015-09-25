t=input()
n=[ ]

for i in range(0,t):
    temp=input()
    n.append(temp)

for i in n:
    count=0
    while(i>0):
        if(i%10==4):
            count+=1
        i=i/10
    print count
