import random
import threading
def convert(strList):
    fList = []
    fList = map(float, strList)
    return fList

line = ""
for i in xrange(0,500000):
    line += str(random.uniform(-1,1))+" "
line += "\n"
fobj_w = open("data","w")
fobj_w.write(line)
fobj_w.close()

fobj_r = open("data","r")
line = fobj_r.readline()
line = line.strip(" \n")
line_ls = line.split(" ")

threads = []
t1 = threading.Thread(target=convert,args=(line_ls[:100000],))
t2 = threading.Thread(target=convert,args=(line_ls[100000:200000],))
t3 = threading.Thread(target=convert,args=(line_ls[200000:300000],))
t4 = threading.Thread(target=convert,args=(line_ls[300000:400000],))
t5 = threading.Thread(target=convert,args=(line_ls[400000:],))
threads.append(t1)
threads.append(t2)
threads.append(t3)
threads.append(t4)
threads.append(t5)

for t in threads:
    t.setDaemon(True)
    t.start()
    t.join()
    print threads
