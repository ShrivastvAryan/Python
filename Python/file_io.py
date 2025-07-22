f=open('myfile.txt','r')

#that r is for reading the file
# w is for writing
# r mode default hota hai

#rb for opening binary file


text=f.read()
print(text)
f.close()