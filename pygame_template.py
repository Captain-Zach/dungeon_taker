# Pygame template - skeleton for a new pygame project
import pygame
import random

WIDTH = 800
HEIGHT = 600
FPS = 30

#initialize pygame create window, and clock
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Template")
clock = pygame.time.Clock()


# Game loop
running = True
while running:
    # Process input (events)

    #Update

    # Draw / render
    screen.fill()
