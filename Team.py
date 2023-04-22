import pygame
import numpy as np


class Team:

    def __init__(self):
        self.team = np.array([])
        self.score = 0

    def add_player(self, player):
        self.team = np.append(self.team, player)