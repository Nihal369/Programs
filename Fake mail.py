text=raw_input()
for i in range(1,len(text)):
    print str(i)+")"+text[:i]+"."+text[i:]+"@gmail.com"
