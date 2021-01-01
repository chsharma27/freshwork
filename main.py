import threading 
from threading import*
import time

dict={} 

def create(key,value,timeout=0):
    if k in dict:
        print("error: key exists") 
    else:
        if(k.isalpha()):
            if len(dict)<(1073741824) and value<=(16777216):
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(k)<=32: 
                    dict[k]=l
            else:
                print("error: Memory limit exceeded!! ")
        else:
            print("error: Invalid key_name!!")

            
def read(key):
    if key not in dict:
        print("error: key does not exist") 
    else:
        b=dict[key]
        if b[1]!=0:
            if time.time()<b[1]: 
                stri=str(key)+":"+str(b[0]) 
                return stri
            else:
                print("error: time-to-live of",key,"has expired") 
        else:
            stri=str(key)+":"+str(b[0])
            return stri


def delete(key):
    if key not in dict:
        print("error: given key does not exist") 
    else:
        b=dict[key]
        if b[1]!=0:
            if time.time()<b[1]: 
                del dict[key]
                print("successfully deleted")
            else:
                print("error: time-to-live of",key,"has expired")
        else:
            del dict[key]
            print("successfully deleted")


def modify(key,value):
    b=dict[key]
    if b[1]!=0:
        if time.time()<b[1]:
            if key not in dict:
                print("error: given key does not exist") 
            else:
                l=[]
                l.append(value)
                l.append(b[1])
                dict[key]=l
        else:
            print("error: time-to-live of",key,"has expired") 
    else:
        if key not in dict:
            print("error: given key does not exist") 
        else:
            l=[]
            l.append(value)
            l.append(b[1])
            dict[key]=l
