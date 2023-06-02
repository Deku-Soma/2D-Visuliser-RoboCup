import json
from tkinter import Tk, Canvas, NW
from PIL import ImageTk, Image
import tkinter as tk
import statistics 
import time
import os
import math


#Loads single json file
#Can be used to store file as an object
#Arguments:
#match- Integer(takes match number which is directory to file named match1 or match2 which is a folder that stores the json files)
#PlayerNum( takes num of json file) -Integer
def loadJSONFile(match, PlayerNum):
        folder="matches"+ os.path.sep +"match"+str(match)
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
        folder="matches"+ os.path.sep +"match"+str(match)
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
 
    x=(xco*24.6667)+395-10
    y=(yco*23.5)+250-10
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

def generateGeneralView(var):
        folder="matches\match"+str(var)
        cwd = os.getcwd()
        path_to_json_file = os.path.join(cwd, folder,"0.json")
        start=time.time()
        gameFile=writeGlobalJSONFile(var)
        file=[]

        dictionary={"BallPosition": [0,0], "CurrGameTime":0,"OpponentPositions":{"OPP1":[0.0,0.0],"OPP10":[0.0,0.0],"OPP11":[0.0,0.0],"OPP2":[0.0,0.0],"OPP3":[0.0,0.0],"OPP4":[0.0,0.0],"OPP5":[0.0,0.0],"OPP6":[0.0,0.0],"OPP7":[0.0,0.0],"OPP8":[0.0,0.0],"OPP9":[0.0,0.0]},"TeamMatePositions":{"TEAM1":[0.0,0.0],"TEAM10":[0.0,0.0],"TEAM11":[0.0,0.0],"TEAM2":[0.0,0.0],"TEAM3":[0.0,0.0],"TEAM4":[0.0,0.0],"TEAM5":[0.0,0.0],"TEAM6":[0.0,0.0],"TEAM7":[0.0,0.0],"TEAM8":[0.0,0.0],"TEAM9":[0.0,0.0]}}
        for t in range(len(gameFile[0])):
                dictionary["CurrGameTime"]=gameFile[0][t]["CurrGameTime"]
                OpponentCurrCoords=getAverageOpponentPosition(t,gameFile)
                BallCurrCoords=getAverageBallPosition(t,gameFile)
                dictionary["BallPosition"][0]=BallCurrCoords[0]
                dictionary["BallPosition"][1]=BallCurrCoords[1]                                                                                     
                for i in range(11):
                        
                        oppCurr=[OpponentCurrCoords[0][i],OpponentCurrCoords[1][i]]    
                        currCoords=gameFile[i][t]['MyPosition']
                        dictionary["OpponentPositions"]["OPP"+str(i+1)][0]=oppCurr[0]
                        dictionary["OpponentPositions"]["OPP"+str(i+1)][1]=oppCurr[1]
                        dictionary["TeamMatePositions"]["TEAM"+str(i+1)][0]=currCoords[0]
                        dictionary["TeamMatePositions"]["TEAM"+str(i+1)][1]=currCoords[1]

                
                with open(path_to_json_file, "a") as outfile:
                        outfile.write(json.dumps(dictionary)+"\n")        
        print(time.time()-start)

         


