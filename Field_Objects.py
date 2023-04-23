import math
import numpy as np


class FieldObjects():

    sprite_file_path = ""

    def __init__(self, image_path, x, y):
        self.sprite_file_path = image_path
        self.centre = [x, y]

    def change_position(self, x, y):
        self.centre = [x, y]

    def change_sprite_file_path(self, new_file_path):

        self.sprite_file_path = new_file_path

    def x(self):
        return self.centre[0]

    def y(self):
        return self.centre[1]



class Player(FieldObjects):

    distance_to_ball = 0

    def set_distance_to_ball(self, ball):
        return math.sqrt((self.x() - ball.x()) ** 2 + (self.y() - ball.y()) ** 2)


class Ball(FieldObjects):

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

