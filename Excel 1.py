#Nihal369

#Inactive state
def inactive():
    print "\nCurrent state:Inactive"
    print "Enter a command(Begin/Exit):",
    command=raw_input()
    command=command.lower()
    if(command=='begin'):
        active()
    elif(command=='exit'):
        #Exited State
        print "\nExitied"
        exit()
    else:
        print "Invalid command! Please try again"
        inactive()

#Active state
def active():
    print "\nCurrent state:Active"
    print "Enter a command(Pause/End):",
    command=raw_input()
    command=command.lower()
    if(command=='pause'):
        paused()
    elif(command=='end'):
        inactive()
    else:
        print "Invalid command! Please try again"
        active()
        
#Paused state
def paused():
    print "\nCurrent state:Paused"
    print "Enter a command(Resume/End):",
    command=raw_input()
    command=command.lower()
    if(command=='resume'):
        active()
    elif(command=='end'):
        inactive()
    else:
        print "Invalid command! Please try again"
        paused()
        
#Program execution starts
inactive()
