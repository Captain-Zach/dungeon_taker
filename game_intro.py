# Pygame template - skeleton for a new pygame project
import pygame
import random
import os
from pygame.locals import *


def intro_pg():



    WIDTH = 800
    HEIGHT = 600
    FPS = 30

    # define colors
    WHITE = (255,255,255)
    BLACK = (0,0,0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    gray = (128,128,128)

    # set up assets folders
    game_folder = os.path.dirname(__file__)


    #initialize pygame create window, and clock
    pygame.init()
    pygame.mixer.init()

    intro_img = pygame.image.load('PixelGunHound.png')


    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    pygame.display.set_caption("Dungeon Taker Intro")
    clock = pygame.time.Clock()

    # Making a sprite group
    all_sprites = pygame.sprite.Group()


    # Game loop
    running = True
    start_ticks = pygame.time.get_ticks()
    while running:

        # Process input (events)
        for event in pygame.event.get():
            # Checking for quit
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                

        screen.fill(WHITE)


        display_logo_size = intro_img.get_size()
        screen.blit(intro_img, [WIDTH/2 - display_logo_size[0]/2, HEIGHT/2 - display_logo_size[1]/2])

        pygame.display.flip()
        seconds = (pygame.time.get_ticks()- start_ticks)/1000
        if seconds > 3:
            print(seconds)
            running = False
        #if the loop takes less than 1/30th of a second, this keeps the rate steady
        clock.tick(FPS)
    

    return ("START_SCREEN")





