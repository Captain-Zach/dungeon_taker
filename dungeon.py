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
room1 = roomLib.drawTargetRoom(roomLib.testRoom)
room2 = roomLib.drawTargetRoom(roomLib.firstXSuccess)
room3 = roomLib.drawTargetRoom(roomLib.testRoom)

# def create_dungeon():
#     # create map


dungeon_dict = {
    "0301":room1,
    "0201":room2,
    "0101":room3,

}
class Dungeon:
    def __init__(self, start_room="0301", map=test_dungeon):
        self.start_room = start_room
        
        pass

class Room:
    def __init__(self, north_door = None, south_door = None, east_door = None, west_door = None, map=roomLib.procRoomY()):
        self.north_door = None
        self.south_door = None
        self.east_door = None
        self.west_door = None
        self.map = roomLib.procRoomY()
        self.door_list = []
        if self.north_door != None:
            self.door_list.append(self.north_door)
        if self.south_door != None:
            self.door_list.append(self.south_door)
        if self.east_door != None:
            self.door_list.append(self.east_door)
        if self.west_door != None:
            self.door_list.append(self.west_door)

    def refresh(self):
        if self.north_door != None:
            self.door_list.append(self.north_door)
        if self.south_door != None:
            self.door_list.append(self.south_door)
        if self.east_door != None:
            self.door_list.append(self.east_door)
        if self.west_door != None:
            self.door_list.append(self.west_door)

class Door(pygame.sprite.Sprite):
    def __init__(self, go_to="0201", pos=(0,9), direction = 'north'):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40,46))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.posX = (pos[1] * 40) 
        self.posY = (pos[0] * 40) - 2
        self.go_to = go_to
        self.direction = direction

        # positioning.
        self.rect.x = self.posX
        self.rect.y = self.posY


    def change_rooms(self, player):
        if self.direction == 'north':
            player.xPos = 9 * 40
            player.yPos = 13 * 40
        if self.direction == 'south':
            player.xPos = 9 * 40
            player.yPos = 2 * 40
        if self.direction == 'east':
            player.xPos = 18 * 40
            player.yPos = 6 * 40
        if self.direction == 'west':
            player.xPos = 2 * 40
            player.yPos = 6 * 40
