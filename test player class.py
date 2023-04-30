from Field_Objects import *

from Team import *
import os


player_file = "nonselectedplayer2-removebg.png"

field_file = "Soccer_Field_HD-downsized.png"

folder = "Assets"

cwd = os.getcwd()

path_to_player_file = os.path.join(cwd, folder, player_file)
path_to_field_file = os.path.join(cwd,folder,field_file)


player = Player(path_to_player_file,0,0)

team = Team()

team.add_player(player)
print(player.x())
print(team.team[0].x())

team.update_team_position([[1,1]])
print(team.team[0].x())
