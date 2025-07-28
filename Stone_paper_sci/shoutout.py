from os import system

names=['Aryan','Rohan','Arnav','Aditi']

for name in names:
    system(f'espeak "say shout to {name}"')