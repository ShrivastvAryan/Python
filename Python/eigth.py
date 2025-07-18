#for loops

name="Abhi"

for i in name:
    print(i)
    if(i=="b"):
        print("This is b")
  


colors=['Red','Green','Blue','Yellow']
for color in colors:
    print(color)

for k in range(0,10,2): #(start index,end index,gap)
    print(k)

#while loop
i=0
while i<4: #pehle ye line check krenge agar ni hua true toh loop mai ni jayega
    print(i)
    i=i+1

print('Loop is done ') # pehle pura loop chalega jab tak false ni hoga phir ye print hoga