import time

timestamp=int(time.strftime('%H'))
print(timestamp)

if(timestamp>16):
    print('Good Evening sir')
elif(timestamp>=12):
    print('Good Afternoon sir')
else:
    print('Good Moring sir')
