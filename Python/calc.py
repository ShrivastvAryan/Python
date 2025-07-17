a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))

performer=input("Enter the operation you want to perform +,-,*,/: ")

if performer=="+":
    print("a + b is :",a+b)
elif performer=="-":
    print("a - b is :",a-b)
elif performer=="*":
    print("a * b is :",a*b)
elif performer=="/":
    print("a / b is :",a/b)
else:
    print("Please recheck your input")

