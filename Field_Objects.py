import numpy as np
from PIL import Image, ImageTk


# This is the class that will store all the information for the sprites on screen

class FieldObjects:

    # Enter a file path and the x and y position of the object. x and y are ints
    def __init__(self, image_path, x, y, ):

        # Here we set the position of the object on the screen
        self.centre = np.array([0, 0])
        self.centre[0] = x
        self.centre[1] = y

        # Here we create the image, rize it and turn it into an object the TKinter canvas can use
        self.sprite_image = Image.open(image_path)
        self.sprite_image = self.sprite_image.resize((50, 50), Image.LANCZOS)
        self.sprite_image_object = ImageTk.PhotoImage(self.sprite_image)

    # This changes the positions of the sprite. enter x and y as ints
    def change_position(self, x, y):
        self.centre = np.array([x, y])

    # This changes the sprites image
    def change_sprite_image(self, new_file_path):
        self.sprite_image = Image.open(new_file_path)
        self.sprite_image = self.sprite_image.resize((50, 50), Image.LANCZOS)
        self.sprite_image_object = ImageTk.PhotoImage(self.sprite_image)

    # This gets the sprite image stored as the ImageTK for the TKinter canvas
    def get_sprite_image(self):
        return self.sprite_image_object

    # Returns the x value of the sprite
    def x(self):
        return self.centre[0]

    # Returns the y value of the sprite
    def y(self):
        return self.centre[1]

    # Returns the x and y position in a Numpy Array
    def print_centre(self):
        print(self.centre)


# This is a subclass of Field Objects to store Player objects
class Player(FieldObjects):

    # Enter a file path and the x and y position of the object. x and y are ints
    def __init__(self, image_path, x, y, distance_to_ball=0):
        super().__init__(image_path, x, y)

        # creates a variable to store the Player's distance to the ball
        self.distance_to_ball = distance_to_ball

    # This sets the Player's distance to the ball to some value
    def set_distance_to_ball(self, distance_to_ball):
        self.distance_to_ball = distance_to_ball

    def get_distance_to_ball(self):
        return self.distance_to_ball


# This is a subclass of Field Objects to Ball objects
class Ball(FieldObjects):

    # Enter a file path and the x and y position of the object. x and y are ints
    def __init__(self, image_path, x, y):
        super().__init__(image_path, x, y)

        # Created a variable that stores which Player is the closest
        self.closest_player = -1

    # This function find the closest player to the ball
    def find_closest_player(self, teams):

        distance = 99999999999
        player_i = 0
        i = 0

        for team in teams:
            for player in team:
                if player.get_distance_to_ball() < distance:
                    distance = player.get_distance_to_ball()
                    player_i = i

                i += 1

        self.closest_player = player_i
