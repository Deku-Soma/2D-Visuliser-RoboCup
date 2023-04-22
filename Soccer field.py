import sys, random, pygame, os
from Field_Objects import Player, Ball
from Team import Team


# class
class Crosshair(pygame.sprite.Sprite):
    def __init__(self,picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = pygame.mouse.get_pos()


'''class players(pygame.sprite.Sprite):
    def __init__(self, team1_sprite_path, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(team1_sprite_path)
        self.size = self.image.get_size()
        # create a 2x bigger image than self.image
        self.bigger_img = pygame.transform.scale(self.image, (int(self.size[0] * 10), int(self.size[1] * 10)))
        self.imageUpdate = pygame.transform.scale(self.image, (2,2))
        self.rect = self.imageUpdate.get_rect()
        self.rect.center = [pos_x,pos_y]
'''

# general area
folder_name = 'Assets'
file_name = 'nonselectedplayer1-removebg-smaller.PNG'

# Get the current working directory
cwd = os.getcwd()

# Construct the file path
team1_sprite_path = os.path.join(cwd, folder_name, file_name)

file_name = 'nonselectedplayer2-removebg-smaller.PNG'

team2_sprite_path = os.path.join(cwd, folder_name, file_name)

file_name = 'soccerball-removebg-smaller.PNG'

ball_sprite_path = os.path.join(cwd, folder_name, file_name)

pygame.init()
clock = pygame.time.Clock()

# Game Screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))
background = pygame.image.load("football-pitch.png")
backgroundUpdate = pygame.transform.scale(background, (800, 600))
pygame.mouse.set_visible(False)

# players
player_group = pygame.sprite.Group()

team1 = Team()

for player in range(11):
    new_player = Player(team1_sprite_path, random.randrange(50, 750), random.randrange(50,300))

    screen.blit(new_player.imageUpdate, new_player.rect)

    player_group.add(new_player)
    team1.add_player(new_player)

team2 = Team()

for player in range(11):
    new_player = Player(team2_sprite_path, random.randrange(50, 750), random.randrange(300, 550))
    player_group.add(new_player)
    team2.add_player(new_player)

new_player = Player(ball_sprite_path,random.randrange(50,750),random.randrange(50,550))
player_group.add(new_player)


crosshair = Crosshair("crosshair_outline_large.png")

crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    screen.blit(backgroundUpdate,(0,0))
    player_group.draw(screen)
    crosshair_group.draw(screen)
    crosshair_group.update()
    clock.tick(60)