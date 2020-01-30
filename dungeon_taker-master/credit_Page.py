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
aegean = (70,143,162)

# set up assets folders
game_folder = os.path.dirname(__file__)


#initialize pygame create window, and clock
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Template")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()

def text_objects(text, font):
    textSurface = font.render(text, True, aegean)
    return textSurface, textSurface.get_rect()

def text_object2(text, font):
    textSurface = font.render(text, True, WHITE)
    return textSurface, textSurface.get_rect()

# Making a sprite group
# all_sprites = pygame.sprite.Group()

def credit_move():
    pygame.init()
    game_folder = os.path.dirname(__file__)
    screen.fill(BLACK)

    largetext = pygame.font.Font('freesansbold.ttf',50)
    textsurf0,textrect0 = text_objects("Credits",largetext)
    textrect0.center = (400,300)

    smalltext = pygame.font.Font('freesansbold.ttf',40)
    textsurf1,textrect1 = text_objects("Zachary Jones",smalltext)
    textrect1.center = (400,400)
    textsurf2,textrect2 = text_objects("Cyril",smalltext)
    textrect2.center = (400,450)
    textsurf3,textrect3 = text_objects("Shayan Yazdi",smalltext)
    textrect3.center = (400,500)
    textsurf4,textrect4 = text_objects("Usha S Rao",smalltext)
    textrect4.center = (400,550)


# Game loop
    running = True
    while running:

        screen.fill(BLACK)

        #if the loop takes less than 1/30th of a second, this keeps the rate steady
        clock.tick(FPS)
        # Process input (events)
        for event in pygame.event.get():
            # Checking for quit
            if event.type == pygame.QUIT:
                pygame.quit()
                quit

        #Update
        # all_sprites.update()
        textrect0.y -= 5
        textrect1.y -= 5
        textrect2.y -= 5
        textrect3.y -= 5
        textrect4.y -= 5





        screen.blit(textsurf0,textrect0)
        screen.blit(textsurf1,textrect1)
        screen.blit(textsurf2,textrect2)
        screen.blit(textsurf3,textrect3)
        screen.blit(textsurf4,textrect4)

        print(textrect1.y)
        pygame.display.update()

        clock.tick(FPS)
        

        # Draw / render


        # all_sprites.draw(screen)

        # always flip last.  This is for double buffering
        pygame.display.flip()





    
    return("Test")






# pygame.quit()