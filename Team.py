<<<<<<< Updated upstream
import pygame
import numpy as np
=======
import numpy as np
from Field_Objects import *
>>>>>>> Stashed changes


class Team:

<<<<<<< Updated upstream
    def __init__(self):
        self.team = np.array([])
        self.score = 0

    def add_player(self, player):
        self.team = np.append(self.team, player)
=======
    team = np.array([])

    def __init__(self):
        self.score = 0

    def add_player(self, player):
        self.team = np.append(self.team, player)

    def change_team_position(self, new_team_positions):

        for player in range(len(self.team)):
            self.team[player].change_position(new_team_positions[player][0], new_team_positions[player][1])

>>>>>>> Stashed changes
