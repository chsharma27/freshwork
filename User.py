import main as data 
data.create("chetan",30
data.create("shivam",75,3610)
data.read("chetan")
data.read("shivam")
data.create("chetan",55)
data.modify("chetan",50)
data.delete("chetan")
thread1=Thread(target=(create or read or delete),args=(key_name,value,timeout)) 
thread1.start()
thread1.sleep()
thread2=Thread(target=(create or read or delete),args=(key_name,value,timeout)) 
thread2.start()
thread2.sleep()
