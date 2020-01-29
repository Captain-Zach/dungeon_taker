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
GREEN = (0, 200, 0)
BLUE = (0, 0, 255)
BLACK = (0,0,0)
bright_green = (0,255,0)
YELLOW = (255,255,0)


pygame.init()
pygame.mixer.init()
start_page = pygame.image.load('dungeon.png')
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dungeon Taker Start")
clock = pygame.time.Clock()


def health_bars(bar_update):
    if bar_update > 75:
        player_health_color = GREEN
    elif bar_update > 45:
        player_health_color = YELLOW
    else:
        player_health_color = RED

    pygame.draw.rect(screen,player_health_color,(600,25,bar_update,25))


def text_objects(text, font):
    textSurface = font.render(text, True, RED)
    return textSurface, textSurface.get_rect()


def button(msg,x,y,w,h,ic,ac,action = None):

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w>mouse[0]>x and y+h>mouse[1]>y:
        pygame.draw.rect(screen,ac,(x,y,w,h))
        if click[0]==1 and action!=None:
            if action=="play":
                return("MAIN")
            elif action=="quit":
                pygame.quit()
                quit()

    else:
        pygame.draw.rect(screen,ic,(x,y,w,h))
    smalltext = pygame.font.Font('freesansbold.ttf',20)
    textsurf,textrect = text_objects(msg,smalltext)
    textrect.center = ((x+(w/2)),(y+(h/2)))
    screen.blit(textsurf,textrect)

def button_intro():


    pygame.init()
    # set up assets folders
    game_folder = os.path.dirname(__file__)

    player_health = 10
    bar_update = 80
    # Game loop
    running = True
    while running:
        #if the loop takes less than 1/30th of a second, this keeps the rate steady
        clock.tick(FPS)
        # Process input (events)
        for event in pygame.event.get():
            # Checking for quit
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.blit(pygame.transform.scale(start_page, (WIDTH,HEIGHT)), (0, 0))

        largetext = pygame.font.Font('freesansbold.ttf',80)
        TextSurf,TextRect = text_objects("Dungeon Taker",largetext)
        TextRect.center = (400,300)
        screen.blit(TextSurf,TextRect)
        x = button("START",150,520,100,50,GREEN,bright_green,"play")
        if x== "MAIN":
            return ("MAIN")
        
        button("QUIT",550,520,100,50,GREEN,bright_green,"quit")
        
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.QUIT()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        player_health -= 1
                        bar_update -= 5
                        

                    elif event.key == pygame.K_UP:
                        player_health += 1
                        bar_update += 5
                        
        print(player_health)
        print(bar_update)
        health_bars(bar_update)
        pygame.display.update()




        clock.tick(FPS)



        pygame.display.flip()



