import json
import threading 

from threading import*
import time

d={}               #'d' is the dictionary in which we store data

#for create operation 
#use syntax "create(key_name,value,timeout_value)" timeout is optional you can continue by passing two arguments without timeout

def create(key,value,timeout=0):
    if key in d:
        print("error: this key is already exists in database") #error message1
    else:
        if(key.isalpha()):
            if len(d)<(1024*1020*1024) and value<=(16*1024*1024): #constraints for file size less than 1GB and Jasonobject value less than 16KB 
                if timeout==0:
                    l1=[value,timeout]
                else:
                    l1=[value,time.time()+timeout]
                if len(key)<=32: #constraints for input key_name capped at 32chars
                    d[key]=l
                    print(key+" is created in database")
            else:
                print("error: given Memory limit is  exceeded!! ")#error message2
        else:
            print("error: Invalind key name!! key name must contain only alphabets and no special characters or numbers")#error message3

#for read operation
            
def read(key):
    if key not in d:
        print(" given key does not exist in database. Please enter a valid key") #error message4
    else:
        p=d[key]
        if p[1]!=0:
            if time.time()<p[1]: #comparing the present time with expiry time
                fresh=str(key)+":"+str(p[0]) #to return the value in the format of JasonObject i.e.,"key_name:value"
                return fresh
            else:
                print("error: time expierd for",key) # show error message5
        else:
            fresh=str(key)+":"+str(p[0])
            return fresh

#for delete operation


def delete(key):
    if key not in d:
        print(" given key does not exist in database. Please enter a valid key") #error message4
    else:
        p=d[key]
        if p[1]!=0:
            if time.time()<p[1]: #comparing the current time with expiry time
                del d[key]
                print("key is successfully deleted from database")
            else:
                print("your time expierd for the",key) # give error message5
        else:
            del d[key]
            print("key is successfully deleted")

