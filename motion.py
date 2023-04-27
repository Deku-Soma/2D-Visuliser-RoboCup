import json
from tkinter import Tk, Canvas, NW
from PIL import ImageTk, Image
import tkinter as tk



def loadJSONFile(PlayerNum):
        jsondata=[]
        f=open(str(PlayerNum)+'.json','r')
        for line in f:
            jsondata.append(json.loads(line))
        f.close()
        return jsondata


def convert(xco,yco):
    x=0
    y=0
 
    x=(xco*30.3333)+500
    y=(yco*35.5)+400-30
    ans=[]
    ans.append(x)
    ans.append(y)
    return ans
    

def getAverageOpponentPosition(t):
    playerData=loadJSONFile(1)
    OpponentAvgPos=playerData[t]['OpponentPositions']
    for j in range(1,12):
        OpponentAvgPos["OPP" + str(j)][0]=0
        OpponentAvgPos["OPP" + str(j)][1]=0
   
    for i in range(1,12):
        playerData=loadJSONFile(i)
        OpponentPositions=playerData[t]['OpponentPositions']
        for j in range(1,12):
            OpponentAvgPos["OPP" + str(j)][0]= OpponentAvgPos["OPP" + str(j)][0] + OpponentPositions["OPP" + str(j)][0]
            OpponentAvgPos["OPP" + str(j)][1]= OpponentAvgPos["OPP" + str(j)][1] + OpponentPositions["OPP" + str(j)][1]
    for i in range(1,12):
        OpponentAvgPos["OPP" + str(i)][0]=(OpponentAvgPos["OPP" + str(i)][0]/(11))
        OpponentAvgPos["OPP" + str(i)][1]=(OpponentAvgPos["OPP" + str(i)][1]/(11))
    return OpponentAvgPos


def getAverageBallPosition(t):
    playerData=loadJSONFile(1)
    avgBallPos= playerData[t]['BallPosition']
    avgBallPos[0]=0
    avgBallPos[1]=0
    for i in range(1,12):
        playerData=loadJSONFile(i)
        BallPosition=playerData[t]['BallPosition']
        avgBallPos[0]=avgBallPos[0]+BallPosition[0]
        avgBallPos[1]=avgBallPos[1]+BallPosition[1]
    avgBallPos[0]= avgBallPos[0]/11
    avgBallPos[1]=avgBallPos[1]/11
    return avgBallPos

        
def changePerspective(canvas,playerIM,i,t):
    playerData=loadJSONFile(i)
    while (t<20*60):
        TeamMatePositionsPresent=playerData[t]['TeamMatePositions']#whole team
        TeamMatePositionsFuture=playerData[t+3]['TeamMatePositions']
        for x in range(1,12):
            if i==x:
                currCoords=playerData[t]['MyPosition']
                nextCoords=playerData[t+3]['MyPosition']
                convCurrCoords= convert(currCoords[0],currCoords[1])
                convNextCoords= convert(nextCoords[0],nextCoords[1])
                moveX=convNextCoords[0]-convCurrCoords[0]
                moveY=convNextCoords[1]-convCurrCoords[1]
                canvas.move(playerIM[x],moveX,moveY  )
                win.update()
            else:
                
                TeamMateCurrentPosition=TeamMatePositionsPresent["TEAM" + str(x)]
                TeamMateNextPosition=TeamMatePositionsFuture["TEAM" + str(x)]
                convCurrCoords= convert(TeamMateCurrentPosition[0],TeamMateCurrentPosition[1])
                convNextCoords= convert(TeamMateNextPosition[0],TeamMateNextPosition[1])
                moveX=convNextCoords[0]-convCurrCoords[0]
                moveY=convNextCoords[1]-convCurrCoords[1]
                canvas.move(playerIM[x],moveX,moveY  )
                win.update()
        t+=3



win = Tk()
t=0
fieldimage = ImageTk.PhotoImage(file="horizontal_field.png")
playerimage= ImageTk.PhotoImage(file="nonselectedplayer1-removebg-smaller.png")
opponentimage= ImageTk.PhotoImage(file="nonselectedplayer2-removebg.png")
ballimage= ImageTk.PhotoImage(file="soccerball-removebg-preview.png")

#set canvas
width, height = fieldimage.width(), fieldimage.height()


canvas = Canvas(win, bg="white", width=width, height=height)
canvas.pack()
#create image objects 
fieldIM=canvas.create_image(0, 0, image=fieldimage, anchor=NW)

playerIM=[None]*12
opponentIM=[None]*12
for i in range(1,12):
    playerData=loadJSONFile(i)
    myCoords=playerData[0]['MyPosition']
    convCoords= convert(myCoords[0],myCoords[1])
    playerIM[i]=canvas.create_image(convCoords[0],convCoords[1], image=playerimage, anchor=NW)

OpponentCoords=getAverageOpponentPosition(0)
for i in range(1,12):
    oppCurr=OpponentCoords["OPP" + str(i)]
    convCoords= convert(oppCurr[0],oppCurr[1])
    opponentIM[i]=canvas.create_image(convCoords[0],convCoords[1], image=opponentimage, anchor=NW)
    #canvas.tag_bind(playerIM[i],"<Button-1>", changePerspective(canvas,playerIM,i,t))

BallCoords=getAverageBallPosition(0)
convBallCoords= convert(BallCoords[0],BallCoords[1])

ballIM=canvas.create_image(convBallCoords[0],convBallCoords[1], image=ballimage, anchor=NW)    
                

while (t<20*60):
    OpponentCurrCoords=getAverageOpponentPosition(t)
    OpponentNextCoords=getAverageOpponentPosition(t+9)
    BallCurrCoords=getAverageBallPosition(t)
    BallNextCoords=getAverageBallPosition(t+9)
    convBallCurrCoords= convert(BallCurrCoords[0],BallCurrCoords[1])
    convBallNextCoords= convert(BallNextCoords[0],BallNextCoords[1])
    canvas.move(ballIM,convBallNextCoords[0]-convBallCurrCoords[0], convBallNextCoords[1]-convBallCurrCoords[1] )
    win.update()
    for i in range(1,12):
        playerData=loadJSONFile(i)
        currCoords=playerData[t]['MyPosition']
        nextCoords=playerData[t+9]['MyPosition']
        convCurrCoords= convert(currCoords[0],currCoords[1])
        convNextCoords= convert(nextCoords[0],nextCoords[1])
        canvas.move(playerIM[i],convNextCoords[0]-convCurrCoords[0], convNextCoords[1]-convCurrCoords[1] )
        win.update()
    for i in range(1,12):
        oppCurr=OpponentCurrCoords["OPP" + str(i)]
        oppNext=OpponentNextCoords["OPP" + str(i)]
        
        convCurrCoords= convert(oppCurr[0],oppCurr[1])
        convNextCoords=convert(oppNext[0],oppNext[1])
        canvas.move(opponentIM[i],convNextCoords[0]-convCurrCoords[0], convNextCoords[1]-convCurrCoords[1] )
        win.update()
    t+=9
win.mainloop()


         


