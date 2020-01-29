import pygame

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
        self.speed = 5

        self.go_left = False
        self.go_up = False

        self.top_box = Collision_Box(self, (1,-2), 'lat')
        self.bottom_box = Collision_Box(self, (1,7), 'lat')
        self.left_box = Collision_Box(self, (-2,1), 'vert')
        self.right_box = Collision_Box(self, (6,1), 'vert')


        self.coll_boxes = [self.top_box, self.bottom_box, self.left_box, self.right_box]


    def update(self):
        if self.go_left == True:
            self.rect.x -= self.speed
        else: self.rect.x += self.speed
        if self.go_up == True:
            self.rect.y -= self.speed
        else: self.rect.y += self.speed
        pass