import sqlite3
import RPi.GPIO as GPIO
import time
from Tkinter import *

conn=sqlite3.connect('vminput.db')
c=conn.cursor()

conn2=sqlite3.connect('votercard.db')
c2=conn2.cursor()

w=Tk()
w.geometry("300x300")
w.configure(background="powder blue")



vi=StringVar()

l1=Label(w,text='Voter Id').pack()
e1=Entry(w,textvariable=vi).pack()
b1=Button(w,text="Submit",command=w.quit).pack()

w.mainloop()

vig=vi.get() #Voter id



i=0
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(16,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(18,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(22,GPIO.IN,pull_up_down=GPIO.PUD_UP)

while(1):
	if GPIO.input(12)==0:
		i+=1
		print ("Button 1 Pressed",i)
		time.sleep(0.5)
		
	if  GPIO.input(16)==0:
		i+=1
		time.sleep(0.5)
		print ("Button 2 Pressed",i)
	
	if GPIO.input(18)==0:
		i+=1
		print ("Button 3 Pressed",i)
		time.sleep(0.5)
		
	if  GPIO.input(22)==0:
		i+=1
		time.sleep(0.5)
		print ("Button 4 Pressed",i)
		break
            
