n=input()
n=int(n)
li=[ ]
for i in range(0,n):
    temp=input()
    li.append(temp)
ans=0
for i in li:
    new=[int(i) for i in i.split()]
    count=0
    for j in new:
        if(j==1):
            count+=1
    if(count>=2):
        ans+=1
print(ans)
