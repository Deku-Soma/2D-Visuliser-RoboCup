# Import required libraries
import os
from tkinter import *
from PIL import ImageTk, Image

# ===========================================================================================================

# Create an instance of tkinter window
win = Tk()

# ============================================================================================================

# Define the properties of the Main window
win.geometry("1100x700")  # aspect ratio
win.config(bg="black")  # background colour



# =============================================================================================================
# creating the frams that will be used to place all the elements of the gui design

# this is the frame that is set to house the field image and is already set to 75% of screen space
fieldFrame = Frame(win, width=750, height=600)
fieldFrame.pack()
fieldFrame.place(anchor=N, relx=0.34, rely=0)
# the relx and rely values are values between 0 and 1, 
# used to place the frame on a percentace value on the screens x,y values
# basically if the x runs from 0-100 a relx=0,3 will place the center x of the frame at x = 30 (30% to the right of x =0)
# Anchor is the alignemnt of the frame

button1Frame = Frame(win, width=500, height=50)
button1Frame.pack()
button1Frame.place(anchor=NW, relx=0.26, rely=0.9)

# ===============================================================================================================

# Here we're going to add a player to the screen

playerFrame = Frame(win, width=50, height=50)
playerFrame.pack()
playerFrame.place(anchor=N, relx=0.34, rely=0.5)

# ===============================================================================================================

# Create a field object that taks up 75% of total screen space
fieldImage = Image.open(
    "horizontal_field.png")  # fetchs field image, note the field image must be in the same folder for this function to work
fieldImage = fieldImage.resize((750, 600),
                               Image.ANTIALIAS)  # resize the field image so it matches the desired aspect ratio
fieldImageObject = ImageTk.PhotoImage(
    fieldImage)  # this variable is used to create a viable image object that can be called

# ================================================================================================================
# Create a Label Widget to display the field
label = Label(fieldFrame, image=fieldImageObject)
label.pack()
# =================================================================================================================

#   creating test buttons for GUI design purposes, these buttons will later be changed to match the desired effects
#   as of right now these buttons have no effect (change this list as buttons are implemeneted)
buttonPlay = Button(button1Frame, text="Pause/player", bg="grey")  # not initiated yet
buttonRewind = Button(button1Frame, text="Rewind", bg="grey")  # not initiated yet
buttonForward = Button(button1Frame, text="Forward", bg="grey")  # not initiated yet
buttonRewind.pack(side=LEFT)  # used the side property to place the buttons next to each other.
buttonPlay.pack(side=LEFT)
buttonForward.pack(side=LEFT)
# =================================================================================================================

playerImage = Image.open("nonselectedplayer1-removebg.png")
playerImage = playerImage.convert("RGBA")  # Convert image to RGBA format
data = playerImage.getdata()  # Get image data
new_data = []
for item in data:
    if item[0] == 255 and item[1] == 255 and item[2] == 255:  # Check if pixel is white
        new_data.append((255, 255, 255, 0))  # Set pixel to transparent
    else:
        new_data.append(item)  # Keep pixel as is
playerImage.putdata(new_data)  # Put new image data back into image
playerImageObject = ImageTk.PhotoImage(playerImage)

label = Label(playerFrame, image=playerImageObject, highlightthickness=0, borderwidth=0, )
label.pack()

# =================================================================================================================

win.mainloop()  # main loop that runs the window, defualt exit condition is clicking the close button.
