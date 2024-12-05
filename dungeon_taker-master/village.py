import pygame
import enemy
import character

# Init for testing purposes.
pygame.init()

######################################################################
#SETTINGS
screenWidth = 800
screenHeight = 600
FPS = 30

#Creates window, and clock, sets Icon
screen = pygame.display.set_mode((screenWidth, screenHeight ))
pygame.display.set_caption("Dungeon Taker: Village Test")
icon = pygame.image.load('images/oubliette.png')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

# runtime variable
running = True

# Sprite groups
floor_sprites = pygame.sprite.Group()
wall_sprites = pygame.sprite.Group()
collision_sprites = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

player = character.Character()


# while loop would be the "scene" function
while running:
    print("village")
    clock.tick(FPS)
    running = False
