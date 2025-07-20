a=input('Enter the number')
print(f'multiplication table of {a}: ')

try:
    for i in range(1,11):
        print(f'{int(a)}*{i}={(a)*i}')
except ValueError:
    print('Sorry some error occured')
except IndexError:
    print('Index error')

print('some lines of code')

#sort of  try and catch of Js
#we can use multiple expect