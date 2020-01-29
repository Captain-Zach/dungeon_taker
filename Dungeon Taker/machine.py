import pygame

import character
import enemy
import roomLib
import test2
import game_intro
import start_page
import credit_Page

# Initialize pygame
pygame.init()

######################################################################
#SETTINGS
screenWidth = 800
screenHeight = 600
FPS = 30
# timeDelay = 50 DEPRECATED





#Creates window, and clock, sets Icon
screen = pygame.display.set_mode((screenWidth, screenHeight ))
pygame.display.set_caption("Dungeon Taker: OTA")
icon = pygame.image.load('images/oubliette.png')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

# STATE
state = "INTRO"
running = True

while running:
    if state == "INTRO":
        state = game_intro.intro_pg()
        print(state)
    if state == "START_SCREEN":
        state = start_page.button_intro()
    if state == "MAIN":
        state = test2.main()
        print(state)
    if state == "END":
        print("Nope")
        quit()