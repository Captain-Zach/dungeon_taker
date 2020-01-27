import pygame
import enemy
import character
import roomLib
import dungeon

# Initialize pygame
pygame.init()

######################################################################
#SETTINGS
screenWidth = 800
screenHeight = 600
FPS = 30
# timeDelay = 50 DEPRECATED





#Creates window, and clock, sets Icon
screen = pygame.display.set_mode((screenWidth, screenHeight ))
pygame.display.set_caption("Dungeon Taker: OTA")
icon = pygame.image.load('images/oubliette.png')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

######################################################################

player = character.Character()
door = dungeon.Door()
wallColor = (50, 50, 50)

running = True

def drawHandling():
    #this function handles the drawing in layers
    #RGB VALUES
    screen.fill((0,0,0))
    # pDraw()
    floor_sprites.draw(screen)
    all_sprites.draw(screen)
    wall_sprites.draw(screen)
    door_sprites.draw(screen)
    collision_sprites.draw(screen)
    attack_sprites.draw(screen)


# def spawn_handling():
#     if player.attack == True:
#         print("spawn thing now")
#         attack = character.Player_Attack(player.direction, player, 10)
#         all_sprites.add(attack)
#         player.attack = False
#         return(attack)

# sprite groups! <3 
floor_sprites = pygame.sprite.Group()
wall_sprites = pygame.sprite.Group()
door_sprites = pygame.sprite.Group()
attack_sprites = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()
collision_sprites = pygame.sprite.Group()
all_sprites.add(player)
# all_sprites.add(door)
door_sprites.add(door)
#get a list of sprites with built in location information
flyTest = enemy.Fly()
flyList = [flyTest]
all_sprites.add(flyTest)
enemy_sprites.add(flyTest)

# roomLib.procRoomX()


# Reads the map of dungeon room, and adds wall and floor sprites.
dungeonTiles = roomLib.drawTestRoom()
for tile in dungeonTiles:
    if tile.tile_type == 1:
        floor_sprites.add(tile)
    if tile.tile_type == 0:

        wall_sprites.add(tile)

coll_boxes = player.coll_list
for box in coll_boxes:
    collision_sprites.add(box)
colls = flyTest.coll_boxes
for box in colls:
    collision_sprites.add(box)

# testing fly collision

# Loading area for rooms


# A state machine for managing the main game loop



while running:

    clock.tick(FPS)
    # pygame.time.delay(timeDelay) DEPRECATED

    #Update
    
    all_sprites.update()
    # attack = spawn_handling()
    if player.attack == True:
        print("spawn thing now")
        attack = character.Player_Attack(player.direction, player, 10)
        attack_sprites.add(attack)
        # all_sprites.add(attack)
        player.attack = False
    attack_sprites.update()
    collision_sprites.update()
    door_sprites.update()
    running = player.game_running
    
    # if a player's collision boxes (nav boxes) hit a wall, this stops players from
    # continuing in that direction until they are free of it.
    hits = pygame.sprite.groupcollide(collision_sprites, wall_sprites, False, False)
    if player.top_box in hits:
        player.collide_up = True
    else: 
        player.collide_up = False
    if player.bottom_box in hits:
        player.collide_down = True
    else:
        player.collide_down = False
    if player.left_box in hits:
        player.collide_left = True
    else:
        player.collide_left = False
    if player.right_box in hits:
        player.collide_right = True
    else:
        player.collide_right = False

    # and now, for the fly object
    if flyTest.top_box in hits:
        flyTest.go_up = False
        # flyTest.up_hit()
    if flyTest.bottom_box in hits:
        flyTest.go_up = True
    if flyTest.left_box in hits:
        flyTest.go_left = False
    if flyTest.right_box in hits:
        flyTest.go_left = True


    ticks = pygame.sprite.groupcollide(enemy_sprites, attack_sprites, True, False)
    if flyTest in ticks:
        print("YEEEEETT")
    if player in ticks:
        print("scored a hit")
    if ticks:
        print("the fly is hit!")

    # trav means travel.  If collision with player sprite, lets move to the next room
    trav = pygame.sprite.groupcollide(door_sprites, all_sprites, False, False)
    if door in trav:
        print("I'm a door!")
        # door.change_rooms(player)
    # Draw / render
    drawHandling()

    pygame.display.flip()

    
    

quit()
