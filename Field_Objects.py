<<<<<<< Updated upstream
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
=======
import math
import numpy as np


class FieldObjects():

    centre = np.array([])
    sprite_file_path = ""

    def __init__(self, image_path, x, y):
        self.sprite_file_path = image_path
        self.centre = np.append(self.centre, [x,y])

    def change_position(self, x, y):
        self.centre = np.array([x, y])

    def change_sprite_file_path(self, new_file_path):

        self.sprite_file_path = new_file_path

    def x(self):
        return self.centre[0]

    def y(self):
        return self.centre[1]

>>>>>>> Stashed changes


class Player(FieldObjects):

<<<<<<< Updated upstream
    def __init__(self, team1_sprite_path, pos_x, pos_y):
        super().__init__(team1_sprite_path, pos_x, pos_y)
        self.distance_to_ball = np.zeros([2])

    def print_centre(self):
        print(self.rect.center)
=======
    distance_to_ball = 0

    def set_distance_to_ball(self, ball):
        return math.sqrt((self.x() - ball.x()) ** 2 + (self.y() - ball.y()) ** 2)
>>>>>>> Stashed changes


class Ball(FieldObjects):

<<<<<<< Updated upstream
    closest_player = ""
=======
    closest_player = -1

    def find_closest_player(self, all_players):

        distance = 1000000000
        i = 0
        player_i = 0
        for player in all_players:

            if distance > math.sqrt((self.x() - player.x()) ** 2 + (self.y() - player.y()) ** 2):

                player_i = i

                distance = math.sqrt((self.x() - player.x()) ** 2 + (self.y() - player.y()) ** 2)

            i += 1

        self.closest_player = player_i

>>>>>>> Stashed changes
