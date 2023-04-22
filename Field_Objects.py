import pygame
import numpy as np


class FieldObjects(pygame.sprite.Sprite):

    centre = ()

    def __init__(self, team1_sprite_path, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(team1_sprite_path)
        self.imageUpdate = pygame.transform.scale(self.image, (1, 1))
        self.rect = self.imageUpdate.get_rect()
        self.rect.center = (pos_x, pos_y)
        self.centre = self.rect.center

    def change_centre(self, pos_x, pos_y):

        self.rect.center(pos_x, pos_y)

    def print_centre(self):
        print(self.rect.center)


class Player(FieldObjects):

    def __init__(self, team1_sprite_path, pos_x, pos_y):
        super().__init__(team1_sprite_path, pos_x, pos_y)
        self.distance_to_ball = np.zeros([2])

    def print_centre(self):
        print(self.rect.center)


class Ball(FieldObjects):

    closest_player = ""
