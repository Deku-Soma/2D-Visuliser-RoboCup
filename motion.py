import json
from tkinter import Tk, Canvas, NW
from PIL import ImageTk, Image
import tkinter as tk



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
import json
from tkinter import Tk, Canvas, NW, Button
from PIL import ImageTk, Image
import tkinter as tk

class Timer:
    def __init__(self, master):
        self.remaining = 0
        self.paused = False
        self.speed = 1
        self.master = master
        self.label = tk.Label(master, text="00:00")
        self.label.pack()
        self.update_timer()
        
    def start_timer(self, remaining=None):
        if remaining:
            self.remaining = remaining
        self.paused = False
        self.update_timer()
        
    def pause_timer(self):
        self.paused = True
        
    def speedup_timer(self):
        self.speed += 1
        
    def rewind_timer(self):
        self.remaining = 0
        
    def update_timer(self):
        if not self.paused:
            self.remaining -= self.speed
            if self.remaining <= 0:
                self.remaining = 0
                return
            minutes = self.remaining // 60
            seconds = self.remaining % 60
            self.label.configure(text="%02d:%02d" % (minutes, seconds))
        self.master.after(1000, self.update_timer)

class PlayerVisualizer:
    def __init__(self, player_num):
        self.canvas = Canvas(win, bg="white", width=width, height=height)
        self.canvas.pack()
        self.fieldimage = ImageTk.PhotoImage(file="horizontal_field.png")
        self.playerimage = ImageTk.PhotoImage(file="nonselectedplayer1-removebg-smaller.png")
        self.fieldIM = self.canvas.create_image(0, 0, image=self.fieldimage, anchor=NW)
        self.playerIM = []
        self.parse_data = ParseData(player_num)
        self.parse_data.initialGameState(player_num)
        for i in range(12):
            self.playerIM.append(self.canvas.create_image(0, 0, image=self.playerimage, anchor=NW))
        self.update_players()
        
    def update_players(self):
        myCoords = self.parse_data.getMyPosition()
        convCoords = convert(myCoords[0], myCoords[1])
        self.canvas.move(self.playerIM[self.parse_data.Player], convCoords[0] - self.parse_data.MyPositionIM[0], convCoords[1] - self.parse_data.MyPositionIM[1])
        self.parse_data.MyPositionIM = convCoords
        for i in range(1, 12):
            if i == self.parse_data.Player:
                continue
            pos = self.parse_data.getOpponentPosition(i)
            if pos is None:
                continue
            convCoords = convert(pos[0], pos[1])
            self.canvas.move(self.playerIM[i], convCoords[0] - self.parse_data.OpponentPositionsIM[i-1][0], convCoords[1] - self.parse_data.OpponentPositionsIM[i-1][1])
            self.parse_data.OpponentPositionsIM[i-1] = convCoords
        self.canvas.update()
        
    def update_player_positions(self, time_interval):
        self.parse_data.setGameState(self.parse_data.Player, time_interval)
        self.update_players()
    
class ParseData:
    def __init__(self, Player):
        self.Player= Player
        self.BallPosition=[]
        self.MyPosition=[]
        self.OpponentPositions=[]
        self.TeamMatePositions=[]
        self.TeamMateDistanceToBall=[]

    def initialGameState(self,PlayerNum): 
        playerData= self.loadJSONFile(PlayerNum)
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

    
    def getMyPosition(self):
        playerData=loadJSONFile(1)
        self.MyPosition=playerData[0]['MyPosition']
        return playerData[0]['MyPosition']
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
    

win = Tk()
fieldimage = ImageTk.PhotoImage(file="horizontal_field.png")
playerimage= ImageTk.PhotoImage(file="nonselectedplayer1-removebg-smaller.png")

#set canvas
width, height = fieldimage.width(), fieldimage.height()


canvas = Canvas(win, bg="white", width=width, height=height)
canvas.pack()
#create image objects 
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
    playerIM[i]=canvas.create_image(convCoords[0],convCoords[1], image=playerimage, anchor=NW)


begin= Timer(win)
begin.start_timer()
#while(begin.remaining>0):
 #   for i in range(1,12):
  #      playerData=loadJSONFile(i)
   #     myCoords=playerData[20*90-begin.remaining]['MyPosition']
    #    convCoords= convert(myCoords[0],myCoords[1])
     #   canvas.move(playerIM[i],myCoords[0]-playerData[20*90-begin.remaining-3]['MyPosition'][0], myCoords[1]-playerData[20*90-begin.remaining-3]['MyPosition'][1] )
      #  win.update()
t=0

while (t<20*60):
    
    for i in range(1,12):
        Player=loadJSONFile(i)
        currCoords=playerData[t]['MyPosition']
        nextCoords=playerData[t+3]['MyPosition']
        convCurrCoords= convert(currCoords[0],currCoords[1])
        convNextCoords= convert(nextCoords[0],nextCoords[1])
        canvas.move(playerIM[i],convNextCoords[0]-convCurrCoords[0], convNextCoords[1]-convCurrCoords[1] )
        win.update()
    t+=3
win.mainloop()
