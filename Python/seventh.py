#match-case
x=int(input("Enter the value of x: "))

match x:

    case 0:
        print('x is zero')
    case 4:
        print('x is 4')
    case _: # this is default case
        print(x)

