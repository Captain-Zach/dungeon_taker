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
    textSurface = font.render(text, True, RED)
    return textSurface, textSurface.get_rect()

# Making a sprite group
# all_sprites = pygame.sprite.Group()

def credit_move():
    pygame.init()
    game_folder = os.path.dirname(__file__)
    screen.fill(BLACK)

    largetext = pygame.font.Font('Halo3.ttf',60)
    textsurf0,textrect0 = text_object2("THE END",largetext)
    textrect0.center = (400,100)

    smalltext = pygame.font.Font('freesansbold.ttf',40)
    textsurf1,textrect1 = text_objects("Zach Jones - Project Lead",smalltext)
    textrect1.center = (400,200)
    textsurf2,textrect2 = text_objects("Tora Jones - Art/Animation",smalltext)
    textrect2.center = (400,250)
    textsurf3,textrect3 = text_objects("Usha S Rao - UI/Presentation",smalltext)
    textrect3.center = (400,300)
    textsurf4,textrect4 = text_objects("Cyril Patton - AI",smalltext)
    textrect4.center = (400,350)
    textsurf5,textrect5 = text_objects("Shayan Yazdi - SFX/Level Design",smalltext)
    textrect5.center = (400,400)


# Game loop
    pygame.mixer.music.load('sounds/boss_fight.wav')
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(loops=-1)

    running = True
    while running:

        screen.fill(BLACK)

        #if the loop takes less than 1/30th of a second, this keeps the rate steady
        clock.tick(FPS)
        # Process input (events)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit()
            # Checking for quit
            if event.type == pygame.QUIT:
                pygame.quit()
                quit

        #Update
        # all_sprites.update()

        # textrect0.y -= 5
        # if textrect0.y < 0:
        #     textrect0.y = HEIGHT
        # textrect1.y -= 5
        # if textrect1.y < 0:
        #     textrect1.y = HEIGHT
        # textrect2.y -= 5
        # if textrect2.y < 0:
        #     textrect2.y = HEIGHT
        # textrect3.y -= 5
        # if textrect3.y < 0:
        #     textrect3.y = HEIGHT
        # textrect4.y -= 5
        # if textrect4.y < 0:
        #     textrect4.y = HEIGHT
        # textrect5.y -= 5
        # if textrect5.y < 0:
        #     textrect5.y = HEIGHT

        screen.blit(textsurf0,textrect0)
        screen.blit(textsurf1,textrect1)
        screen.blit(textsurf2,textrect2)
        screen.blit(textsurf3,textrect3)
        screen.blit(textsurf4,textrect4)
        screen.blit(textsurf5,textrect5)

        print(textrect1.y)
        pygame.display.update()

        clock.tick(FPS)
        

        # Draw / render


        # all_sprites.draw(screen)

        # always flip last.  This is for double buffering
        pygame.display.flip()





    
    return("Test")






# pygame.quit()