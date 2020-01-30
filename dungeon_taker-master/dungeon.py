import pygame
import random
import roomLib
import node

test_dungeon = [
    [0,0,0,0],
    [0,0,1,0],
    [0,0,1,0],
    [0,1,1,0],
    [0,1,0,0],
    [0,1,0,0],
    [0,0,0,0],
]
class Dungeon:
    def __init__(self, start_room="0301", map=test_dungeon):
        self.start_room = start_room
        
        pass

