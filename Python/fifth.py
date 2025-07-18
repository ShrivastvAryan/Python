#Strings methods
# Strings are immutable

a="Aryan!!"
print(len(a))
print(a.upper())
print(a.lower()) # In these all cases strings wont me mutated , a new string will be created for every function that execute
print(a.rstrip('!')) # strip/remove the given trailing character
print(a.replace("Aryan","Harry"))
print(a.split("r")) # Split at that word

b="hi there Kaise ho Aryan Aryan" 
print(b.capitalize())#Captiliasize the first word and make other words small
print(len(b))
print(len(b.center(17)))
print(b.count("Aryan")) #Use to count the given word
print(b.endswith("Aryan")) # Use to confirm the ending 
print(b.find('there')) # Return the first word index and returns -1 if word not present
print(b.isalnum())#includes A-X , 0-9 (agar space hoga beech mai toh ni hoga )
print(b.isalpha()) #includes A-z
print(b.islower()) #if all are in lowercasse
print(b.isprintable())# if we have \n have init so its not an printable character


c='    '
print(c.isspace()) # only return true when have no words in it and only have space

d="Hi There"
print(d.istitle()) #First word of every letter should be capital
print(d.startswith('H'))

