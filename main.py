import pygame
from pygame.locals import *
from sys import exit
from gameobjects.Vector2 import Vector2

screen_width = 1024
screen_height = 1024
bg_tela_inicial = 'bg-telafundo.jpg'
background_image_filename = 'bg-mar.jpeg'
sprite_image_filename = 'boat.png'
mask_background = 'bg-mar-overlay.jpg'

pygame.init()

screen = pygame.display.set_mode((1024, 1024), 0, 32)
initial_background = pygame.image.load(bg_tela_inicial).convert()

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

button_width = 200
button_height = 50
play_button_rect = pygame.Rect((screen_width - button_width) // 2, screen_height // 2 - button_height, button_width, button_height)
exit_button_rect = pygame.Rect((screen_width - button_width) // 2, screen_height // 2 + 20, button_width, button_height)

show_initial_screen = True

while show_initial_screen:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos

            if play_button_rect.collidepoint(mouse_x, mouse_y):
                show_initial_screen = False

            elif exit_button_rect.collidepoint(mouse_x, mouse_y):
                pygame.quit()
                exit()

    screen.blit(initial_background, (0, 0))

    pygame.draw.rect(screen, (200, 200, 200, 128), play_button_rect)
    pygame.draw.rect(screen, (200, 200, 200, 128), exit_button_rect)

    font = pygame.font.Font(None, 36)
    play_text = font.render('PLAY', True, (255, 255, 255))
    play_text_rect = play_text.get_rect(center=play_button_rect.center)
    screen.blit(play_text, play_text_rect)

    exit_text = font.render('EXIT', True, (255, 255, 255))
    exit_text_rect = exit_text.get_rect(center=exit_button_rect.center)
    screen.blit(exit_text, exit_text_rect)

    pygame.display.update()

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
