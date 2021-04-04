from os import system
from time import sleep

statement = input('Please Enter your statement: ')
timer = input('Enter your time Example (1 m / 1 h / 30 s) : ')
ftime = timer.split()

if ftime[1] == 'm':
    number1 = int(ftime[0])
    number1 = number1 * 60
    for i in range(number1):
        print(f"{str(number1 -i)} SecTime",end="\r")
        sleep(1)
    #sleep(number1)
    system('notify-send '+'"'+statement+'"')
    system('mpv ~/Music/notif.mp3')
elif ftime[1] == 'h':
    number1 = int(ftime[0])
    number1 = number1 * 3600
    for i in range(number1):
        print(f"{str(number1 -i)} SecTime",end="\r")
        sleep(1)
    #sleep(number1)
    system('notify-send '+'"'+statement+'"')
    system('mpv ~/Music/notif.mp3')
elif ftime[1] == 's':
    number1 = int(ftime[0])
    for i in range(number1):
        print(f"{str(number1 -i)} SecTime",end="\r")
        sleep(1)
    #sleep(number1)
    system('notify-send '+'"'+statement+'"')
    system('mpv ~/Music/notif.mp3')

def timer(statement,time,kind_time):
    from time import sleep
    number1 = int(time)
    if kind_time == 'minute' or kind_time == 'minutes':
        number1 = number1 * 60
        sleep(number1)
        system('notify-send '+'"'+statement+'"')
        system('mpv ~/Music/notif.mp3')
    elif kind_time == 'hour' or kind_time == 'hours':
        number1 = number1 * 3600
        sleep(number1)
        system('notify-send '+'"'+statement+'"')
        system('mpv ~/Music/notif.mp3')
    elif kind_time == 'second' or kind_time =='seconds':
        sleep(number1)
        system('notify-send '+'"'+statement+'"')
        system('mpv ~/Music/notif.mp3')
# timer('tea is ready',20,'second')
