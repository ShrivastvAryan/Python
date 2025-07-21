marks=[12,46,66,43,3]

# index=0

# for mark in marks:
#     print(mark)
#     if(index==3):
#         print("Im osm")
#     index=index+1

for index,mark in enumerate(marks): #enumarate value ke saath index bi deta hai
    # for index,mark in enumerate(marks,start=1) #for startng from index 1
    print(mark)
    if(index==3):
        print('Im osm')

