def greet(fx): #this is the decorator function
    def mfx():
        print('Good Morning')
        fx()
        print('Thanks for using this func')
    return mfx

@greet
def hello():
    print('Hello world')

hello()

#these are basically decorating the function by giving starting and ending lines
# or can be done greet(hello)