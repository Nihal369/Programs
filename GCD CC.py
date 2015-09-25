t=input()
nums=[ ]
for i in range(0,t):
    temp=raw_input()
    a,b=temp.split()
    a=int(a)
    b=int(b)
    nums.append((a,b))

for i in nums:
    gcd=1
    for j in range(1,i[0]):
        if(i[0]%j==0 and i[1]%j==0):
            gcd=j
    lcm=(i[0]*i[1])/gcd
    print str(gcd)+" "+str(lcm)
    
