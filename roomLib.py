import random

import pygame

import node

wallChance = 50
reducer = 50

# north gate = [1,9] [1,8] [1,10] , [2,8] [2,9] [2,10]
# south gate = [13,8] [13,9] [13,10] , [12,8] [12,9] [12,10]

testRoom= [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
]

#for testing pathfinding
testRoomX= [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
]

firstXSuccess = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], 
    [0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0], 
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0], 
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0], 
    [0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], 
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0], 
    [0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0], 
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], 
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0], 
    [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0], 
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0], 
    [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0], 
    [0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

secondXSuccess = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], 
    [0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0], 
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0], 
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0], 
    [0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], 
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0], 
    [0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0], 
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], 
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0], 
    [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0], 
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0], 
    [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0], 
    [0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
roomList = []

WHITE = (255,255,255)
GREY = (50,50,50)
BLACK = (0,0,0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Block(pygame.sprite.Sprite):
    def __init__(self, xPos, yPos, tile_type):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40,40))
        if tile_type == 1:
            self.image.fill(BLACK)
            self.rect = self.image.get_rect()
        if tile_type == 0:
            self.image.fill(GREY)
            self.rect = self.image.get_rect()
        self.rect.topleft = ((xPos*40),(yPos*40))
        self.tile_type = tile_type

class Room:
    #for use with 
    def __init__(self):
        self.north = False
        self.south = False
        self.east = False
        self.west = False

        self.n_room = None
        self.s_room = None
        self.e_room = None
        self.w_room = None

        self.room = procRoomY(self.north, self.south, self.east, self.south)











# Call this function to make the test room for enemy or player testing purposes
# Also useful for bypassing lvl generation
def drawTestRoom():
    dungeonSprites = []
    for y in range(0, len(testRoom), 1):
        for x in range(0, len(testRoom[y]), 1):
            # populate a list to be returned containing sprites for the sprite god.
            dungeonSprites.append(Block(x,y,testRoom[y][x]))
            # if testRoom[y][x] == 0:
            #     pygame.draw.rect(displaySurface, colorList, (0 + (x * 40), 0 + (y * 40),40,40))
    return dungeonSprites

def drawTargetRoom(target_room):
    dungeonSprites = []
    for y in range(0, len(target_room), 1):
        for x in range(0, len(target_room[y]), 1):
            # populate a list to be returned containing sprites for the sprite god.
            dungeonSprites.append(Block(x,y,target_room[y][x]))
            # if testRoom[y][x] == 0:
            #     pygame.draw.rect(displaySurface, colorList, (0 + (x * 40), 0 + (y * 40),40,40))
    return dungeonSprites

def drawTestRoomX(displaySurface, colorList):
    for y in range(0, len(roomList[0]), 1):
        for x in range(0, len(roomList[0][y]), 1):
            if roomList[0][y][x] == 0:
                
                pygame.draw.rect(displaySurface, colorList, (0 + (x * 40), 0 + (y * 40),40,40))

    pass

def generateRoom():
    newRoom = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
]
    for y in range(1, len(newRoom) - 1, 1):
        
        for x in range(1, len(newRoom[y]) - 1, 1):
            if random.randint(0, 100) < wallChance:
                #this is the first print to fire off!
                print("x", x)
                newRoom[y][x] = 0
    return(newRoom)

def drawRandRoom(displaySurface, colorList):
    #roomList[TARGETROOM] will be passed through a parameter
    room2render = roomList[0]
    for y in range(0, len(room2render), 1):
        for x in range(0, len(room2render[y]), 1):
            if testRoom[y][x] == 0:
                pygame.draw.rect(displaySurface, colorList, (0 + (x * 40), 0 + (y * 40),40,40))
    x=0
    pass

    
def reductor():
    #roomList[TARGETROOM] will be passed through a parameter

    for y in range(1, len(roomList[0]) - 1, 1):
        for x in range(1, len(roomList[0][y]) - 1, 1):
            if roomList[0][y][x] == 0:
                if random.randint(0, 100) < reducer:
                    roomList[0][y][x] = 1
    pass
    

    
def reductorX(target_room):
    #roomList[TARGETROOM] will be passed through a parameter

    for y in range(1, len(target_room) - 1, 1):
        for x in range(1, len(target_room[y]) - 1, 1):
            if target_room[y][x] == 0:
                if random.randint(0, 100) < reducer:
                    target_room[y][x] = 1
    pass
    
def searchTest(room, startX = 9, startY = 13, targX = 9, targY = 1): #will eventually accept arguments for 
    #single use search test.
    start = node.Node([startY, startX])
    #NOTE!
    queue = node.SLL(start)
    burn = node.SLL()
    target = [targY,targX]
    run = True

    #hard code logic for step one
    while run:
        coordY = queue.head.val[0]
        coordX = queue.head.val[1]

        #check left
        if room[coordY][coordX - 1] != 0:
            if burn.valCheck([coordY,coordX-1]) != True:
                queue.append(node.Node([coordY, coordX - 1]))
                queue.printSLL()
        #Check Up
        if room[coordY -1][coordX] != 0:
            if burn.valCheck([coordY-1,coordX]) != True:
                queue.append(node.Node([coordY- 1, coordX ]))
                queue.printSLL()
        
        #Check Right
        if room[coordY][coordX + 1] != 0:
            if burn.valCheck([coordY,coordX+1]) != True:
                queue.append(node.Node([coordY, coordX + 1]))
                queue.printSLL()

        #Check Down
        if room[coordY + 1][coordX] != 0:
            if burn.valCheck([coordY,coordX-1]) != True: 
                queue.append(node.Node([coordY + 1, coordX]))
                queue.printSLL()
        #if value is found in SLL, pathfinding was a success
        if queue.valCheck(target):
            # print("AHHHH!")
            return(True)
        #otherwise, we have to add the node to the burn list so we dont accidentally 
        #queue it again.
        burn.append(burn.cleanNode(queue.head))
        queue.dropFront()
        # NOTE
        queue = queue.removeDupes()
        queue.printSLL()
        if queue.head.nxt == None:
            # print("YOU FAILEDDDD")
            return False
    #return False

def procRoom():
    generateRoom()
    path = searchTest(roomList[0])
    while path != True:
        reductor()
        path = searchTest(roomList[0])
    return

def procRoomX():
    generateRoom()
    blankFill()
    path = searchTest(roomList[0])
    while path != True:
        blankFill()
        gateClear()
        reductor()
        path = searchTest(roomList[0])
    print("DONE")
    print(roomList[0])
    return(roomList[0])

def procRoomY():
    newRoom = generateRoom()
    blankFillX(newRoom)
    path = searchTest(newRoom)
    while path != True:
        blankFillX(newRoom)
        gateClearX(newRoom)
        reductorX(newRoom)
        path = searchTest(newRoom)
    # line cut
    gateClearX(newRoom)
    for x in range(1, len(newRoom[6])-1,1):
        newRoom[6][x] = 1
        

    print("DONE")
    print(newRoom)
    return(newRoom)

def blankFill():
    for y in range(1, len(roomList[0]) - 1, 1):
        for x in range(1, len(roomList[0][y]) - 1, 1):
            if roomList[0][y][x] == 1:
                if searchTest(roomList[0], targX = x, targY=y) != True:
                    if random.randint(0,100) < 40:
                        # print("filling in")
                        roomList[0][y][x] = 0
                    else:
                        pass
                        # print("start point", y,x)
                        # print("No path, leaving empty")
                else:
                    pass
                    # print("found path, leaving clear")

def blankFillX(room_target):
    for y in range(1, len(room_target) - 1, 1):
        for x in range(1, len(room_target[y]) - 1, 1):
            if room_target[y][x] == 1:
                if searchTest(room_target, targX = x, targY=y) != True:
                    if random.randint(0,100) < 40:
                        # print("filling in")
                        room_target[y][x] = 0
                    else:
                        pass
                        # print("start point", y,x)
                        # print("No path, leaving empty")
                else:
                    pass
                    # print("found path, leaving clear")


def gateClear():
    # print("Clearing squares nearest the exits")
    #access individual squares
    # North Gate
    roomList[0][1][9] = 1
    roomList[0][1][8] = 1
    roomList[0][1][10] = 1
    roomList[0][2][8] = 1
    roomList[0][2][9] = 1
    roomList[0][2][10] = 1
    # South Gate
    roomList[0][13][8] = 1
    roomList[0][13][9] = 1
    roomList[0][13][10] = 1
    roomList[0][12][8] = 1
    roomList[0][12][9] = 1
    roomList[0][12][10] = 1
    # East Gate
    roomList[0][6][1] = 1
    roomList[0][7][1] = 1
    roomList[0][5][1] = 1
    roomList[0][6][2] = 1
    roomList[0][7][2] = 1
    roomList[0][5][2] = 1
    # West Gate
    roomList[0][6][17] = 1
    roomList[0][7][17] = 1
    roomList[0][5][17] = 1
    roomList[0][6][18] = 1
    roomList[0][7][18] = 1
    roomList[0][5][18] = 1
    pass

def gateClearX(target_room):
    # print("Clearing squares nearest the exits")
    #access individual squares
    # North Gate
    target_room[1][9] = 1
    target_room[1][8] = 1
    target_room[1][10] = 1
    target_room[2][8] = 1
    target_room[2][9] = 1
    target_room[2][10] = 1
    # South Gate
    target_room[13][8] = 1
    target_room[13][9] = 1
    target_room[13][10] = 1
    target_room[12][8] = 1
    target_room[12][9] = 1
    target_room[12][10] = 1
    # East Gate
    target_room[6][1] = 1
    target_room[7][1] = 1
    target_room[5][1] = 1
    target_room[6][2] = 1
    target_room[7][2] = 1
    target_room[5][2] = 1
    # West Gate
    target_room[6][17] = 1
    target_room[7][17] = 1
    target_room[5][17] = 1
    target_room[6][18] = 1
    target_room[7][18] = 1
    target_room[5][18] = 1
    pass


###############################TEST CODE###############################
#searchTest(testRoom)

#searchTest(testRoomX)

#procRoom()

#procRoomX()
