import pygame
import random
import roomLib
import node

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255, 0, 0)
YELLOW = (255,255,0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


test_dungeon = [
    [0, 0, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 0],
    [0, 1, 1, 0],
    [0, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 0],
]

class Dungeon:
    def __init__(self, start_room="0301", map=test_dungeon):
        self.start_room = start_room
        
        pass

class Door(pygame.sprite.Sprite):
    def __init__(self, go_to="0201", pos=(0,9)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40,32))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.posX = (pos[1] * 40) 
        self.posY = (pos[0] * 40) + 9
        self.go_to = go_to

        # positioning.
        self.rect.x = self.posX
        self.rect.y = self.posY
