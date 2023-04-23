# Import required libraries
from tkinter import *
from PIL import ImageTk, Image

#===========================================================================================================

# Create an instance of tkinter window
win = Tk()

#============================================================================================================
# Define the properties of the Main window
win.geometry("1500x700") #aspect ratio
win.config(bg="black")# background colour

def main():
    #=============================================================================================================
    # creating the frams that will be used to place all the elements of the gui design

    # this is the frame that is set to house the field image and is already set to 75% of screen space
    fieldFrame = Frame(win, width=750, height=600)
    fieldFrame.pack()
    fieldFrame.place(x=0,y=0) 
    # the relx and rely values are values between 0 and 1, 
    # the x and y values specify the position of the top left corner of the frame
    #used to place the frame on a percentace value on the screens x,y values
    # basically if the x runs from 0-100 a relx=0,3 will place the center x of the frame at x = 30 (30% to the right of x =0)
    # Anchor is the alignemnt of the frame

    button1Frame = Frame(win, width=500, height=50)
    button1Frame.pack()
    button1Frame.place(anchor=NW, relx=0.2, rely=0.9)

    # frame for timer 
    frameTimer = Frame(win, width=50, height=20)
    frameTimer.pack()
    frameTimer.place(anchor=NW, relx=0.8, rely=0.01)

    #===============================================================================================================

    # Create a field object that taks up 75% of total screen space
    fieldImage = Image.open("horizontal_field.png") # fetchs field image, note the field image must be in the same folder for this function to work
    fieldImage = fieldImage.resize((750, 600), Image.ANTIALIAS) # resize the field image so it matches the desired aspect ratio
    fieldImageObject = ImageTk.PhotoImage(fieldImage)# this variable is used to create a viable image object that can be called

    #================================================================================================================
    # Create a Label Widget to display the field
    labelField = Label(fieldFrame, image = fieldImageObject)
    labelField.pack()
    #================================================================================================================
    # crosshair image is used to represent a player and serve as an example to visualise the cooridnate system
    # refer to the Co-ordinate system for soccer field tect file

    playerImage = Image.open("crosshair_blue_small.png")
    playerImage = playerImage.resize((50,50),Image.ANTIALIAS)
    playerObject = ImageTk.PhotoImage(playerImage) 
    labelPlayer = Label(fieldFrame,image = playerObject)
    labelPlayer.pack()
    labelPlayer.place(x=0,y=0)

    #=================================================================================================================

    #   creating test buttons for GUI design purposes, these buttons will later be changed to match the desired effects
    #   as of right now these buttons have no effect (change this list as buttons are implemeneted)
    buttonPlay = Button(button1Frame, text = "Pause/player",bg="grey") #not initiated yet
    buttonRewind = Button(button1Frame, text= "Rewind",bg="grey")# not initiated yet
    buttonForward = Button(button1Frame,text = "Forward",bg="grey")# not initiated yet
    buttonRewind.pack(side=LEFT) # used the side property to place the buttons next to each other.
    buttonPlay.pack(side=LEFT)
    buttonForward.pack(side=LEFT)
    #=================================================================================================================
    # label for timer 
    labelTimer = Label(frameTimer,text ="00:00",bg="grey",padx=5 )
    labelTimer.pack()

main()
win.mainloop()# main loop that runs the window, defualt exit condition is clicking the close button.