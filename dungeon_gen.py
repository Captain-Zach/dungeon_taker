import os
import pickle
import random

import pygame

import dungeon
import node

dungeon_list = []
# map out a dungeon
def map_gen():
    pass

# package dungeon
def dungeon_packer(d_dict, map = dungeon.test_dungeon):
    newDungeon = dungeon.Dungeon(d_dict, map)
    # set newDungeon first room.
    # method or some stuff.
    return newDungeon

# make a dungeon dictionary
def make_dungeon_dict(map = dungeon.test_dungeon):
    d_dict = {}
    dungeon_map = map
    # pass 1 creates the rooms
    for y in range(1, len(dungeon_map)-1):
        for x in range(1, len(dungeon_map[y])-1):
            if dungeon_map[y][x] == 1:
                d_dict[build_coord(y,x)] = dungeon.Room()
                # print(d_dict[build_coord(y,x)].map)
    # CANNOT PICKLE PYGAME THINGERS (SURFACES OR IMAGES)
    # for y in range(1, len(dungeon_map)-1):
    #     for x in range(1, len(dungeon_map[y])-1):
    #         if dungeon_map[y][x] == 1:
    #             # if room to the left
    #             if dungeon_map[y][x-1] == 1:
    #                 d_dict[build_coord(y,x)].east_door = dungeon.Door(direction='east', pos=(6,0), go_to=build_coord(y,x-1))
    #             # if room above
    #             if dungeon_map[y-1][x] == 1:
    #                 d_dict[build_coord(y,x)].north_door = dungeon.Door(direction='north', go_to=build_coord(y-1,x))
    #             # if room above
    #             if dungeon_map[y][x+1] == 1:
    #                 d_dict[build_coord(y,x)].west_door = dungeon.Door(direction='west',pos=(6,19), go_to=build_coord(y,x+1))
    #             # if room above
    #             if dungeon_map[y+1][x] == 1:
    #                 d_dict[build_coord(y,x)].south_door = dungeon.Door(direction='south',pos=(14,9), go_to=build_coord(y+1,x))
    #             d_dict[build_coord(y,x)].refresh()
    return d_dict

# builds coordinate strings out of int data
def build_coord(y, x):
    y_coord = ""
    x_coord = ""
    if y < 10:
        y_coord = "0"+str(y)
    else: y_coord = str(y)
    if x < 10:
        x_coord = "0"+str(x)
    else: x_coord = str(x)
    coordinate = y_coord+x_coord
    return coordinate


new_dungeon = dungeon_packer(make_dungeon_dict(), dungeon.test_dungeon)
dungeon_list.append(new_dungeon)


with open('dungeons/dungeon.pkl', 'wb') as pickle_file:
    pickle.dump(dungeon_list, pickle_file)
