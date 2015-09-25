temp=raw_input()
n,k=temp.split()
n=int(n)
k=int(k)
word=raw_input()
w=[int(i) for i in word.split()]
w=sorted(w)
f=0
for i in w:
 if(f==0):
    for j in range(i+1,10000):
        if((i*j)%n==0 or n%(i*j)==0):
            m=j-i+1
            print("Minimum interval length: "+str(m))
            print("Found intervals:")
            f=1
            break
    if(f==0):
        print("NONE")
        exit()
    m-=1
    j=i+m
    if((i*j)%n==0 or n%(i*j)==0):
        print("["+str(i)+","+str(j)+"]")
    
            
    
    

