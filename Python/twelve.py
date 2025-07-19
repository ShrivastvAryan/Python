#Functions argument

def average(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
        return sum/len(numbers)


c=average(5,6,7,1)
print(c) # if we write here then it will overwrite the default values

#keyword arguments: if we write the values with keywords as it is then we dont
#need to think about the order of number
#reutrn statemnt is used to give value back to the calling fucntion
