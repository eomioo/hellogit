#!/usr/bin/python3

# Filename: alarm_clock.py
# make a alarm clock

from tkinter import *
import datetime
import time
import winsound

def alarm(set_alarm_timer):
	while True:
		time.sleep(1)
		current_time = datetime.datetime.now()
		now = current_time.strftime("%H:%M:%S")
		date = current_time.strftime("%Y:%d:%m")
		print('The Set Date is:', date)
		print(now)
		if now == set_alarm_timer:
			print("Time to Wake up")
			winsound.PlaySound("breed.wav", winsound.SND_FILENAME)
			break

def actual_time():
	set_alarm_timer = f"{hour.get()}:{minitue.get()}:{sec.get()}"
	alarm(set_alarm_timer)

clock = Tk()

clock.title("Alarm Clock")
clock.geometry("400x200")
time_format = Label(clock, text="ENter time in 24 hour format", fg="red", bg="black", font="Arial").place(x=60, y=120)
addTime = Label(clock, text="Hour Min Sec", font=60).place(x=150)
setYourAlarm = Label(clock, text="When to wake you up", fg="blue", relief="solid", font=("HElevetica", 10, "bold")).place(x=0, y=29)

# the variables we require to set the alarm:
hour = StringVar()
minitue = StringVar()
sec = StringVar()

# time require to set the alarm clock:
hourTime = Entry(clock, textvariable=hour, bg="pink", width=15).place(x=170, y=30)
minTime = Entry(clock, textvariable=minitue, bg="pink", width=15).place(x=210, y=30)
secTime = Entry(clock, textvariable=sec, bg="pink", width=15).place(x=250, y=30)

# to take the time unput by user
submit = Button(clock, text="Set Alarm", fg="red", width=10, command=actual_time).place(x=110, y=70)

clock.mainloop()