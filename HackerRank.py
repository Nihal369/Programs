temp=raw_input()
n,k,x=temp.split()
n=int(n)
k=int(k)
x=int(x)
temp=raw_input()
li=[int(i) for i in temp.split()]
li.sort()
li.reverse()
ans=li[0]*(x**k)
li=li[1:]
li=list(set(li))
for i in li:
    ans+=i
print ans
    
