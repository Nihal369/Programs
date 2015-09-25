n=input()
li=[ ]
for i in range(0,n):
    temp=raw_input()
    li.append(temp)
new=[]
for i in li:
    t,s=i.split()
    t=int(t)
    s=int(s)
    new.append((t,s))
c=0
for i in range(0,len(new)):
    for j in range(0,len(new)):
        if(i!=j):
            if(new[i]==new[j] and new[i]!=64 and new[j]!=64):
                c+=1
                new[j]=64
print c+1
