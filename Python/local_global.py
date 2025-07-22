x=4
print(x)

def hello():
    x=5
    print(f'The local x is {x}')
    print('Hello there')

hello()

print(f'the gloabl x is {x}')


'''to make changes thorugh local variable 
in global variable

def hello():
    global x
    x=4
    y=5
    now it will change the global x
'''