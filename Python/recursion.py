def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1) # function calling inside function
    
#this is recursion function ke andar function ko call kr dia
print(factorial(5))

#ex2
def fibonacci_recursive(n):
    # Base cases for the recursion
    if n <= 1:
        return n
    # Recursive step: F(n) = F(n-1) + F(n-2)
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
    
print(fibonacci_recursive(5))