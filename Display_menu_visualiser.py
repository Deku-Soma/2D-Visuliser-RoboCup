import tkinter as tk
from tkinter import messagebox
from tkinter import *
import os
from PIL import ImageTk, Image
from Team import *
from Field_Objects import *
win = tk.Tk()

win.geometry("1000x800") #aspect ratio
win.config(bg="green")# background colour
#============================================================
#functions
def go_to_menu(event):
    Frame_welcome.pack_forget()
    Frame_menu.pack(fill="both",expand=True)

def go_to_visualiser(event):
    if menu.get() == "Game 1":
        Frame_menu.pack_forget()
        Frame_visualiser.pack(fill="both",expand=True)
    else: 
        messagebox.showinfo("Warning", "You have not selected a game. \n Please selecte a game")

#=============================================================
Frame_welcome = tk.Frame(win,bg="blue",width=1000,height=800)
#=============================================================
#welcome frame components
canvas = tk.Canvas(Frame_welcome, bg="black", width=1000, height=800)


welcomeFile = "robocub2-resize.jpg"
menu_button_file = "menu_button.png"
folder = "Assets"

cwd = os.getcwd()

path_to_welcome_file = os.path.join(cwd,folder,welcomeFile)
path_to_menu_button_file = os.path.join(cwd,folder,menu_button_file)

welcomeIm = Image.open(path_to_welcome_file)
welcomeIm = welcomeIm.resize((1000,800),Image.LANCZOS)
welcomeImObject = ImageTk.PhotoImage(welcomeIm)

menu_buttonIM = Image.open(path_to_menu_button_file)
menu_buttonIM = menu_buttonIM.resize((200,75),Image.LANCZOS)
menu_buttonIMobject = ImageTk.PhotoImage(menu_buttonIM)


welcomebg=canvas.create_image(0, 0, image=welcomeImObject, anchor="nw")
menu_buttonbg = canvas.create_image(400, 500, image=menu_buttonIMobject, anchor="nw")
canvas.tag_bind(menu_buttonbg,"<Button-1>", go_to_menu)
canvas.pack()
#=============================================================
Frame_menu = tk.Frame(win,bg="black",width=1000,height=800)
#=============================================================
#create canvas for menu
canvas_menu = tk.Canvas(Frame_menu, width=1000, height=800)
menubgfile = "menubg.jpg"
path_to_menu_bg = os.path.join(cwd,folder,menubgfile)

menubgIm = Image.open(path_to_menu_bg)
menubgIm = menubgIm.resize((1000,800),Image.LANCZOS)
menubgIMobject = ImageTk.PhotoImage(menubgIm)
menubg = canvas_menu.create_image(0,0,image=menubgIMobject,anchor="nw")

#button to go to visualiser
visualiser_button_file = "match_button.png"
path_to_visualiser_button = os.path.join(cwd,folder,visualiser_button_file)
visualiser_buttonIM = Image.open(path_to_visualiser_button)
visualiser_buttonIM = visualiser_buttonIM.resize((200,75),Image.LANCZOS)
visualiser_buttonIMobject = ImageTk.PhotoImage(visualiser_buttonIM)
visualiser_buttonbg = canvas_menu.create_image(400,500,image=visualiser_buttonIMobject,anchor="nw")
# menu frame components
label_menu = tk.Label(Frame_menu,text="Welcome to the RoboCup Visualiser",font= 50,bg="blue", fg = "white")
menu = tk.StringVar()
menu.set("Select a game")

#Create a dropdown Menu
drop= tk.OptionMenu(canvas_menu, menu,"Game 1")
drop.pack()
drop.place(x=500,y=300)

Frame_visualiser = tk.Frame(win,bg="white",width=1000,height=800)

Frame_welcome.pack(expand=True,fill="both")
canvas_menu.tag_bind(visualiser_buttonbg,"<Button-1>", go_to_visualiser)
canvas_menu.focus()
canvas_menu.pack(fill="both",expand=True)
#=============================================================
#visualiser screen
# creating the frams that will be used to place all the elements of the gui design

# this is the frame that is set to house the field image and is already set to 75% of screen space
canvas_visualiser = Canvas(Frame_visualiser, bg="black", width=1920, height=1080)
canvas_visualiser.pack()
# the relx and rely values are values between 0 and 1, 
# the x and y values specify the position of the top left corner of the frame
#used to place the frame on a percentace value on the screens x,y values
# basically if the x runs from 0-100 a relx=0,3 will place the center x of the frame at x = 30 (30% to the right of x =0)
# Anchor is the alignemnt of the frame

time_button_frame = Frame(Frame_visualiser, width=500, height=50, )
time_button_frame.pack()
time_button_frame.place(anchor=N, relx=0.5, rely=0.9)

# frame for timer 
frameTimer = Frame(Frame_visualiser, width=50, height=20)
frameTimer.pack()
frameTimer.place(anchor=NW, relx=0.8, rely=0.01)

#===============================================================================================================

field_file = "Soccer_Field_HD-downsized.png"

folder = "Assets"

cwd = os.getcwd()

path_to_field_file = os.path.join(cwd,folder,field_file)
# Create a field object that taks up 75% of total screen space
fieldImage = Image.open(path_to_field_file) # fetchs field image, note the field image must be in the same folder for this function to work
fieldImage = fieldImage.resize((750, 600), Image.LANCZOS) # resize the field image so it matches the desired aspect ratio
fieldImageObject = ImageTk.PhotoImage(fieldImage)# this variable is used to create a viable image object that can be called\
#create image objects 
fieldIM=canvas_visualiser.create_image(0, 0, image=fieldImageObject, anchor=NW)

#================================================================================================================
# Create a Label Widget to display the field
#================================================================================================================
#  image is used to represent a player and serve as an example to visualise the cooridnate system
# refer to the Co-ordinate system for soccer field tect file

player1_file = "nonselectedplayer1-removebg.png"
player2_file = "nonselectedplayer2-removebg.png"
folder = "Assets"

cwd = os.getcwd()

path_to_player1_file = os.path.join(cwd, folder, player1_file)
path_to_player2_file = os.path.join(cwd, folder, player2_file)

team1 = Team()
team2 = Team()

for i in range(0,11) :
    player1 = Player(path_to_player1_file, i*50, i*50)

    player2 = Player(path_to_player2_file,i*50,500)
    team1.add_player(player1)
    team1.team[i].print_centre()
    team2.add_player(player2)
teams = [team1,team2]

#display_teams(teams,canvas)
playerIM = [None]*22
playerlist=[] 
ct =0
playerImage = Image.open(path_to_player1_file)
playerImage = playerImage.resize((50, 50), Image.LANCZOS)
playerObject = ImageTk.PhotoImage(playerImage)

for x in range(0,2):
    if x == 0:
        for i in range(0,11):

            playerIM[i] = canvas_visualiser.create_image(teams[x].team[i].x(), teams[x].team[i].y(), image=teams[x].team[i].get_sprite_image(), anchor=NW)
            #cts = str(ct)
            #canvas.tag_bind(playerIM,"<Button-"+cts+">", key)
    else:
        for i in range(0,11):
            playerIM[i+11]=canvas_visualiser.create_image(teams[x].team[i].x(),teams[x].team[i].y(), image=teams[x].team[i].get_sprite_image(), anchor=NW)
            print(playerIM)
            #cts = str(ct)
            #canvas.tag_bind(playerIM,"<Button-"+cts+">", key)
   

#=================================================================================================================


#=================================================================================================================

#   creating test buttons for GUI design purposes, these buttons will later be changed to match the desired effects
#   as of right now these buttons have no effect (change this list as buttons are implemeneted)
buttonPlay = Button(time_button_frame, text = "Pause/player",bg="grey") #not initiated yet
buttonRewind = Button(time_button_frame, text= "Rewind",bg="grey")# not initiated yet
buttonForward = Button(time_button_frame,text = "Forward",bg="grey")# not initiated yet
buttonRewind.pack(side=LEFT) # used the side property to place the buttons next to each other.
buttonPlay.pack(side=LEFT)
buttonForward.pack(side=LEFT)
#=================================================================================================================
# label for timer 
labelTimer = Label(frameTimer,text ="00:00",bg="grey",padx=5 )
labelTimer.pack()





win.mainloop()


