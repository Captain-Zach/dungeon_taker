import pygame
import random
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

class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((w,h))

# Call this function to make the test room for enemy or player testing purposes
# Also useful for bypassing lvl generation
def drawTestRoom(displaySurface, colorList):
    for y in range(0, len(testRoom), 1):
        for x in range(0, len(testRoom[y]), 1):
            if testRoom[y][x] == 0:
                pygame.draw.rect(displaySurface, colorList, (0 + (x * 40), 0 + (y * 40),40,40))

    pass

def drawTestRoomX(displaySurface, colorList):
    for y in range(0, len(roomList[0]), 1):
        for x in range(0, len(roomList[0][y]), 1):
            if roomList[0][y][x] == 0:
                
                pygame.draw.rect(displaySurface, colorList, (0 + (x * 40), 0 + (y * 40),40,40))

    pass

def generateRoom():
    newRoom = testRoom
    for y in range(1, len(newRoom) - 1, 1):
        
        for x in range(1, len(newRoom[y]) - 1, 1):
            if random.randint(0, 100) < wallChance:
                #this is the first print to fire off!
                print("x", x)
                newRoom[y][x] = 0
    
    roomList.append(newRoom)

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
            print("AHHHH!")
            return(True)
        #otherwise, we have to add the node to the burn list so we dont accidentally 
        #queue it again.
        burn.append(burn.cleanNode(queue.head))
        queue.dropFront()
        # NOTE
        queue = queue.removeDupes()
        queue.printSLL()
        if queue.head.nxt == None:
            print("YOU FAILEDDDD")
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
    return

def blankFill():
    for y in range(1, len(roomList[0]) - 1, 1):
        for x in range(1, len(roomList[0][y]) - 1, 1):
            if roomList[0][y][x] == 1:
                if searchTest(roomList[0], targX = x, targY=y) != True:
                    if random.randint(0,100) < 40:
                        print("filling in")
                        roomList[0][y][x] = 0
                    else:
                        print("start point", y,x)
                        print("No path, leaving empty")
                else:
                    print("found path, leaving clear")
    pass

def gateClear():
    print("Clearing squares nearest the exits")
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

    pass


###############################TEST CODE###############################
#searchTest(testRoom)

#searchTest(testRoomX)

#procRoom()

#procRoomX()