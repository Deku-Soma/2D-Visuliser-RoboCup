import json

def loadJSONFile(PlayerNum):
    jsondata=[]
    with open(str(PlayerNum)+'.json','r') as f:
        for line in f:
            jsondata.append(json.loads(line))
    return jsondata

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
        
    def __str__(self):
        return f"Player: {self.Player} BallPosition: {self.BallPosition} MyPosition: {self.MyPosition} TeamMateDistanceToBall: {self.TeamMateDistanceToBall} OpponentPositions: {self.OpponentPositions} TeamMatePositions: {self.TeamMatePositions}"

def calculate_average_opponent_position(home_team_positions, away_team_positions):
    num_home_players = len(home_team_positions)
    num_away_players = len(away_team_positions)
    avg_opponent_positions = []

    for i in range(num_home_players):
        opponent_positions = []
        for j in range(num_away_players):
            opponent_x = away_team_positions[j]['x']
            opponent_y = away_team_positions[j]['y']
            distance_to_opponent = ((home_team_positions[i]['x'] - opponent_x) ** 2 + (home_team_positions[i]['y'] - opponent_y) ** 2) ** 0.5
            if distance_to_opponent < 10: # Only consider opponents within 10 meters
                opponent_positions.append((opponent_x, opponent_y))
        if len(opponent_positions) > 0:
            avg_opponent_x = sum([p[0] for p in opponent_positions]) / len(opponent_positions)
            avg_opponent_y = sum([p[1] for p in opponent_positions]) / len(opponent_positions)
            avg_opponent_positions.append((avg_opponent_x, avg_opponent_y))
        else:
            avg_opponent_positions.append(None)

    return avg_opponent_positions


test= ParseData(1)
test.initialGameState(1)
print(test)
test.setGameState(1,21)
print(test)
