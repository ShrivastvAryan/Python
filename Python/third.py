#Typecasting,User Input

a='1'
b='5'

print(int(a)+int(b))  #This is typecasting and it is explicit typecasting

#Implicit TypeCasting

c=6
d=7.6
print(c+d) #giving output of float even if c is an integer

#User input, By default it takes input as String

e=input("enter the first number: ")
f=input("enter the second number: ")

print(e+f) #concatination will occur here
print(int(e)+int(f))