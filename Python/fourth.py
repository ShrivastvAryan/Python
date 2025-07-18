#Strings in python
a='''
Hi there 
how are you kaise ho ap
'''

print(a) # this trip quote help us to define it at string also allow us to write in multiple lines
#In python strings are like an array of character

#for loop through strings

for i in a:
    print(i)

#length function 
b="Aryan"
print(len(b))

#Slicing function
print(b[:2]) # Even if we dont put zero at first place it will automatically take it as zero
print(b[0:-2]) # Here python autmoatically treat it as b[0:len(b)-2] which makes the final result as b[0:3]
print(b[-3:-1]) # Same logic as above
print(b[-1:-3]) # it will not print this because it has no logic