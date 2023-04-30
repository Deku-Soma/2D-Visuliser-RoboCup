import os
player_file = "nonselectedplayer2-removebg.png"

field_file = "Soccer_Field_HD-downsized.png"

folder = "Assets"

cwd = os.getcwd()



path_to_player_file = os.path.join(cwd, folder, player_file)
#print(path_to_player_file)
#path_to_field_file = os.path.join(cwd,folder,field_file)

fileName = "nonselectedplayer2-removebg.png"
folderName = "Assets"

cwd = os.getcwd()

player_image_path = os.path.join(cwd, folderName, fileName)
print(player_image_path)