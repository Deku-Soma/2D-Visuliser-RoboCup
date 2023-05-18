This is the RoboCup git repository for the MacroHard group
Cricle CI test results:
[![CircleCI](https://dl.circleci.com/status-badge/img/gh/Deku-Soma/2D-Visuliser-RoboCup/tree/master.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/Deku-Soma/2D-Visuliser-RoboCup/tree/master)
CodeCov:
[![codecov](https://codecov.io/gh/Deku-Soma/2D-Visuliser-RoboCup/branch/master/graph/badge.svg?token=WKYPNDC727)](https://codecov.io/gh/Deku-Soma/2D-Visuliser-RoboCup)


Field_Objects Class:

to initialise the class you need to pass it the path way to file (E.g. c:/MacroHard/image) and an x and y coordinate
To get the file path you can use the os library

There 2 variables associated with this class

centre - this stores the central position of the sprite. NB it's stored in a numpy array
sprite_file_path - this stores the file path to the image

There 4 Functions associated with this class

change_position - updates the x,y coordinate of the Field_Objects
change_sprite_file_path - this changes the file path for the image allowing you to change the image of Field_Objects
x - returns x coordinate of the Field_Objects
y - returns y coordinate of the Field_Objects


Player class:

this is a subclass of Field_Objects

There 1 variable associated with this class

distance_to_ball - stores the player's distance to the ball

There's 1 Function associated with this class

set_distance_to_ball - calculates the the distance between the ball and the player


Ball class:

this is a subclass of Field_Objects

There 1 variable associated with this class

closest_player - find

There's 1 Function associated with this class

find_closest_player - finds the closest player


Team class:

This class is responsible for storing all the players for a team and the team's score

There is 1 variable associated with the class

team - numpy array that stores all the players from the Player class

There's 3 Function associated with this class

add_player - adds a player to the team array
update_team_position - updates all the field positions
update_score - increments the team's score by 1
