f=open('myfile.txt','w')
lines=['line1\n','line2\n','line3\n']
f.writelines(lines)
f.close()

#this is writelines method 
#it does not automatically make new line we need to use \n
#writelines method use to add line 