import pygame

import character
import credit_Page
import enemy
import game_intro
import moo
import roomLib
import start_page
import test2
import dungeon_trav

# Initialize pygame
pygame.init()

######################################################################
#SETTINGS
screenWidth = 800
screenHeight = 600
FPS = 30
# timeDelay = 50 DEPRECATED





#Creates window, and clock, sets Icon
# screen = pygame.display.set_mode((screenWidth, screenHeight ))
screen = pygame.display.set_mode((screenWidth, screenHeight ), pygame.FULLSCREEN)
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
    if state == "VILLAGE":
        state = moo.moo()
    if state == "MAIN":
        state = dungeon_trav.main()
        print(state)
    if state == "CREDITS":
        state = credit_Page.credit_move()
    if state == "END":
        print("Nope")
        quit()
