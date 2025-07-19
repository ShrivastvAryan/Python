#Operations on tuple 

# If you want to change or modify tuple
# then first create it as list and then 
# mutate that list and then again change
# it to tuple

Country=('Spain','Italy','India','Australia')

listCountry=list(Country) # Conversion to list
listCountry.append("Japan")
print(listCountry)

Country=tuple(listCountry)#Again declaring as tuple
print(Country)

'''index(element,start,end)'''



