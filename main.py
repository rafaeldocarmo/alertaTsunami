import pygame
from pygame.locals import *
from sys import exit
from gameobjects.Vector2 import Vector2
from boat import Boat

background_image_filename = 'bg-mar.jpeg'
mask_background = 'bg-mar-overlay.png'

pygame.init()
screen = pygame.display.set_mode((1024, 1024), 0, 32)

collision_mask = pygame.image.load(mask_background).convert()
background = pygame.image.load(background_image_filename).convert()

boat = Boat('boat.png', (410, 410), 100, collision_mask)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    boat.move(keys, clock.get_time() / 1000.0)
    boat.check_bounds(screen.get_width(), screen.get_height())

    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))

    boat.draw(screen)

    pygame.display.update()
    clock.tick(60)
