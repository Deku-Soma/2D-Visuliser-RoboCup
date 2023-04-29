import math
import numpy as np
from PIL import Image, ImageTk


class FieldObjects:

    def __init__(self, image_path, x, y):
        self.centre = np.array([0,0])
        self.centre[0] = x
        self.centre[1] = y

        self.sprite_image = Image.open(image_path)
        self.sprite_image = self.sprite_image.resize((50, 50), Image.LANCZOS)
        self.sprite_image_object = ImageTk.PhotoImage(self.sprite_image)

    def change_position(self, x, y):
        self.centre = np.array([x, y])

    def change_sprite_file_path(self, new_file_path):
        self.sprite_image = Image.open(new_file_path)
        self.sprite_image = self.sprite_image.resize((50, 50), Image.LANCZOS)
        self.sprite_image_object = ImageTk.PhotoImage(self.sprite_image)

    def get_sprite_image(self):
        return self.sprite_image_object

    def x(self):
        return self.centre[0]

    def y(self):
        return self.centre[1]

    def print_centre(self):
        print(self.centre)


class Player(FieldObjects):

    def __init__(self, image_path, x, y):
        super().__init__(image_path, x, y)
        self. distance_to_ball = 0

    def set_distance_to_ball(self, ball):
        return math.sqrt((self.x() - ball.x()) ** 2 + (self.y() - ball.y()) ** 2)


class Ball(FieldObjects):

    def __init__(self):
        super.__init__()
        self.closest_player = -1

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

