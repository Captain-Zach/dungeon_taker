# Pygame template - skeleton for a new pygame project
import pygame
import random
import os

WIDTH = 800
HEIGHT = 600
FPS = 30

# define colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# set up assets folders
game_folder = os.path.dirname(__file__)


#initialize pygame create window, and clock
pygame.init()
pygame.mixer.init()
pygame.joystick.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Template")
clock = pygame.time.Clock()

# Making a sprite group
all_sprites = pygame.sprite.Group()

joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
print(joysticks)
# Game loop
running = True
while running:
    #if the loop takes less than 1/30th of a second, this keeps the rate steady
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # Checking for quit
        if event.type == pygame.QUIT:
            running = False

    #Update
    all_sprites.update()

    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # always flip last.  This is for double buffering.
    pygame.display.flip()






pygame.quit()