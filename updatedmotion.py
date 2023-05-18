import json
from tkinter import Tk, Canvas, NW
from PIL import ImageTk, Image
import tkinter as tk
import statistics 
import time
import os

#Loads single json file
#Can be used to store file as an object
#Arguments:
#match- Integer(takes match number which is directory to file named match1 or match2 which is a folder that stores the json files)
#PlayerNum( takes num of json file) -Integer
def loadJSONFile(match, PlayerNum):
        folder="match"+str(match)
        cwd = os.getcwd()
        path_to_json_file = os.path.join(cwd, folder, str(PlayerNum))
        jsondata=[]
        f=open(path_to_json_file+'.json','r')
        for line in f:
            jsondata.append(json.loads(line))
        f.close()
        return jsondata

#Loads all json files in folder
#Example of folder match1
#Can be used to store all json filse as an object in an array
#Arguments:
#match- integer (takes match number which is directory to file named match1 or match2 which is a folder that stores the json files)
def writeGlobalJSONFile(match):
        total=0
        folder="match"+str(match)
        cwd = os.getcwd()        
        globaldata=[]
        jsondata=[]
        start=time.time()
        for i in range(1,12):
                jsondata=[]
                path_to_json_file = os.path.join(cwd, folder,str(i))
                f= open(path_to_json_file+'.json','r')
                for line in f:
                        jsondata.append(json.loads(line))
                f.close()
                globaldata.append(jsondata)
        end=time.time()
        print("-------------------")
        print("Total loadtime: "+ str(end-start))
        print("-------------------")
        return globaldata
#Converts coordinates in json file to coordinates of the field
#Arguments:
#xco: float, x-coordinate of element
#yco-float, y-coordinate of element
def convert(xco,yco):
    x=0
    y=0
 
    x=(xco*30.3333)+500
    y=(yco*35.5)+400-30
    ans=[]
    ans.append(x)
    ans.append(y)
    return ans
    
#Returns array of all average opponent position at time step t
#Arguments:
#t- integer, time step
#playerDataList- Array of all json files
def getAverageOpponentPosition(t,playerDataList):
    oppAvgxPos=[None]*11
    oppAvgyPos=[None]*11
    for i in range(11):
            oppAvgxPos[i]=[None]*11
            oppAvgyPos[i]=[None]*11
   
    for j in range(11):
        for i in range(11):
            playerData=playerDataList[i]
            oppAvgxPos[j][i]=(playerData[t]['OpponentPositions']["OPP" + str(j+1)][0])
            oppAvgyPos[j][i]=(playerData[t]['OpponentPositions']["OPP" + str(j+1)][1])
    oppxPos=[]
    oppyPos=[]
    for i in range(11):
            
            oppxPos.append(statistics.fmean(oppAvgxPos[i]))
            oppyPos.append(statistics.fmean(oppAvgyPos[i]))
    oppAvgPos=[oppxPos,oppyPos]        
    return oppAvgPos

#Returns average ball position at time step
#Arguments:
#t-integer, timestep i.e current line in json file
#playerDataList- Array of all json files
def getAverageBallPosition(t,playerDataList):
    avgBallxPos=[None]*11
    avgBallyPos=[None]*11
    for i in range(11):
        playerData=playerDataList[i]
        avgBallxPos[i]=playerData[t]['BallPosition'][0]
        avgBallyPos[i]=playerData[t]['BallPosition'][1]
    avgBallPos=[statistics.fmean(avgBallxPos),statistics.fmean(avgBallyPos)]
    return avgBallPos
        

#intitialise canvas
win = Tk()
t=0
fieldimage = ImageTk.PhotoImage(file="horizontal_field.png")
playerimage= ImageTk.PhotoImage(file="nonselectedplayer1-removebg.png")
opponentimage= ImageTk.PhotoImage(file="nonselectedplayer2-removebg.png")
ballimage= ImageTk.PhotoImage(file="soccerball-removebg-preview.png")

#set canvas
width, height = fieldimage.width(), fieldimage.height()


canvas = Canvas(win, bg="white", width=width, height=height)
canvas.pack()
#create image objects 
fieldIM=canvas.create_image(0, 0, image=fieldimage, anchor=NW)
test=writeGlobalJSONFile(1) #stores all json files of match1

#places opponents and players on canvas
playerIM=[None]*12
opponentIM=[None]*12
for i in range(11):
    playerData=test[i]
    myCoords=playerData[0]['MyPosition']
    convCoords= convert(myCoords[0],myCoords[1])
    playerIM[i]=canvas.create_image(convCoords[0],convCoords[1], image=playerimage, anchor=NW)  
OpponentCoords=getAverageOpponentPosition(0,test)
for i in range(11):
    oppCurr=[OpponentCoords[0][i],OpponentCoords[1][i]]
    convCoords= convert(oppCurr[0],oppCurr[1])
    opponentIM[i]=canvas.create_image(convCoords[0],convCoords[1], image=opponentimage, anchor=NW)


#places ball on canvas
BallCoords=getAverageBallPosition(0,test)
convBallCoords= convert(BallCoords[0],BallCoords[1])
ballIM=canvas.create_image(convBallCoords[0],convBallCoords[1], image=ballimage, anchor=NW)    

#Gets shortest game length file
gameLengthList=[]
print(" ")
print("Game Length List:")
for i in range(11):
    playerData=test[i]
    gameLengthList.append(len(playerData))
    print("Player " + str(i)+": " +str(gameLengthList[i]))  
gameLength= min(gameLengthList)
print(" ")
print("-------------------")
print("Minimum Game Length: "+ str(gameLength))
print("-------------------")
print(" ")

#visualiser
total=0
while (t<gameLength):
    start=time.time()
    #calculates next and current coords based on average distance
    OpponentCurrCoords=getAverageOpponentPosition(t,test)
    OpponentNextCoords=getAverageOpponentPosition(t+1,test)
    BallCurrCoords=getAverageBallPosition(t,test)
    BallNextCoords=getAverageBallPosition(t+1,test)
    
    #converts coords to place accurately on soccer field
    convBallCurrCoords= convert(BallCurrCoords[0],BallCurrCoords[1])
    convBallNextCoords= convert(BallNextCoords[0],BallNextCoords[1])
    
    #moves ball element on canvas
    canvas.move(ballIM,convBallNextCoords[0]-convBallCurrCoords[0], convBallNextCoords[1]-convBallCurrCoords[1] )
    win.update()
    
    # moves opponent and player images on canvas
    for i in range(11):
        #calculates distance to move player
        currCoords=test[i][t]['MyPosition']
        nextCoords=test[i][t+1]['MyPosition']
        
        #converts distances to place on soccer field
        convCurrCoords= convert(currCoords[0],currCoords[1])
        convNextCoords= convert(nextCoords[0],nextCoords[1])
        canvas.move(playerIM[i],convNextCoords[0]-convCurrCoords[0], convNextCoords[1]-convCurrCoords[1] )

        #calculates distance to move opponent
        oppCurr=[OpponentCurrCoords[0][i],OpponentCurrCoords[1][i]]
        oppNext=[OpponentNextCoords[0][i],OpponentNextCoords[1][i]]

        #converts distance to move player
        convCurrCoords= convert(oppCurr[0],oppCurr[1])
        convNextCoords=convert(oppNext[0],oppNext[1])
        canvas.move(opponentIM[i],convNextCoords[0]-convCurrCoords[0], convNextCoords[1]-convCurrCoords[1] )
        win.update()
    end=time.time()
    #update ticker
    t+=1
win.mainloop()


         


