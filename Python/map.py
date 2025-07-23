from functools import reduce


def cube(x):

    return x**3

l=[2,4,5,7,8]

newl=list(map(cube,l))
print(newl)

#we can also use here for loop
# but map make this short
#map(fucntion,list)


#FILTER

def filter_fucntion(a):
    return a>4

newl=list(filter(filter_fucntion,l))
print(newl)

#filter elements are used to filter 
#jin jin values ke lie wo true return krega toh wo wo values list mai ayegi


#reduce function 
numbers=[1,2,3,4,5]

def mysum(x,y):
    return x+y

sum =reduce(mysum,numbers) 
#it will work line 1+2=3 then 3+3=6

