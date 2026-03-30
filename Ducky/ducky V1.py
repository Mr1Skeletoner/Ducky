from tkinter import *
import winsound
import time
import os
os.chdir(os.path.dirname(os.path.abspath(__file__))) # i dont know what this does
# but it fixes the problem where the code looks for files (image and audio) in another place

ducky_window = Tk()

ducky_window.geometry("250x300")
ducky_window.title("Ducky")
ducky = PhotoImage(file="ducky.png")
ducky_window.iconphoto(True, ducky)

ducky_says = StringVar()
ducky_says.set("")

def ducky_clicked():
    winsound.PlaySound("quack.wav", 0) # shoutout to crazyduckman or smth he owns this audio
    ducky_says.set("I believe in you!")

ducky_button = Button(ducky_window, image=ducky, command=ducky_clicked)
ducky_text = Label(ducky_window, textvariable=ducky_says)


ducky_button.pack()
ducky_text.pack()


ducky_window.mainloop()



# i feel stupid making ts
# no way this took 3 hours
