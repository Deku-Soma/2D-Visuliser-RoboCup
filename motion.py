import json
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import Canvas, NW

def loadJSONFile(PlayerNum):
        jsondata=[]
        f=open(str(PlayerNum)+'.json','r')
        for line in f:
            jsondata.append(json.loads(line))
        return jsondata
def convertCoords(xcoord,ycoord):
        coordsConverted=[]
        x= 500+ (xcoord*60.33)
        y=400+(ycoord*70.5)
        coordsConverted.append(x)
        coordsConverted.append(y)
        return coordsConverted
def convertCoordArray(coord):
        coordsConverted=[]
        x= 500+ (coord[0]*60.33)
        y=400+(coord[1]*70.5)
        coordsConverted.append(x)
        coordsConverted.append(y)
        return coordsConverted

def convert(xco,yco):
    x=0
    y=0
    x=(xco*30.3333)+500
    y=(yco*35.5)+400-30
    ans=[]
    ans.append(x)
    ans.append(y)
    return ans

# Define the ParseData class and other functions as before

class ParseData:
    def __init__(self, Player):
        self.Player= Player
        self.BallPosition=[]
        self.MyPosition=[]
        self.OpponentPositions=[]
        self.TeamMatePositions=[]
        self.TeamMateDistanceToBall=[]

    def initialGameState(self,PlayerNum): 
        playerData= loadJSONFile(PlayerNum)
        self.Player=PlayerNum
        self.BallPosition=playerData[0]['BallPosition']
        self.OpponentPositions=playerData[0]['OpponentPositions']
        self.TeamMatePositions=playerData[0]['TeamMatePositions']
        self.MyPosition=playerData[0]['MyPosition']
        self.TeamMateDistanceToBall=playerData[0]['TeamMateDistanceToBall']
            
    def setGameState(self,PlayerNum,TimeInterval):
        playerData=loadJSONFile(PlayerNum)
        self.Player=PlayerNum
        self.BallPosition=playerData[TimeInterval]['BallPosition']
        self.MyPosition=playerData[TimeInterval]['MyPosition']
        self.TeamMateDistanceToBall=playerData[TimeInterval]['TeamMateDistanceToBall']
        self.OpponentPositions=playerData[TimeInterval]['OpponentPositions']
        self.TeamMatePositions=playerData[TimeInterval]['TeamMatePositions']

    def getMyPosition():
        playerData = loadJSONFile(1)
        myPosition = playerData[0]['MyPosition']
        return myPosition
    
    def getBallPosition(self):
        return self.BallPosition
    def getTeamMateDistanceToBall(self):
        return self.TeamMateDistanceToBall
    def getOpponentPositions(self):
        return self.OpponentPositions
    def getTeamMatePositions(self):
        return self.TeamMatePositions
    def __str__(self):
        return f"Player: {self.Player} BallPosition: {self.BallPosition} MyPosition: {self.MyPosition} TeamMateDistanceToBall: {self.TeamMateDistanceToBall} OpponentPositions: {self.OpponentPositions} TeamMatePositions: {self.TeamMatePositions}"
    

# Create the main window and canvas as before
win = tk.Tk()
fieldimage = ImageTk.PhotoImage(file="horizontal_field.png")
playerimage= ImageTk.PhotoImage(file="nonselectedplayer1-removebg-smaller.png")
width, height = fieldimage.width(), fieldimage.height()
canvas = Canvas(win, bg="white", width=width, height=height)
canvas.pack()
fieldIM = canvas.create_image(0, 0, image=fieldimage, anchor=NW)

# Load the player data
player_data = {}
for i in range(1, 12):
    player_data[i] = loadJSONFile(i)

# Create the player images
playerIM = {}
for i in range(1, 12):
    playerIM[i] = canvas.create_image(0, 0, image=playerimage, anchor=NW)

# Define the animation loop
def animate(frame):
    for i in range(1, 12):
        curr_coords = player_data[i][frame]['MyPosition']
        next_coords = player_data[i][frame+3]['MyPosition']
        conv_curr_coords = convert(curr_coords[0], curr_coords[1])
        conv_next_coords = convert(next_coords[0], next_coords[1])
        canvas.move(playerIM[i], conv_next_coords[0]-conv_curr_coords[0], conv_next_coords[1]-conv_curr_coords[1])
    win.update()

# Define the control functions
def rewind():
    global frame
    frame = max(0, frame-10)
    update_frame()

def pause():
    global paused
    paused = not paused

def speedup():
    global speed
    speed = min(3, speed+1)

def update_frame():
    canvas.after_cancel(after_id)
    if not paused:
        animate(frame)
        frame += 3*speed
    after_id = canvas.after(1000//30, update_frame)

# Initialize the frame, paused and speed variables
frame = 0
paused = False
speed = 1

begin= Timer(win)
begin.start_timer
#while(begin.remaining>0):
 #   for i in range(1,12):
  #      playerData=loadJSONFile(i)
   #     myCoords=playerData[20*90-begin.remaining]['MyPosition']
    #    convCoords= convert(myCoords[0],myCoords[1])
     #   canvas.move(playerIM[i],myCoords[0]-playerData[20*90-begin.remaining-3]['MyPosition'][0], myCoords[1]-playerData[20*90-begin.remaining-3]['MyPosition'][1] )
      #  win.update()

# Create the control panel and buttons
control_panel = tk.Frame(win)
rewind_button = tk.Button(control_panel, text="Rewind", command=rewind)
pause_button = tk.Button(control_panel, text="Pause", command=pause)
speedup_button = tk.Button(control_panel, text="Speed Up", command=speedup)
rewind_button.pack(side=tk.LEFT)
pause_button.pack(side=tk.LEFT)
speedup_button.pack(side=tk.LEFT)
control_panel.pack()

# Start the animation loop
after_id = canvas.after(0, update_frame)

win.mainloop()
