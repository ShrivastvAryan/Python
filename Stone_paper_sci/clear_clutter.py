import os

files=os.listdir('./images')

i=1

for file in files:
        if file.endswith('.jpeg'):
            print(file)
            os.rename(f'./images/{file}',f'./images/img-{i}.jpeg')
            i=i+1


# os.rename('/bg-a.jpeg','/bg-1.jpg')