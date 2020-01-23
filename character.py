import pygame

class Character:
    def __init__(self, xPos = 370, yPos = 480, speed = 3, attack = 1, health = 10):
        self.sprite = pygame.image.load('images/princess.png')
        self.xPos = xPos
        self.yPos = yPos
        self.speed = speed
        self.attack = attack
        self.health = health
        #######Collision points#############
        self.top = (self.xPos + 16, self.yPos)
        self.right = (self.xPos + 32, self.yPos + 16)
        self.bottom = (self.xPos+ 16, self.yPos + 32)
        self.left = (self.xPos, self.yPos + 16)
        #######Collision points###########

        self.upTrigger = False
        self.downTrigger = False
        self.rightTrigger = False
        self.leftTrigger = False
        pass

    def movement(self):
        if self.upTrigger:
            self.yPos -= self.speed

        if self.downTrigger:
            self.yPos += self.speed

        if self.leftTrigger:
            self.xPos -= self.speed

        if self.rightTrigger:
            self.xPos += self.speed

    def inputHandler(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.leftTrigger = True
                    print("Left arrow is pressed")
                if event.key == pygame.K_RIGHT:
                    self.rightTrigger = True
                    print("Right arrow is pressed")
                if event.key == pygame.K_UP:
                    self.upTrigger = True
                    print("Up Key pressed")
                if event.key == pygame.K_DOWN:
                    self.downTrigger = True
                    print("Down Key pressed")

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.leftTrigger = False
                    print("Left Key up")
                if event.key == pygame.K_RIGHT:
                    self.rightTrigger = False
                    print("Right Key UP")
                if event.key == pygame.K_UP:
                    self.upTrigger = False
                    print("Up Key up")
                if event.key == pygame.K_DOWN:
                    self.downTrigger = False
                    print("Down Key up")

            if event.type == pygame.QUIT:
                return(False)
            else: return(True)
        return(True)
        