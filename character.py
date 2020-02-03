import pygame

# define colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Collision_Box(pygame.sprite.Sprite):
    def __init__(self, parent, pos, shape):
        pygame.sprite.Sprite.__init__(self)
        if shape == 'vert':
            self.image = pygame.Surface((8, 24))
        if shape == 'lat':
            self.image = pygame.Surface((24, 8))
        # Setting color for testing.
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.pos = pos
        self.rect.center = self.pos
        self.parent = parent
        self.triggered = False
        


    def update(self):
        self.rect.x = self.parent.rect.x + self.pos[0]
        self.rect.y = self.parent.rect.y + self.pos[1]

# class Collision_Group(pygame.sprite.Sprite):
#     def __init__(self, parent, offset):




class Player_Bullet(pygame.sprite.Sprite):
    def __init__(self, direction, origin, offset = 20):
        pygame.sprite.Sprite.__init__(self)
        if direction == 'LEFT' or direction == 'RIGHT':
            self.image = pygame.Surface((16,8))
        if direction == 'UP' or direction == 'DOWN':
            self.image = pygame.Surface((8,16))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.direction = direction
        self.origin = origin
        self.offset = offset
        self.speed = 20

        self.lifetime_frames = 30

        if self.direction == 'UP':
            target = (origin.rect.midtop[0], origin.rect.midtop[1] - self.offset)
            self.rect.center = target
        if self.direction == 'DOWN':
            target = (origin.rect.midbottom[0], origin.rect.midbottom[1] + self.offset)
            self.rect.center = target
        if self.direction == 'LEFT':
            target = (origin.rect.midleft[0] - self.offset, origin.rect.midleft[1] )
            self.rect.center = target
        if self.direction == 'RIGHT':
            target = (origin.rect.midright[0] + self.offset, origin.rect.midright[1])
            self.rect.center = target
            # self.rect.center[0] += self.offset

        self.game_running = True
    def update(self):
        if self.direction == 'UP':
            self.rect.y -= self.speed
        if self.direction == 'DOWN':
            self.rect.y += self.speed
        if self.direction == 'LEFT':
            self.rect.x -= self.speed
        if self.direction == 'RIGHT':
            self.rect.x += self.speed
        self.lifetime_frames -= 1
        if self.lifetime_frames < 1:
            self.kill()





class Player_Spear(pygame.sprite.Sprite):
    def __init__(self, direction, origin, offset = 100):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((16,64))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.direction = direction
        self.origin = origin
        self.offset = offset

        self.rot = 0

        self.lifetime_frames = 7

        if self.direction == 'UP':
            target = (origin.rect.midtop[0], origin.rect.midtop[1] - self.offset)
            self.rect.center = target
        if self.direction == 'DOWN':
            target = (origin.rect.midbottom[0], origin.rect.midbottom[1] + self.offset)
            self.rect.center = target
        if self.direction == 'LEFT':
            target = (origin.rect.midleft[0] - self.offset, origin.rect.midleft[1] )
            self.rect.center = target
        if self.direction == 'RIGHT':
            target = (origin.rect.midright[0] + self.offset, origin.rect.midright[1])
            self.rect.center = target
            # self.rect.center[0] += self.offset
        self.anim_counter = 0
        self.game_running = True
    def update(self):
        if self.direction == 'UP':
            self.anim_counter += 1
            if self.anim_counter == 1:
                self.image = pygame.image.load('sprites/stab_01.png')
            if self.anim_counter == 2:
                self.image = pygame.image.load('sprites/stab_02.png')
            if self.anim_counter == 3:
                self.image = pygame.image.load('sprites/stab_03.png')
            if self.anim_counter == 4:
                self.image = pygame.image.load('sprites/stab_03.png')
            if self.anim_counter == 5:
                self.image = pygame.image.load('sprites/stab_03.png')
            if self.anim_counter >= 6:
                self.image = pygame.image.load('sprites/stab_04.png')
            target = (self.origin.rect.midtop[0] + 3, self.origin.rect.midtop[1] - self.offset - 15)
            self.rect.center = target
        if self.direction == 'DOWN':
            self.anim_counter += 1
            if self.anim_counter == 1:
                self.image = pygame.image.load('sprites/stab_01.png')
                self.image = pygame.transform.rotate(self.image, 180)
            if self.anim_counter == 2:
                self.image = pygame.image.load('sprites/stab_02.png')
                self.image = pygame.transform.rotate(self.image, 180)
            if self.anim_counter == 3:
                self.image = pygame.image.load('sprites/stab_03.png')
                self.image = pygame.transform.rotate(self.image, 180)
            if self.anim_counter == 4:
                self.image = pygame.image.load('sprites/stab_03.png')
                self.image = pygame.transform.rotate(self.image, 180)
            if self.anim_counter == 5:
                self.image = pygame.image.load('sprites/stab_03.png')
                self.image = pygame.transform.rotate(self.image, 180)
            if self.anim_counter >= 6:
                self.image = pygame.image.load('sprites/stab_04.png')
                self.image = pygame.transform.rotate(self.image, 180)
            target = (self.origin.rect.midbottom[0] - 8, self.origin.rect.midbottom[1] + self.offset - 7)
            self.rect.center = target
        if self.direction == 'LEFT':
            self.anim_counter += 1
            if self.anim_counter == 1:
                self.image = pygame.image.load('sprites/stab_01.png')
                self.image = pygame.transform.rotate(self.image, 90)
            if self.anim_counter == 2:
                self.image = pygame.image.load('sprites/stab_02.png')
                self.image = pygame.transform.rotate(self.image, 90)
            if self.anim_counter == 3:
                self.image = pygame.image.load('sprites/stab_03.png')
                self.image = pygame.transform.rotate(self.image, 90)
            if self.anim_counter == 4:
                self.image = pygame.image.load('sprites/stab_03.png')
                self.image = pygame.transform.rotate(self.image, 90)
            if self.anim_counter == 5:
                self.image = pygame.image.load('sprites/stab_03.png')
                self.image = pygame.transform.rotate(self.image, 90)
            if self.anim_counter >= 6:
                self.image = pygame.image.load('sprites/stab_04.png')
                self.image = pygame.transform.rotate(self.image, 90)
            target = (self.origin.rect.midleft[0] - self.offset -17, self.origin.rect.midleft[1] + 25)
            self.rect.center = target
        if self.direction == 'RIGHT':
            self.anim_counter += 1
            if self.anim_counter == 1:
                self.image = pygame.image.load('sprites/stab_01.png')
                self.image = pygame.transform.rotate(self.image, -90)
            if self.anim_counter == 2:
                self.image = pygame.image.load('sprites/stab_02.png')
                self.image = pygame.transform.rotate(self.image, -90)
            if self.anim_counter == 3:
                self.image = pygame.image.load('sprites/stab_03.png')
                self.image = pygame.transform.rotate(self.image, -90)
            if self.anim_counter == 4:
                self.image = pygame.image.load('sprites/stab_03.png')
                self.image = pygame.transform.rotate(self.image, -90)
            if self.anim_counter == 5:
                self.image = pygame.image.load('sprites/stab_03.png')
                self.image = pygame.transform.rotate(self.image, -90)
            if self.anim_counter >= 6:
                self.image = pygame.image.load('sprites/stab_04.png')
                self.image = pygame.transform.rotate(self.image, -90)
            target = (self.origin.rect.midright[0] + self.offset - 10, self.origin.rect.midright[1] + 30)
            self.rect.center = target
        self.lifetime_frames -= 1
        if self.lifetime_frames < 1:
            self.kill()



class Player_Attack(pygame.sprite.Sprite):
    def __init__(self, direction, origin, offset = 5):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((64,32))
        self.image_orig = pygame.image.load('sprites/slash_01.png')
        self.image = self.image_orig.copy()
        self.rot = 0
        if direction == 'DOWN':
            pass
        if direction == 'LEFT' or direction == 'RIGHT':
            self.image = pygame.image.load('sprites/sword_01.png')
        # self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.direction = direction
        self.origin = origin
        self.offset = offset


        self.lifetime_frames = 7

        if self.direction == 'UP':
            target = (origin.rect.midbottom[0], origin.rect.midbottom[1] - self.offset)
            self.rect.center = target
        if self.direction == 'DOWN':
            target = (origin.rect.midbottom[0], origin.rect.midbottom[1] + self.offset)
            self.rect.center = target
        if self.direction == 'LEFT':
            target = (origin.rect.midleft[0] - self.offset, origin.rect.midleft[1] )
            self.rect.center = target
        if self.direction == 'RIGHT':
            target = (origin.rect.midright[0] + self.offset, origin.rect.midright[1])
            self.rect.center = target
            # self.rect.center[0] += self.offset

        self.game_running = True
        # Setting delay
        self.anim_delay = 0
        self.anim_counter = 0
    def update(self):
        if self.direction == 'UP':
            self.anim_counter += 1
            if self.anim_counter == 1:
                self.image = pygame.image.load('sprites/slash_01.png')
            if self.anim_counter == 2:
                self.image = pygame.image.load('sprites/slash_02.png')
            if self.anim_counter == 3:
                self.image = pygame.image.load('sprites/slash_03.png')
            if self.anim_counter == 4:
                self.image = pygame.image.load('sprites/slash_04.png')
            if self.anim_counter >= 5:
                self.image = pygame.image.load('sprites/slash_05.png')
            target = (self.origin.rect.midtop[0], self.origin.rect.midtop[1] - self.offset-8)
            self.rect.midtop = target
        if self.direction == 'DOWN':
            self.anim_counter += 1
            if self.anim_counter == 1:
                self.image = pygame.image.load('sprites/slash_01.png')
                self.image = pygame.transform.rotate(self.image, 180)
            if self.anim_counter == 2:
                self.image = pygame.image.load('sprites/slash_02.png')
                self.image = pygame.transform.rotate(self.image, 180)
            if self.anim_counter == 3:
                self.image = pygame.image.load('sprites/slash_03.png')
                self.image = pygame.transform.rotate(self.image, 180)
            if self.anim_counter == 4:
                self.image = pygame.image.load('sprites/slash_04.png')
                self.image = pygame.transform.rotate(self.image, 180)
            if self.anim_counter >= 5:
                self.image = pygame.image.load('sprites/slash_05.png')
                self.image = pygame.transform.rotate(self.image, 180)
            target = (self.origin.rect.midbottom[0] - 5, self.origin.rect.midbottom[1] + self.offset)
            self.rect.center = target
        if self.direction == 'LEFT':
            self.anim_counter += 1
            if self.anim_counter == 1:
                self.image = pygame.image.load('sprites/slash_01.png')
                self.image = pygame.transform.rotate(self.image, 90)
            if self.anim_counter == 2:
                self.image = pygame.image.load('sprites/slash_02.png')
                self.image = pygame.transform.rotate(self.image, 90)
            if self.anim_counter == 3:
                self.image = pygame.image.load('sprites/slash_03.png')
                self.image = pygame.transform.rotate(self.image, 90)
            if self.anim_counter == 4:
                self.image = pygame.image.load('sprites/slash_04.png')
                self.image = pygame.transform.rotate(self.image, 90)
            if self.anim_counter >= 5:
                self.image = pygame.image.load('sprites/slash_05.png')
                self.image = pygame.transform.rotate(self.image, 90)
            target = (self.origin.rect.topleft[0] - self.offset - 10, self.origin.rect.topleft[1] )
            self.rect.center = target
        if self.direction == 'RIGHT':
            self.anim_counter += 1
            if self.anim_counter == 1:
                self.image = pygame.image.load('sprites/slash_01.png')
                self.image = pygame.transform.rotate(self.image, -90)
            if self.anim_counter == 2:
                self.image = pygame.image.load('sprites/slash_02.png')
                self.image = pygame.transform.rotate(self.image, -90)
            if self.anim_counter == 3:
                self.image = pygame.image.load('sprites/slash_03.png')
                self.image = pygame.transform.rotate(self.image, -90)
            if self.anim_counter == 4:
                self.image = pygame.image.load('sprites/slash_04.png')
                self.image = pygame.transform.rotate(self.image, -90)
            if self.anim_counter >= 5:
                self.image = pygame.image.load('sprites/slash_05.png')
                self.image = pygame.transform.rotate(self.image, -90)
            target = (self.origin.rect.center[0] + self.offset -7 , self.origin.rect.center[1] -15)
            self.rect.center = target
        self.lifetime_frames -= 1
        if self.lifetime_frames < 1:
            self.kill()

        # self.rect.center = 

class Character(pygame.sprite.Sprite):
    def __init__(self, xPos = 370, yPos = 480, speed = 5, attack = 1, health = 10):
        pygame.sprite.Sprite.__init__(self)
        # Let's get started
        # self.image = pygame.Surface((32,32))
        self.state = None
        self.image = pygame.image.load('sprites/readyDown_01.png')
        # self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (xPos, yPos)
        self.xPos = xPos
        self.yPos = yPos
        self.speed = speed
        self.attack = attack
        self.health = health

        self.weapon = 1

        # Used for positions in the dungeon
        self.dungeon_pos = "0302"
        # Used for direction manipulation
        self.direction_lock = False
        self.direction = 'DOWN'
        self.upTrigger = False
        self.downTrigger = False
        self.rightTrigger = False
        self.leftTrigger = False
        self.attack = False
        
        # Used for collision and movement
        self.collide_up = False
        self.collide_down = False
        self.collide_left = False
        self.collide_right = False


        ######## Set collision boxes
        self.top_box = Collision_Box(self, (4, 0), shape = 'lat')
        self.bottom_box = Collision_Box(self, (4, 24), shape = 'lat')
        self.left_box = Collision_Box(self, (0,4), shape = 'vert')
        self.right_box = Collision_Box(self, (24,4), shape = 'vert')


        # all directional colliders to be added to groups.
        self.coll_list = [self.top_box, self.bottom_box, self.left_box, self.right_box]
        # This is the trigger to end the game
        self.game_running = True

    def update(self):
        self.movement()
        self.inputHandler()
        self.animation()
        pass
    
    def animation(self):
        if self.direction == 'UP':
            self.image = pygame.image.load('sprites/readyUp_01.png')
        if self.direction == 'DOWN':
            self.image = pygame.image.load('sprites/readyDown_01.png')
        if self.direction == 'LEFT':
            self.image = pygame.image.load('sprites/readyLeft_01.png')
        if self.direction == 'RIGHT':
            self.image = pygame.image.load('sprites/readyRight_01.png')
        

    def movement(self):
        if self.upTrigger and not self.collide_up:
            if self.direction_lock == False:
                self.direction = 'UP'
            self.yPos -= self.speed

        if self.downTrigger and not self.collide_down:
            if self.direction_lock == False:
                self.direction = 'DOWN'
            self.yPos += self.speed

        if self.leftTrigger and not self.collide_left:
            if self.direction_lock == False:
                self.direction = 'LEFT'
            self.xPos -= self.speed

        if self.rightTrigger and not self.collide_right:
            if self.direction_lock == False:
                self.direction = 'RIGHT'
            self.xPos += self.speed
        self.rect.center = (self.xPos, self.yPos)

    def inputHandler(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    if self.weapon > 2:
                        self.weapon = 1
                    else:
                        self.weapon += 1
                if event.key == pygame.K_ESCAPE:
                    print("credits scene go")
                    self.state = "CREDITS"
                if event.key == pygame.K_TAB:
                    self.direction_lock = True
                if event.key == pygame.K_LEFT:
                    self.leftTrigger = True
                if event.key == pygame.K_RIGHT:
                    self.rightTrigger = True
                if event.key == pygame.K_UP:
                    self.upTrigger = True
                if event.key == pygame.K_DOWN:
                    self.downTrigger = True
                # Now handling attack input
                if event.key == pygame.K_SPACE:
                    self.attack = True
                    # print("Attack key pressed")
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_TAB:
                    self.direction_lock = False
                if event.key == pygame.K_LEFT:
                    self.leftTrigger = False
                if event.key == pygame.K_RIGHT:
                    self.rightTrigger = False
                if event.key == pygame.K_UP:
                    self.upTrigger = False
                if event.key == pygame.K_DOWN:
                    self.downTrigger = False
            
            if event.type == pygame.QUIT:
                print("I clicked quit")
                self.game_running = False
            else: self.game_running = True
        
    