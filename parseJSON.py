import json
def loadJSONFile(PlayerNum):
        jsondata=[]
        f=open(str(PlayerNum)+'.json','r')
        for line in f:
            jsondata.append(json.loads(line))
        return jsondata

class ParseData:
    def __init__(self, Player):
        self.Player= Player
        self.BallPosition=[]
        self.MyPosition=[]
        self.TeamMateDistanceToBall=[]

    def initialGameState(self,PlayerNum): 
        playerData= loadJSONFile(PlayerNum)
        self.Player=PlayerNum
        self.BallPosition=playerData[0]['BallPosition']
        self.MyPosition=playerData[0]['MyPosition']
        self.TeamMateDistanceToBall=playerData[0]['TeamMateDistanceToBall']
            
    def setGameState(self,PlayerNum,TimeInterval):
        playerData=loadJSONFile(PlayerNum)
        self.Player=PlayerNum
        self.BallPosition=playerData[TimeInterval]['BallPosition']
        self.MyPosition=playerData[TimeInterval]['MyPosition']
        self.TeamMateDistanceToBall=playerData[TimeInterval]['TeamMateDistanceToBall']

    def __str__(self):
        return f"Player: {self.Player} BallPosition: {self.BallPosition} MyPosition: {self.MyPosition} TeamMateDistanceToBall: {self.TeamMateDistanceToBall}"
    
         

test= ParseData(1)
test.initialGameState(1)
print(test)
test.setGameState(1,21)
print(test)
