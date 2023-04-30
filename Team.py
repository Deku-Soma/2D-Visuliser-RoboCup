import numpy as np
from Field_Objects import *


class Team:

    def __init__(self):
        self.score = 0
        self.team = np.array([])


    def add_player(self, player):
        self.team = np.append(self.team, player)

    def update_team_position(self, new_team_positions):

        for player in range(len(self.team)):
            self.team[player].change_position(new_team_positions[player][0], new_team_positions[player][1])

    def update_score(self):
        self.score += 1
