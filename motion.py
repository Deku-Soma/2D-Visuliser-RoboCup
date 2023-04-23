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
        playerData=loadJSONFile(1)
        self.MyPosition=playerData[0]['MyPosition']
        return playerData[0]['MyPosition']
    def getBallPosition():
        return self.BallPosition
    def getTeamMateDistanceToBall():
        return self.TeamMateDistanceToBall
    def getOpponentPositions():
        return self.OpponentPositions
    def getTeamMatePositions():
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
begin.start_timer
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
        playerData=loadJSONFile(i)
        currCoords=playerData[t]['MyPosition']
        nextCoords=playerData[t+3]['MyPosition']
        convCurrCoords= convert(currCoords[0],currCoords[1])
        convNextCoords= convert(nextCoords[0],nextCoords[1])
        canvas.move(playerIM[i],convNextCoords[0]-convCurrCoords[0], convNextCoords[1]-convCurrCoords[1] )
        win.update()
    t+=3
win.mainloop()


         


