a=input()
b=input()
gcd=1
for i in range(1,a):
    if(a%i==0 and b%i==0):
        gcd=i
lcm=(a*b)/gcd
print str(gcd)+" "+str(lcm)
