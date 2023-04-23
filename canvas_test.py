from tkinter import Tk, Canvas, NW
from PIL import ImageTk, Image

win = Tk()

#test event on click
def key(event):
    print("pressed")
#add images    
fieldimage = ImageTk.PhotoImage(file="horizontal_field.png")
playerimage= ImageTk.PhotoImage(file="nonselectedplayer2-removebg.png")

#set canvas
width, height = fieldimage.width(), fieldimage.height()
canvas = Canvas(win, bg="white", width=width, height=height)
canvas.pack()
#create image objects 
fieldIM=canvas.create_image(0, 0, image=fieldimage, anchor=NW)
playerIM=canvas.create_image(5, 0, image=playerimage, anchor=NW)

#bind events
canvas.tag_bind(playerIM,"<Button-1>", key)

win.mainloop()
