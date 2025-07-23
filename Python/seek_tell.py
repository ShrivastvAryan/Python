with open('file.txt','r') as f:
    print(type(f))

    f.seek(10)

    data=f.read(5)
    print(data)

#iska mtlb ye hai ki pehle 10th character tak ayega phir uske 5 character aur aage jayega 
#f.tell() used to give info on which byte we are standing
#f.truncate(5) which means mujhe apni file mai khaali 5 character chahiye