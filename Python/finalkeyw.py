def func():
    try:
        l=[1,4,6,7]
        i=int(input('Enter the index: '))
        print(l[i])
        return 1
    
    except:
        print('Some error occured')
        return 0
    
    finally:
        print('Im finally executed') #finally is always executed

 #we can also write simple as print('Im finally executed) 
 # the difference comes in defining function 
 #  finally is used to close some connection basically when done in function which make it different 