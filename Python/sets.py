s={2,4,2,6,'Aryan','Rohan'}
print(s)

#Sets repeated values ni leta hai
#Sets are unordered collection of data
#multiple data type are allowed

a=set() #empty set
print(type(a))


#set methods in python
s1={1,4,5,6,7}
s2={4,6,8,3,2}
print(s1.union(s2))
print(s1.intersection(s2))
#s1.update(s2)# s1 mai s2 ki bi values le aaoo
print(s1.isdisjoint(s2))
print(s1.issuperset(s2))
print(s1.issubset(s2))
print(s1.discard(4)) # remove that item
print(s1.pop()) #koi random value pop ho jayegi
print(s1)

#del s1 delete the set