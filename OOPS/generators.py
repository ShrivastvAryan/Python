def my_generator():
    """A simple generator that yields numbers from 0 to 4."""
    for i in range(5):
        yield i

gen=my_generator()
print(next(gen))  # Output: 0

# ye on the fly generate krta hai without taking much memory
#jabki list mein saare elements store hote hain