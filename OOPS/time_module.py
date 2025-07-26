import time

def usingWhile():
    i=0
    while i<500:
        i=i+1
        print(i)
    

def usingFor():
    for i in range(500):
        print(i)
    pass

init =time.time()
usingFor()
t1=time.time()-init

usingWhile()
print(t1)
print(t1)

# it tells kitni der lagi pura program run hone mai
#time has many more modules