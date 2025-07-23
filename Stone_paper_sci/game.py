import random
# Stone Paper Scissor
#here stone is 1 , paper is 0, scissor is -1

game_list=[1,0,-1]

print('Hi there welcome to the Stone Paper Scissor game')

print('---------------------------------------------')

print('So let me tell you the rules of game\n' \
'Stone=1 \nPaper=0 \nScissor=-1\n')

b=random.choice(game_list)
# print(b)

a=int(input("Enter the number of stone, paper or scissor: "))


if(a==b):
    print('Draw')

#Stone logic
elif(a==1 and b==0):
    print('You lost')
elif(a==1 and b==-1):
    print('You won')

#Scissor logic
elif(a==-1 and b==0):
    print('You won')
elif(a==-1 and b==1):
    print('You lost')

#Paper logic
elif(a==0 and b==1):
    print('You won')
elif(a==0 and b==-1):
    print('You lost')