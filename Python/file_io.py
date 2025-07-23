f=open('myfile.txt','r')

#that r is for reading the file
# w is for writing
# r mode default hota hai

#rb for opening binary file

#always close the file
#or use with.open('myfile.txt','a') as f:


text=f.read()
print(text)
f.close()