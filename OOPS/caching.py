import functools
import time

@functools.lru_cache(maxsize=None)
def fx(n):
    time.sleep(5) #iske chalte 5 second le raha hai tu run
    return n*5


print(fx(20))
print('done for 20')
print(fx(2))
print('done for 2')

print(fx(20))  # This will be instant due to caching
print('done for 20 again')