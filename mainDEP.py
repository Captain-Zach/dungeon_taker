import pygame
import character
import roomLib


# Initialize pygame
pygame.init()

######################################################################
#SETTINGS
screenWidth = 800
screenHeight = 600
timeDelay = 50
screen = pygame.display.set_mode((screenWidth, screenHeight ))
pygame.display.set_caption("Dungeon Taker: OTA")
icon = pygame.image.load('images/oubliette.png')
pygame.display.set_icon(icon)

######################################################################

player = character.Character()

wallColor = (50, 50, 50)

def pDraw():
    screen.blit(player.sprite, (player.xPos, player.yPos))
    #print(player.xPos, player.yPos)

running = True

def drawHandling():
    #this function handles the drawing in layers
    #RGB VALUES
    screen.fill((0,0,0))
    pDraw()

roomLib.procRoomX()

# A state machine for managing the main game loop



while running:


    pygame.time.delay(timeDelay)

    running = player.inputHandler()
    player.movement()

    drawHandling()

    roomLib.drawTestRoom(screen, wallColor)

    pygame.display.update()

    
    