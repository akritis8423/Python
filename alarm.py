import os
import datetime
from playsound import playsound
from AppKit import NSSound
os. system('cleart')
alarmH=int(input("What hour do you want the alarm to ring?"))
alarmM=int(input("What minute do you want the alarm to ring? "))
amPm= str(input("am or pm"))
os. system('cleart')
print("Waiting for alerm", alarmH, alarmM, amPm)
if (amPm=="pm"):
    alarmH = alarmH + 12
    while(1==1):
        if(alarmH== datetime.datetime.now().hour and alarmM==datetime.datetime.now().minute):
            print("Time to Wake up")
        playsound('/E:/music/beep-07.mp3')
        break