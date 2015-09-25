questions=[]
print "Enter the Wikipedia text\n"
text=raw_input()
li=[i for i in text.split('.')]
print "Enter the 5 questions\n"
for i in range(1,6):
    print "Q"+str(i)+":",
    temp=raw_input()
    questions.append(temp)

for i in questions:
    dup=[j for j in i.split()]
    for k in range(0,len(dup)):
        for l in range(0,len(li)):
            if(dup[k] in li[l]):
                print li[l]
                break
            
