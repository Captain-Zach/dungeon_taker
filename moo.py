import pygame as pg
import sys
from os import path
from settings import *
from sprites import *
from tilemap import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT), pg.FULLSCREEN)
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.load_data()

    def load_data(self):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'images')
        map_folder = path.join(game_folder, 'maps')
        self.map = TiledMap(path.join(map_folder, 'village.tmx'))
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()
        # self.player_img = pg.image.load(path.join(img_folder, PLAYER_IMG)).convert_alpha()
        # self.bullet_img = pg.image.load(path.join(img_folder, BULLET_IMG)).convert_alpha()
        # self.mob_img = pg.image.load(path.join(img_folder, MOB_IMG)).convert_alpha()
        # self.wall_img = pg.image.load(path.join(img_folder, WALL_IMG)).convert_alpha()
        # self.wall_img = pg.transform.scale(self.wall_img, (TILESIZE, TILESIZE))

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.mobs = pg.sprite.Group()
        self.bullets = pg.sprite.Group()
        # for row, tiles in enumerate(self.map.data):
        #     for col, tile in enumerate(tiles):
        #         if tile == '1':
        #             Wall(self, col, row)
        #         if tile == 'M':
        #             Mob(self, col, row)
        #         if tile == 'P':
        #             self.player = Player(self, col, row)
        for tile_object in self.map.tmxdata.objects:
            if tile_object.name == 'player':
                self.player = Player(self, tile_object.x, tile_object.y)
            if tile_object.name == 'wall':
                Obstacle(self, tile_object.x, tile_object.y,
                         tile_object.width, tile_object.height)
        self.player = Player(self, 15, 23)
        self.camera = Camera(self.map.width, self.map.height)
        self.draw_debug = False

    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            thing = self.events()
            if thing == "MAIN":
                return("MAIN")
            self.update()
            self.draw()

    def quit(self):
        return("MAIN")

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()
        self.camera.update(self.player)

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        # self.screen.fill(BGCOLOR)
        self.screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return(self.quit())
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    return(self.quit())
                if event.key == pg.K_LEFT:
                    self.player.move(dx=-1)
                if event.key == pg.K_RIGHT:
                    self.player.move(dx=1)
                if event.key == pg.K_UP:
                    self.player.move(dy=-1)
                if event.key == pg.K_DOWN:
                    self.player.move(dy=1)

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

# create the game object
def moo():
    g = Game()
    g.show_start_screen()
    pg.mixer.init()
    pg.mixer.music.load('sounds/village_music.wav')
    pg.mixer.music.set_volume(0.4)
    pg.mixer.music.play(loops=-1)
    while True:
        g.new()
        thing = g.run()
        if thing == "MAIN":
            return("MAIN")
        g.show_go_screen()
    return("MAIN")