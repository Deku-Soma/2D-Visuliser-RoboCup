from tkinter import Tk, Canvas, NW, Button
import loadJSONFile
from PIL import ImageTk, Image
import tkinter as tk
import time as Timer

def pause():
    global paused
    paused = not paused

def rewind():
    global t
    t = max(0, t - 120)

def speedup():
    global speed
    speed = min(10, speed + 2)

def update_canvas():
    global t, paused, speed
    if not paused:
        canvas.delete("players")
        for i in range(1,12):
            playerData=loadJSONFile(i)
            myCoords=playerData[t]['MyPosition']
            convCoords= convert(myCoords[0],myCoords[1])
            playerIM[i]=canvas.create_image(convCoords[0],convCoords[1], image=playerimage, anchor=NW, tag="players")
        t = min(t + speed, len(playerData)-1)
    win.after(50, update_canvas)

win = Tk()
fieldimage = ImageTk.PhotoImage(file="horizontal_field.png")
playerimage= ImageTk.PhotoImage(file="nonselectedplayer1-removebg-smaller.png")
width, height = fieldimage.width(), fieldimage.height()
canvas = Canvas(win, bg="white", width=width, height=height)
canvas.pack()
fieldIM=canvas.create_image(0, 0, image=fieldimage, anchor=NW)

test=ParseData(1)
test.initialGameState(1)
playerData=loadJSONFile(1)
myCoords=playerData[0]['MyPosition']
playerIM=[None]*12
for i in range(1,12):
    playerData=loadJSONFile(i)
    myCoords=playerData[0]['MyPosition']
    convCoords= convert(myCoords[0],myCoords[1])
    playerIM[i]=canvas.create_image(convCoords[0],convCoords[1], image=playerimage, anchor=NW, tag="players")

begin= Timer(win)
begin.start_timer()

speed = 1
paused = False
t = 0

Button(win, text="Pause/Play", command=pause).pack()
Button(win, text="Rewind", command=rewind).pack()
Button(win, text="Speed Up", command=speedup).pack()

win.after(0, update_canvas)
win.mainloop()
