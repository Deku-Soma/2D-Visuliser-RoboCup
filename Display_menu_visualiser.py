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
import math

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
    
def back_to_menu(gameFile):
    Frame_visualiser.grid_forget()
    Frame_menu.grid()
    del gameFile 
def go_to_visualiser(optvar):
    print(optvar.get())
    if optvar.get()>0 :
        Frame_menu.grid_forget()
        Frame_visualiser.grid()
    else:
        messagebox.showinfo("Warning", "You have not selected a game. \n Please selecte a game")

def update_visualiser():

    #Loads json files into array
    gameFile=motion.writeGlobalJSONFile(optvar.get())
    #back_menu_button = tk.Button(Frame_visualiser, text="Back", command=lambda: back_to_menu(gameFile))
    #back_menu_button.grid(row=0,column=0)


    #determines shortest gamelength
    gameLengthList=[]

    for i in range(11):
        
        playerData=gameFile[i]
        gameLengthList.append(len(playerData))
    print("Player " + str(i)+": " +str(gameLengthList[i]))
    
    gameLength= min(gameLengthList)
    
    #visualiser
    total=0
    playerview=11
    t=0
    nextT=0
    timer.speed_up=1
    tps= round(gameLength/(20*60))#sets amount of lines of log to cover per second
    while(timer.time_step<(20*60)):

        #displays player info
        playerInfo=gameFile[optPlayerInfovar.get()]
        
        playerdataValueBallPosition_label.configure(text=str(round(playerInfo[t]["BallPosition"][0],2))+" "+str(round(playerInfo[t]["BallPosition"][1],2)))
        playerdataValueMyPosition_label.configure(text=str(round(playerInfo[t]["MyPosition"][0],2))+" "+str(round(playerInfo[t]["MyPosition"][1],2)))
        for i in range(11):
            playerdataValueOppPosition_label[i].configure(text=str(round(playerInfo[t]["OpponentPositions"]["OPP"+str(i+1)][0],2))+" "+str(round(playerInfo[t]["OpponentPositions"]["OPP"+str(i+1)][1],2)))
            playerdataValueTeamDistance_label[i].configure(text=str(round(playerInfo[t]["TeamMateDistanceToBall"][str(i+1)],2)))
            playerdataValueTeamPosition_label[i].configure(text=str(round(playerInfo[t]["TeamMatePositions"]["TEAM"+str(i+1)][0],2))+" "+str(round(playerInfo[t]["OpponentPositions"]["OPP"+str(i+1)][1],2)))


        #time functions        
        tps= round(gameLength/(20*60))
        if t>gameLength or t+tps>gameLength:
            messagebox.showinfo("Game Over", "End of log file")
            break
            
        if timer.ticking==True and timer.rewind==False:
            nextT=tps*timer.speed_up
            timer.time_step+=1*timer.speed_up
            timer_label.configure(text=timer.format_time())
        elif timer.ticking==False:
            nextT=0
            timer_label.configure(text=timer.format_time())
        elif timer.rewind==True:
            nextT=-tps*timer.speed_up
            timer.time_step-=1*timer.speed_up
            timer_label.configure(text=timer.format_time())
        playerview=optPlayervar.get()    
        start=time.time()

        #player motion updates
        
        if playerview==11:#general view
                
    #calculates next and current coords based on average distance
            OpponentCurrCoords=motion.getAverageOpponentPosition(t,gameFile)
            OpponentNextCoords=motion.getAverageOpponentPosition(t+nextT,gameFile)
            BallCurrCoords=motion.getAverageBallPosition(t,gameFile)
            BallNextCoords=motion.getAverageBallPosition(t+nextT,gameFile)
                                                                                                               
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
        

    
        else:
                
            #selected player view   
            gameLength=gameLengthList[playerview]
            step=1200/gameLength
            playerData=gameFile[playerview]#retrieves log json file from array
            
            #update ball
            BallCurrCoords=playerData[t]["BallPosition"]
            BallNextCoords=playerData[t+nextT]["BallPosition"]
            convBallCurrCoords= motion.convert(BallCurrCoords[0],BallCurrCoords[1])
            convBallNextCoords= motion.convert(BallNextCoords[0],BallNextCoords[1])
            canvas_visualiser.move(ballIM,convBallNextCoords[0]-convBallCurrCoords[0], convBallNextCoords[1]-convBallCurrCoords[1] )

            #update team mate and opponent positions
            TeamMatePositionsPresent=playerData[t]['TeamMatePositions']
            TeamMatePositionsFuture=playerData[t+nextT]['TeamMatePositions']
            OpponentPositionsPresent=playerData[t]['OpponentPositions']
            OpponentPositionsFuture=playerData[t+nextT]['OpponentPositions']
                
            for x in range(11):
                    
                #update teammate position        
                TeamMateCurrentPosition=TeamMatePositionsPresent["TEAM" + str(x+1)]
                TeamMateNextPosition=TeamMatePositionsFuture["TEAM" + str(x+1)]
                convCurrCoords= motion.convert(TeamMateCurrentPosition[0],TeamMateCurrentPosition[1])
                convNextCoords= motion.convert(TeamMateNextPosition[0],TeamMateNextPosition[1])
                moveX=convNextCoords[0]-convCurrCoords[0]
                moveY=convNextCoords[1]-convCurrCoords[1]
                canvas_visualiser.move(playerIM[x],moveX,moveY)

                #update opponent position
                OpponentCurrentPosition=OpponentPositionsPresent["OPP" + str(x+1)]
                OpponentNextPosition=OpponentPositionsFuture["OPP" + str(x+1)]
                convCurrCoords= motion.convert(OpponentCurrentPosition[0],OpponentCurrentPosition[1])
                convNextCoords= motion.convert(OpponentNextPosition[0],OpponentNextPosition[1])
                moveX=convNextCoords[0]-convCurrCoords[0]
                moveY=convNextCoords[1]-convCurrCoords[1]
                canvas_visualiser.move(opponentIM[x],moveX,moveY)
                
            win.update()

        
        #timer functions
        if timer.ticking==True:
            if timer.rewind==True:
                t-=tps*timer.speed_up
                nextT=-tps*timer.speed_up
                timer.time_step-=1*timer.speed_up
                timer_label.configure(text=timer.format_time())
                if t<0:
                    t=0
                    nextT=tps
                    timer.time_step=0
                    timer_label.configure(text=timer.format_time())
                    timer.rewind=False
                    timer.speed_up=1
                if t+nextT<0:
                    t=0
                    nextT=tps
                    timer.time_step=0
                    timer_label.configure(text=timer.format_time())
                    timer.rewind=False
                    timer.speed_up=1
            else:
                t+=nextT*timer.speed_up
                timer.time_step+=1
                timer_label.configure(text=timer.format_time())
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
gameselection.menu.add_radiobutton(label = "WITS-FC_vs_WITS-GOTO", value=1,variable=optvar)
gameselection.menu.add_radiobutton(label = "WITS-FC_vs_WITS-FC", value=2,variable=optvar)
gameselection.menu.add_radiobutton(label = "WITS-FC_vs_STAND", value=3,variable=optvar) 
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
canvas_visualiser.grid(row=1,column=0)
# the relx and rely values are values between 0 and 1, 
# the x and y values specify the position of the top left corner of the frame
# used to place the frame on a percentace value on the screens x,y values
# basically if the x runs from 0-100 a relx=0,3 will place the center x of the frame at x = 30 (30% to the right of x =0)
# Anchor is the alignemnt of the frame
timer_label = tk.Label(Frame_visualiser, text=timer.format_time())
timer_label.grid(row=0,column=1)
start_button = tk.Button(Frame_visualiser, text="Start", command=timer.start_timer)
start_button.grid(row=10,column=0)
stop_button = tk.Button(Frame_visualiser, text="Pause", command=timer.stop_timer)
stop_button.grid(row=10,column=1)
rewind_button = tk.Button(Frame_visualiser, text="Rewind", command=timer.rewind_timer)
rewind_button.grid(row=10,column=2)
speedup_button = tk.Button(Frame_visualiser, text="Speed Up", command=timer.speedup_timer)
speedup_button.grid(row=11,column=1,columnspan=2)




optPlayervar=tk.IntVar(value=11)
playerselection = Menubutton(Frame_visualiser, text="Select perspective")
#gameselection.grid(row=3, column=4, padx=5, pady=5)
playerselection.menu = Menu(playerselection, tearoff=0)
playerselection["menu"] = playerselection.menu
# Create a dropdown Menu
for i in range(11):
    playerselection.menu.add_radiobutton(label = "Player "+ str(i+1), value=i,variable=optPlayervar,command=lambda:print(optPlayervar.get()))
playerselection.menu.add_radiobutton(label = "Average Player", value=11,variable=optPlayervar,command=lambda:print(optPlayervar.get()))
playerselection.grid(row=12,column=0)

#player info display
playerdata_label = tk.Label(Frame_visualiser)
playerdata_label.grid(column=3,row=0, padx=5, pady=5,rowspan=20)
playerdataFieldBallPosition_label = tk.Label(playerdata_label, text="BallPosition")
playerdataValueBallPosition_label=tk.Label(playerdata_label,text="Value")
playerdataFieldBallPosition_label.grid(column=1,row=1, padx=2, pady=5)
playerdataValueBallPosition_label.grid(column=2,row=1, padx=2, pady=5)
playerdataFieldMyPosition_label=tk.Label(playerdata_label, text="MyPosition")
playerdataValueMyPosition_label=tk.Label(playerdata_label,text="Value")
playerdataFieldMyPosition_label.grid(column=1,row=2, padx=2, pady=5)
playerdataValueMyPosition_label.grid(column=2,row=2, padx=2, pady=5)
playerdataOpponentPosition_label=tk.Label(playerdata_label, text="Opponent Position:")
playerdataOpponentPosition_label.grid(column=1,row=3,columnspan=2, padx=2, pady=5)
playerdataFieldOppPosition_label=[None]*11
playerdataValueOppPosition_label=[None]*11
for i in range(11):
    playerdataFieldOppPosition_label[i]=tk.Label(playerdata_label, text="OPP"+str(i+1))
    playerdataValueOppPosition_label[i]=tk.Label(playerdata_label, text="Value")
    playerdataFieldOppPosition_label[i].grid(column=1,row=4+i, pady=5)
    playerdataValueOppPosition_label[i].grid(column=2,row=4+i, padx=2, pady=5)

playerdataTeamMatePosition_label=tk.Label(playerdata_label, text="TeamMate Position:")
playerdataTeamMatePosition_label.grid(column=3,row=1,columnspan=2, padx=2, pady=5)
playerdataFieldTeamPosition_label=[None]*11
playerdataValueTeamPosition_label=[None]*11
for i in range(11):
    playerdataFieldTeamPosition_label[i]=tk.Label(playerdata_label, text="TEAM"+str(i+1))
    playerdataValueTeamPosition_label[i]=tk.Label(playerdata_label, text="Value")
    playerdataFieldTeamPosition_label[i].grid(column=3,row=2+i, pady=5)
    playerdataValueTeamPosition_label[i].grid(column=4,row=2+i, padx=2, pady=5)

playerdataTeamMateDistance_label=tk.Label(playerdata_label, text="TeamMate Distance:")
playerdataTeamMateDistance_label.grid(column=5,row=1,columnspan=2, padx=2, pady=5)
playerdataFieldTeamDistance_label=[None]*11
playerdataValueTeamDistance_label=[None]*11
for i in range(11):
    playerdataFieldTeamDistance_label[i]=tk.Label(playerdata_label, text="TEAM"+str(i+1))
    playerdataValueTeamDistance_label[i]=tk.Label(playerdata_label, text="Value")
    playerdataFieldTeamDistance_label[i].grid(column=5,row=2+i, pady=5)
    playerdataValueTeamDistance_label[i].grid(column=6,row=2+i, padx=2, pady=5)

optPlayerInfovar=tk.IntVar(value=0)
playerInfoselection = Menubutton(Frame_visualiser, text="Select Player Info")
#gameselection.grid(row=3, column=4, padx=5, pady=5)
playerInfoselection.menu = Menu(playerInfoselection, tearoff=0)
playerInfoselection["menu"] = playerInfoselection.menu
# Create a dropdown Menu
for i in range(11):
    playerInfoselection.menu.add_radiobutton(label = "Player "+ str(i+1), value=i,variable=optPlayerInfovar,command=lambda:print(optPlayervar.get()))
playerInfoselection.grid(row=13,column=0)
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
