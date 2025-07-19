a=[11,34,1,4,6,8]

print(a.index(1)) # print the index position of that number
print(a.count(1)) # count the no. of occuring

a.insert(1,900) #this means add 900 at index 1
m=[800,1000,2000]
a.extend(m)# this will add a new list at the end,isme a naya ban jayega

'''to change without changing value of original list
use contactination method i.e k=a+m , then k will be 
the new list'''
print(a)

'''important thing
m=a
m[0]=0
print(a)  '''

'''If we look into it if m=a then not a new list 
will be formed,same original list will be mutated
in python

To counter this always use copy function
i.e m=l.copy()
    m[0]=0
    print(l) , now this method will create a new list'''




# list mai replace function kaam ni karta
