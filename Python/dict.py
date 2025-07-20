dic={
    1:"Aryan",
    10:"Anshu",
    344:"Rohan"
}

print(dic[10])

#ordered collection 
# 10 is key and Anshu is value
#print(dic['name']) # it will throw error on non existence
#print(dic.get('name))# it will null on non existence

for key in dic.keys():
    print(dic[key]) # return the value corresponding to key