from tkinter import Tk, Canvas, NW
from PIL import ImageTk, Image
import os

win = Tk()

#test event on click
def key(event):
    print("pressed")
#add images    

player_file = "nonselectedplayer2-removebg.png"

field_file = "Soccer_Field_HD-downsized.png"

folder = "Assets"

cwd = os.getcwd()

path_to_player_file = os.path.join(cwd, folder, player_file)
path_to_field_file = os.path.join(cwd,folder,field_file)
playerImage = Image.open(path_to_field_file)
playerimage = playerImage.resize((900,600),Image.ANTIALIAS)
fieldimage = ImageTk.PhotoImage(playerimage)
playerimage= ImageTk.PhotoImage(file=path_to_player_file)

#set canvas
canvas = Canvas(win, bg="black", width=1920, height=1080)
canvas.pack()
#create image objects 
fieldIM=canvas.create_image(0, 0, image=fieldimage, anchor=NW)
playerIM=canvas.create_image(5, 0, image=playerimage, anchor=NW)

#bind events
canvas.tag_bind(playerIM,"<Button-1>", key)

win.mainloop()
