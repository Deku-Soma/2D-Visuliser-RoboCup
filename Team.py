import numpy as np
from Field_Objects import *


class Team:

    def __init__(self):
        pass

    team = np.array([])
    score = 0

    def add_player(self, player):
        self.team = np.append(self.team, player)

    # when you add a new_team_positions it must be a 2d array
    def update_team_position(self, new_team_positions):
        for player in range(len(self.team)):
            self.team[player].change_position(new_team_positions[player][0], new_team_positions[player][1])

    def update_score(self):
        self.score += 1


team = Team()
player = Player('', 0, 0)

team.add_player(player)

team.update_team_position([[1, 1]])
