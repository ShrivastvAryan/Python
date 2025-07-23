def appl(fx,value): 
  return 6+fx(value) #function ke andar function

double=lambda x:x*2
avg= lambda x,y,z: x+y+z/3

print(double(5))
print(avg(2,4,6))
print(appl(double,2))

#lamba functions are small shorcuts of long functions for writing small operation