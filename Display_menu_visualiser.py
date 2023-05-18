import tkinter as tk
from tkinter import messagebox
from tkinter import *
import os
from Team import *
from Field_Objects import *
import updatedmotion as motion
from PIL import ImageTk, Image
import time
import timesimple as ts

win = tk.Tk()

win.geometry("1200x800")  # aspect ratio
win.config(bg="green")  # background colour

frame_vis = False  # Bool for Frame Visualiser is packed

Frame_visualiser = tk.Frame(win, bg="black", width=1200, height=800)

#frameTimer = Frame(Frame_visualiser, width=50, height=20)
#frameTimer.grid(row=3,column=4)
#frameTimer.place(anchor=NW, relx=0.01, rely=0.01)

# Keresh please add in the Timer declaration max_ticks=Keresh_get_max_tick_function

timer = ts.Timer()

# ============================================================
# functions

def go_to_menu(event):
    Frame_welcome.grid_forget()
    Frame_menu.grid()
    

def go_to_visualiser(optvar):
    print(optvar.get())
    if optvar.get() == 1:
        Frame_menu.grid_forget()
        Frame_visualiser.grid()
    else:
        messagebox.showinfo("Warning", "You have not selected a game. \n Please selecte a game")

# Keresh You must add the motion to the update_visualiser function
def update_visualiser():
    
    #This increments the timer by 1
    gameFile=motion.writeGlobalJSONFile(optvar.get())
    # Keresh  add your part here
    # keresh_function(timer.time_step)

    #frameTimer.after(int(1000/(timer.speed_up * timer.tps)), update_visualiser)
    # Above Determines how long each tick in the game is gonna last
    gameLengthList=[]

    for i in range(11):
        
        playerData=gameFile[i]
        gameLengthList.append(len(playerData))
    print("Player " + str(i)+": " +str(gameLengthList[i]))
    
    gameLength= min(gameLengthList)
    
    #visualiser
    total=0
    playerview=0
    t=0
    nextT=0

    while(t<gameLength):
        if timer.ticking==True and timer.rewind==False:
            nextT=1*timer.speed_up
            timer.time_step+=1*timer.speed_up
            timer_label.configure(text=timer.format_time())
        elif timer.ticking==False:
            nextT=0
            timer_label.configure(text=timer.format_time())
        elif timer.rewind==True:
            nextT=-1*timer.speed_up
            timer.time_step-=1*timer.speed_up
            timer_label.configure(text=timer.format_time())
            
        start=time.time()
        if playerview==11:
                
                
                
                
                
    #calculates next and current coords based on average distance
            OpponentCurrCoords=motion.getAverageOpponentPosition(t,gameFile)
            OpponentNextCoords=motion.getAverageOpponentPosition(t+nextT,gameFile)
            BallCurrCoords=motion.getAverageBallPosition(t,gameFile)
            BallNextCoords=motion.getAverageBallPosition(t+NextT,gameFile)
                                                                                                               
    #converts coords to place accurately on soccer field
            convBallCurrCoords= motion.convert(BallCurrCoords[0],BallCurrCoords[1])
            convBallNextCoords= motion.convert(BallNextCoords[0],BallNextCoords[1])
    
    #moves ball element on canvas
            canvas_visualiser.move(ballIM,convBallNextCoords[0]-convBallCurrCoords[0], convBallNextCoords[1]-convBallCurrCoords[1] )
    
    # moves opponent and player images on canvas
            for i in range(11):
                    
                        
        #calculates distance to move player
                currCoords=gameFile[i][t]['MyPosition']
                nextCoords=gameFile[i][t+nextT]['MyPosition']
        
        #converts distances to place on soccer field
                convCurrCoords= motion.convert(currCoords[0],currCoords[1])
                convNextCoords= motion.convert(nextCoords[0],nextCoords[1])
                canvas_visualiser.move(playerIM[i],convNextCoords[0]-convCurrCoords[0], convNextCoords[1]-convCurrCoords[1] )

        #calculates distance to move opponent
                oppCurr=[OpponentCurrCoords[0][i],OpponentCurrCoords[1][i]]
                oppNext=[OpponentNextCoords[0][i],OpponentNextCoords[1][i]]

        #converts distance to move player
                convCurrCoords= motion.convert(oppCurr[0],oppCurr[1])
                convNextCoords=motion.convert(oppNext[0],oppNext[1])
                canvas_visualiser.move(opponentIM[i],convNextCoords[0]-convCurrCoords[0], convNextCoords[1]-convCurrCoords[1] )
        
            win.update()
        

    
    
    #update ticker
    
        else:
                
                
            gameLength=gameLengthList[playerview]
            step=1200/gameLength
            playerData=gameFile[playerview]
            BallCurrCoords=playerData[t]["BallPosition"]
            BallNextCoords=playerData[t+nextT]["BallPosition"]
            convBallCurrCoords= motion.convert(BallCurrCoords[0],BallCurrCoords[1])
            convBallNextCoords= motion.convert(BallNextCoords[0],BallNextCoords[1])
            canvas_visualiser.move(ballIM,convBallNextCoords[0]-convBallCurrCoords[0], convBallNextCoords[1]-convBallCurrCoords[1] )
            TeamMatePositionsPresent=playerData[t]['TeamMatePositions']
            TeamMatePositionsFuture=playerData[t+nextT]['TeamMatePositions']
            OpponentPositionsPresent=playerData[t]['OpponentPositions']
            OpponentPositionsFuture=playerData[t+nextT]['OpponentPositions']
                
            for x in range(11):
                    
                        
                        
                TeamMateCurrentPosition=TeamMatePositionsPresent["TEAM" + str(x+1)]
                TeamMateNextPosition=TeamMatePositionsFuture["TEAM" + str(x+1)]
                convCurrCoords= motion.convert(TeamMateCurrentPosition[0],TeamMateCurrentPosition[1])
                convNextCoords= motion.convert(TeamMateNextPosition[0],TeamMateNextPosition[1])
                moveX=convNextCoords[0]-convCurrCoords[0]
                moveY=convNextCoords[1]-convCurrCoords[1]
                canvas_visualiser.move(playerIM[x],moveX,moveY)
                OpponentCurrentPosition=OpponentPositionsPresent["OPP" + str(x+1)]
                OpponentNextPosition=OpponentPositionsFuture["OPP" + str(x+1)]
                convCurrCoords= motion.convert(OpponentCurrentPosition[0],OpponentCurrentPosition[1])
                convNextCoords= motion.convert(OpponentNextPosition[0],OpponentNextPosition[1])
                moveX=convNextCoords[0]-convCurrCoords[0]
                moveY=convNextCoords[1]-convCurrCoords[1]
                canvas_visualiser.move(opponentIM[x],moveX,moveY)
                
            win.update()
            end=time.time()
            delay=step-(end-start)
            if delay>0:
                    time.sleep(delay)
        
                #print(end-start)
        if timer.ticking==True:
            if timer.rewind==True:
                t-=1*timer.speed_up
                nextT=-1*timer.speed_up
                timer.time_step-=1*timer.speed_up
                timer_label.configure(text=timer.format_time())
                if t<0:
                    t=0
                    nextT=1
                    timer.time_step=0
                    timer_label.configure(text=timer.format_time())
                    timer.rewind=False
                if t+nextT<0:
                    t=0
                    nextT=1
                    timer.time_step=0
                    timer_label.configure(text=timer.format_time())
                    timer.rewind=False
            else:
                t+=1*timer.speed_up
        else:
            t+=0
            nextT=0



# =============================================================
Frame_welcome = tk.Frame(win, bg="blue", width=1200, height=800)
# =============================================================
# welcome frame components
canvas = tk.Canvas(Frame_welcome, bg="black", width=1200, height=800)

welcomeFile = "robocub2-resize.jpg"
menu_button_file = "menu_button.png"
folder = "Assets"

cwd = os.getcwd()

path_to_welcome_file = os.path.join(cwd, folder, welcomeFile)
path_to_menu_button_file = os.path.join(cwd, folder, menu_button_file)

welcomeIm = Image.open(path_to_welcome_file)
welcomeIm = welcomeIm.resize((1000, 800), Image.LANCZOS)
welcomeImObject = ImageTk.PhotoImage(welcomeIm)

menu_buttonIM = Image.open(path_to_menu_button_file)
menu_buttonIM = menu_buttonIM.resize((200, 75), Image.LANCZOS)
menu_buttonIMobject = ImageTk.PhotoImage(menu_buttonIM)

welcomebg = canvas.create_image(0, 0, image=welcomeImObject, anchor="nw")

menu_buttonbg = canvas.create_image(400, 500, image=menu_buttonIMobject, anchor="nw")
canvas.tag_bind(menu_buttonbg, "<Button-1>", go_to_menu)
canvas.grid()
Frame_welcome.grid()
# =============================================================
Frame_menu = tk.Frame(win, bg="black", width=1200, height=800)
# =============================================================
# create canvas for menu
canvas_menu = tk.Canvas(Frame_menu, width=1200, height=800)
menubgfile = "menubg.jpg"
path_to_menu_bg = os.path.join(cwd, folder, menubgfile)

menubgIm = Image.open(path_to_menu_bg)
menubgIm = menubgIm.resize((1200, 800), Image.LANCZOS)

#menubg = canvas_menu.create_image(0, 0, image=menubgIMobject, anchor="nw")
l=tk.Label(Frame_menu)
l.image = ImageTk.PhotoImage(menubgIm)
l.config(image=l.image)
l.place(x=0,y=0,relwidth=1,relheight=1)
#canvas_menu.grid()
# button to go to visualiser
'''visualiser_button_file = "match_button.png"
path_to_visualiser_button = os.path.join(cwd, folder, visualiser_button_file)
visualiser_buttonIM = Image.open(path_to_visualiser_button)
visualiser_buttonIM = visualiser_buttonIM.resize((200, 75), Image.LANCZOS)
visualiser_buttonIMobject = ImageTk.PhotoImage(visualiser_buttonIM)
visualiser_buttonbg = canvas_menu.create_image(400, 500, image=visualiser_buttonIMobject, anchor="nw")'''
# menu frame components
label_menu = tk.Label(l, text="Welcome to the RoboCup Visualiser", font=50, bg="blue", fg="white")
label_menu.place(x=400,y=0)
optvar=tk.IntVar(value=1)
gameselection = Menubutton(l, text="Select a game")
#gameselection.grid(row=3, column=4, padx=5, pady=5)
gameselection.menu = Menu(gameselection, tearoff=0)
gameselection["menu"] = gameselection.menu
# Create a dropdown Menu
gameselection.menu.add_radiobutton(label = "Game 1", value=1,variable=optvar,command=lambda:print(optvar.get()))
gameselection.menu.add_radiobutton(label = "Game 2", value=2,variable=optvar,command=lambda:print(optvar.get())) 
gameselection.place(x=400,y=400)



# canvas_menu.tag_bind(visualiser_buttonbg, "<Button-1>", go_to_visualiser)

start_game_button = tk.Button(l, text="start", command=lambda: [go_to_visualiser(optvar), update_visualiser()])

#start_game_button.grid(row=9,column=4)
start_game_button.place(x=400,y=500)
#canvas_menu.grid(row=0,column=0,columnspan=4,rowspan=4)

#win.update()
field_file = "Soccer_Field_HD-downsized.png"

folder = "Assets"

cwd = os.getcwd()

path_to_field_file = os.path.join(cwd, folder, field_file)
# Create a field object that taks up 75% of total screen space
fieldimage = ImageTk.PhotoImage(file=path_to_field_file)
width, height = fieldimage.width(), fieldimage.height()
# fetchs field image, note the field image must be in the same folder for this function to work
  # resize the field image so it matches the desired aspect ratio
 # this variable is used to create a viable image object that can be called\



# =============================================================
# visualiser screen
# creating the frams that will be used to place all the elements of the gui design

# this is the frame that is set to house the field image and is already set to 75% of screen space
canvas_visualiser = Canvas(Frame_visualiser, bg="black", width=width, height=height)
canvas_visualiser.grid(row=1,column=2)
# the relx and rely values are values between 0 and 1, 
# the x and y values specify the position of the top left corner of the frame
# used to place the frame on a percentace value on the screens x,y values
# basically if the x runs from 0-100 a relx=0,3 will place the center x of the frame at x = 30 (30% to the right of x =0)
# Anchor is the alignemnt of the frame
timer_label = tk.Label(Frame_visualiser, text=timer.format_time())
timer_label.grid(row=0,column=2)
start_button = tk.Button(Frame_visualiser, text="Start", command=timer.start_timer)
start_button.grid(row=10,column=0)
stop_button = tk.Button(Frame_visualiser, text="Pause", command=timer.stop_timer)
stop_button.grid(row=10,column=1)
rewind_button = tk.Button(Frame_visualiser, text="Rewind", command=timer.rewind_timer)
rewind_button.grid(row=10,column=2)
speedup_button = tk.Button(Frame_visualiser, text="Speed Up", command=timer.speedup_timer)
speedup_button.grid(row=10,column=3)
'''time_button_frame = Frame(Frame_visualiser, width=200, height=50, )
time_button_frame.pack()
time_button_frame.place(anchor=N, relx=0.5, rely=0.9)
'''
# frame for timer 


# ===============================================================================================================


# create image objects
fieldIM = canvas_visualiser.create_image(0, 0, image=fieldimage, anchor=NW)

# ================================================================================================================
# Create a Label Widget to display the field
# ================================================================================================================
#  image is used to represent a player and serve as an example to visualise the cooridnate system
# refer to the Co-ordinate system for soccer field tect file

player1_file = "nonselectedplayer1.png"
player2_file = "nonselectedplayer2.png"
ball_file="soccerball-removebg-preview.png"
folder = "Assets"

cwd = os.getcwd()

path_to_player1_file = os.path.join(cwd, folder, player1_file)
path_to_player2_file = os.path.join(cwd, folder, player2_file)
path_to_ball_file = os.path.join(cwd, folder, ball_file)

playerimage= ImageTk.PhotoImage(file=path_to_player1_file)
opponentimage= ImageTk.PhotoImage(file=path_to_player2_file)
ballimage= ImageTk.PhotoImage(file=path_to_ball_file)


# =================================================================================================================
#places opponents and players on canvas
playerIM=[None]*12
opponentIM=[None]*12
playerData=motion.loadJSONFile(1,1)
TeamMatePositionsPresent=playerData[0]['TeamMatePositions']
OpponentPositionsPresent=playerData[0]['OpponentPositions']
for i in range(11):
    TeamMateCurrentPosition=TeamMatePositionsPresent["TEAM" + str(i+1)]
    OpponentCurrentPosition=OpponentPositionsPresent["OPP" + str(i+1)]
    convCoords= motion.convert(TeamMateCurrentPosition[0],TeamMateCurrentPosition[1])
    playerIM[i]=canvas_visualiser.create_image(convCoords[0],convCoords[1], image=playerimage, anchor=NW)  
    convCoords= motion.convert(OpponentCurrentPosition[0],OpponentCurrentPosition[1])
    opponentIM[i]=canvas_visualiser.create_image(convCoords[0],convCoords[1], image=opponentimage, anchor=NW)


    

#places ball on canvas
BallCurrCoords=playerData[0]["BallPosition"]
convBallCoords= motion.convert(BallCurrCoords[0],BallCurrCoords[1])
ballIM=canvas_visualiser.create_image(convBallCoords[0],convBallCoords[1], image=ballimage , anchor=NW)
del playerData


# =================================================================================================================

#   creating test buttons for GUI design purposes, these buttons will later be changed to match the desired effects
#   as of right now these buttons have no effect (change this list as buttons are implemeneted)
'''buttonPlay = Button(time_button_frame, text = "Pause/player",bg="grey") #not initiated yet
buttonRewind = Button(time_button_frame, text= "Rewind",bg="grey")# not initiated yet
buttonForward = Button(time_button_frame,text = "Forward",bg="grey")# not initiated yet
buttonRewind.pack(side=LEFT) # used the side property to place the buttons next to each other.
buttonPlay.pack(side=LEFT)
buttonForward.pack(side=LEFT)
#=================================================================================================================
# label for timer 
labelTimer = Label(frameTimer,text ="00:00",bg="grey",padx=5 )
labelTimer.pack()'''

win.mainloop()
