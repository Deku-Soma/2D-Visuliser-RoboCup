import numpy as np
from Field_Objects import *


class Team:

    team = np.array([])

    def __init__(self):
        self.score = 0

    def add_player(self, player):
        self.team = np.append(self.team, player)

    def change_team_position(self, new_team_positions):

        for player in range(len(self.team)):
            self.team[player].change_position(new_team_positions[player][0], new_team_positions[player][1])

