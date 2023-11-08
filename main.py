import pygame
from pygame.locals import *
from sys import exit
from gameobjects.Vector2 import Vector2

background_image_filename = 'bg-mar.jpeg'
sprite_image_filename = 'boat.png'
mask_background = 'bg-mar-overlay.jpg'

pygame.init()

screen = pygame.display.set_mode((920, 920), 0, 32)

collision_mask = pygame.image.load(mask_background).convert()
background = pygame.image.load(background_image_filename).convert()
novo_tamanho = (70, 35)
sprite = pygame.transform.scale(pygame.image.load(sprite_image_filename), novo_tamanho)

clock = pygame.time.Clock()

position = Vector2(410, 410)
speed = 250
heading = Vector2()

def check_bounds(position):
    if position.x < 0:
        position.x = 0
    elif position.x >= screen.get_width() - sprite.get_width():
        position.x = screen.get_width() - sprite.get_width()

    if position.y < 0:
        position.y = 0
    elif position.y >= screen.get_height() - sprite.get_height():
        position.y = screen.get_height() - sprite.get_height()

    boat_rect = sprite.get_rect(topleft=(position.x, position.y))
    if boat_rect.colliderect(collision_mask.get_rect()):
        position = Vector2(boat_rect.topleft)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        position.x -= speed * clock.get_time() / 1000.0
    if keys[K_RIGHT]:
        position.x += speed * clock.get_time() / 1000.0
    if keys[K_UP]:
        position.y -= speed * clock.get_time() / 1000.0
    if keys[K_DOWN]:
        position.y += speed * clock.get_time() / 1000.0

    screen.blit(background, (0, 0))
    screen.blit(sprite, (position.x, position.y))

    check_bounds(position)

    pygame.display.update()
    clock.tick(60)
