import main as s 
s. create("suman",25) 
s. read("suman")
s. create("suman",50)
s. modify("suman",55)
s. delete("suman")

test=Thread(target=(create or read or delete),args=(key_name,value,timeout)) 
test.start()
test.sleep()