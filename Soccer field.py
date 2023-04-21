import sys,random
import pygame

#class 
class Crosshair(pygame.sprite.Sprite):
    def __init__(self,picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.center = pygame.mouse.get_pos()


class players(pygame.sprite.Sprite):
    def __init__(self,picture_path,pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.imageUpdate = pygame.transform.scale(self.image, (10,10))
        self.rect = self.imageUpdate.get_rect()
        self.rect.center = [pos_x,pos_y]

#general area


pygame.init()
clock = pygame.time.Clock()

#Game Screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))
background = pygame.image.load("football-pitch.png")
backgroundUpdate = pygame.transform.scale(background, (800, 600))
pygame.mouse.set_visible(False)

#players
player_group = pygame.sprite.Group()
for player in range(11):
    new_player = players("crosshair_blue_small.png",random.randrange(50,750),random.randrange(50,300))
    player_group.add(new_player)

for player in range(11):
    new_player = players("crosshair_red_small.png",random.randrange(50,750),random.randrange(300,550))
    player_group.add(new_player)
new_player = players("SoccerBall.png",random.randrange(50,750),random.randrange(50,550))
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