import pygame
import math

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Collision_Box(pygame.sprite.Sprite):
    def __init__(self, parent, pos, shape):
        pygame.sprite.Sprite.__init__(self)
        if shape == 'vert':
            self.image = pygame.Surface((3, 6))
        if shape == 'lat':
            self.image = pygame.Surface((6, 3))
        # Setting color for testing.
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.pos = pos
        self.rect.center = parent.rect.center
        self.parent = parent
        self.triggered = False
        self.go_left = False
        self.go_up = False

        
    def update(self):
        self.rect.x = self.parent.rect.x + self.pos[0]
        self.rect.y = self.parent.rect.y + self.pos[1]


class Fly(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((8,8))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (300, 100)

        self.speed = 2.4
        self.speed2 = 1.2

        self.vert_angle = True
        self.lat_angle = True

        self.go_left = False
        self.go_up = False


        self.top_box = Collision_Box(self, (1,-2), 'lat')
        self.bottom_box = Collision_Box(self, (1,7), 'lat')
        self.left_box = Collision_Box(self, (-2,1), 'vert')
        self.right_box = Collision_Box(self, (7,1), 'vert')


        self.coll_boxes = [self.top_box, self.bottom_box, self.left_box, self.right_box]


    def update(self):
        if 0 < self.rect.x < 800 and 0 < self.rect.y < 600:
            if self.go_left == True:
                if self.lat_angle == True:
                    self.rect.x -= self.speed
                else:
                    self.rect.x -= self.speed2

            if self.go_left == False:
                if self.lat_angle == True:
                    self.rect.x += self.speed
                else:
                    self.rect.x += self.speed2

            if self.go_up == True:
                if self.vert_angle == True:
                    self.rect.y -= self.speed 
                else:
                    self.rect.y -= self.speed2

            if self.go_up == False:
                if self.vert_angle == True:
                    self.rect.y += self.speed
                else:
                    self.rect.y += self.speed2
        else:
            self.rect.x = 300
            self.rect.y = 20

class Basic_Chaser(pygame.sprite.Sprite):
    def __init__(self, xPos = 340, yPos = 460):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((8,8))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()

        self.rect.center = (xPos, yPos)
        self.xPos = xPos
        self.yPos = yPos


        self.go_left = True
        self.go_right = True
        self.go_up = True
        self.go_down = True



        self.top_box = Collision_Box(self, (1,9), 'lat')
        self.bottom_box = Collision_Box(self, (1,-4), 'lat')
        self.left_box = Collision_Box(self, (-4,1), 'vert')
        self.right_box = Collision_Box(self, (9,1), 'vert')


        self.coll_boxes = [self.top_box, self.bottom_box, self.left_box, self.right_box]

    def update_basic_chaser(self, player):
        xDelta = self.xPos - player.xPos
        yDelta = self.yPos - player.yPos


        # All the y and x coefficents are to make the 
        # chaser move at a non-right angle when 
        # proper. It only adds +-45 degrees 
        # making the chaser capable of 360 degree angle
        # movement!
        x_cof = 1
        y_cof = 1
        if xDelta != 0 and yDelta != 0:
            if xDelta > yDelta:
                if abs(xDelta/yDelta) < 2:
                    x_cof = abs(xDelta/yDelta)
                else:
                    x_cof = 2
                y_cof = 1
            if yDelta > xDelta:
                if abs(yDelta/xDelta) < 2:
                    y_cof = abs(yDelta/xDelta)
                else:
                    y_cof = 2
                x_cof = 1
        else:
            x_cof = 1
            y_cof = 1

        if math.sqrt((xDelta**2) + (yDelta**2)) < 200:
            # Moves chaser towards player's x cord
            # Moves chaser left
            if xDelta != 0:
                if xDelta > 0 and self.go_left == True:
                    self.xPos -= (1.5*x_cof)
                    # moves chaser right
                if xDelta < 0 and self.go_right == True:
                    self.xPos += (1.5*x_cof)
            # Moves chaster towards player's y cord
            # moves chaser down
            if yDelta != 0:
                if yDelta > 0 and self.go_down == True:
                    self.yPos -= (1.5*y_cof)
                    # moves chaser up
                if yDelta < 0 and self.go_up == True:
                    self.yPos += (1.5*y_cof)
        self.rect.center = (self.xPos, self.yPos)

        