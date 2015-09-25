n=input()
c=0
ts=0
for i in range(1,n+1):
    c+=1
    s=0
    for j in range(1,i+1):
        s+=j
    ts+=s
    if(ts>n):
        print c-1
        exit()
    elif(ts==n):
        print c
        exit()
