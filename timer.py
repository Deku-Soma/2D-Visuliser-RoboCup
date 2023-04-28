import sys
import pygame
from pygame.locals import *

pygame.init()

screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Soccer Game Timer')

font = pygame.font.Font(None, 36)

start_time = pygame.time.get_ticks()

while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Calculate the elapsed time
    elapsed_time = pygame.time.get_ticks() - start_time

    # Convert the elapsed time to seconds
    seconds = int(elapsed_time / 1000)

    # Format the time as minutes:seconds
    timer_text = '{:02d}:{:02d}'.format(seconds // 60, seconds % 60)

    # Create a surface for the timer display
    timer_surface = font.render(timer_text, True, (255, 255, 255))

    # Display the timer on the screen
    screen.fill((0, 0, 0))
    screen.blit(timer_surface, (screen_width // 2 - timer_surface.get_width() // 2,
                                 screen_height // 2 - timer_surface.get_height() // 2))
    pygame.display.update()
