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
            self.image = pygame.Surface((3, 3))
        if shape == 'lat':
            self.image = pygame.Surface((3, 3))
        # Setting color for testing.
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.pos = pos
        self.rect.center = self.pos
        self.parent = parent
        self.triggered = False
        self.go_left = False
        self.go_up = False

        



class Fly(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((4,4))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (300, 100)
        self.speed = 5

        self.go_left = False
        self.go_up = False

        self.top_box = Collision_Box(self, (0,0), 'lat')


    def update():
        pass