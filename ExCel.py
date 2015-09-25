#Global stuff

questions=[]
text=[]

#Wikipedia Text
def wiki():
    global text
    print "Enter the wikipedia text\n"
    temp=raw_input()
    text=[i for i in temp.split('.')]

#Questions
def ques():
    global questions
    print "Enter the questions\n"
    for i in range(1,6):
        print "Q"+str(i)+":",
        temp=raw_input()
        questions.append(temp)

#AI
def AI():
    for i in range(0,len(questions)):
        questions[i]=questions[i].lower()
        new=[j for j in questions[i].split()]
        for j in range(0,len(text)):
            if(questions[i] in text[j]):
                print text[j]
                break
wiki()
ques()
AI()
