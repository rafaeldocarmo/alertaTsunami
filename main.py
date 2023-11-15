import pygame
from pygame.locals import *
from sys import exit
from gameobjects.Vector2 import Vector2
from boat import Boat
from doll import Doll

screen_width = 1024
screen_height = 900
bg_tela_inicial = './bg-telafundo.jpg'
background_image_filename = './bg-mar.jpeg'
mask_background = './bg-mar-overlay.png'

pygame.init()
pygame.mixer.init()

#SONS
som_barco = pygame.mixer.Sound('sombarco.mp3')
pygame.mixer.music.load('space.mp3')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)


screen = pygame.display.set_mode((1024, 900), 0, 32)
initial_background = pygame.image.load(bg_tela_inicial).convert()

collision_mask = pygame.image.load(mask_background).convert()
background = pygame.image.load(background_image_filename).convert()

boat = Boat('./boat.png', (410, 410), 100, collision_mask)

# Nível 1
image_filenames_level1 = ['./doll1.png', './doll2.png', './doll3.png', './doll4.png']
positions_level1 = [(500, 50), (200, 650), (90, 300), (900, 500)]
dolls_level1 = [Doll(image_filename, position) for image_filename, position in zip(image_filenames_level1, positions_level1)]

image_filenames_level2 = ['./doll1.png', './doll2.png', './doll3.png', './doll4.png', './doll5.png', './doll6.png']
positions_level2 = [(20, 20), (900, 1000), (90, 300), (50, 900), (900, 50), (500, 600)]
dolls_level2 = [Doll(image_filename, position) for image_filename, position in zip(image_filenames_level2, positions_level2)]

image_filenames_level3 = ['./doll1.png', './doll2.png', './doll3.png', './doll4.png', './doll5.png', './doll6.png', './doll7.png', './doll8.png', './doll9.png', './doll10.png']
positions_level3 = [(20, 20), (900, 1000), (90, 300), (50, 900), (900, 50), (500, 50), (200, 650), (600, 800), (900, 500), (700, 300)]
dolls_level3 = [Doll(image_filename, position) for image_filename, position in zip(image_filenames_level3, positions_level3)]

current_level = 1

if current_level == 1:
    dolls = dolls_level1
elif current_level == 2:
    dolls = dolls_level2
elif current_level == 3:
    dolls = dolls_level3

clock = pygame.time.Clock()

TIMEREVENT = pygame.USEREVENT + 1
pygame.time.set_timer(TIMEREVENT, 1000) 

game_time = 55  
original_game_time = game_time

button_width = 200
button_height = 50
play_button_rect = pygame.Rect((screen_width - button_width) // 2, screen_height // 2 - button_height, button_width, button_height)
exit_button_rect = pygame.Rect((screen_width - button_width) // 2, screen_height // 2 + 20, button_width, button_height)

show_initial_screen = True
game_over = False

font = pygame.font.Font(None, 36)
score = 0
menu_button_rect = pygame.Rect((screen_width - button_width) // 2, screen_height // 2 + 90, button_width, button_height)
instructions_button_rect = pygame.Rect((screen_width - button_width) // 2, screen_height // 2 + 160, button_width, button_height)
sound_button_rect = pygame.Rect((screen_width - button_width) // 2, screen_height // 2 + 230, button_width, button_height)
sound_on = True

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

            elif menu_button_rect.collidepoint(mouse_x, mouse_y):
                # Adicione código para mostrar o menu
                pass

            elif instructions_button_rect.collidepoint(mouse_x, mouse_y):
                # Adicione código para mostrar instruções
                pass

            elif sound_button_rect.collidepoint(mouse_x, mouse_y):
                # Adicione código para ligar/desligar som
                sound_on = not sound_on

    screen.blit(initial_background, (0, 0))

    pygame.draw.rect(screen, (200, 200, 200, 128), play_button_rect)
    pygame.draw.rect(screen, (200, 200, 200, 128), instructions_button_rect)
    pygame.draw.rect(screen, (200, 200, 200, 128), sound_button_rect)
    pygame.draw.rect(screen, (200, 200, 200, 128), exit_button_rect)

    font = pygame.font.Font(None, 36)
    play_text = font.render('PLAY', True, (255, 255, 255))
    play_text_rect = play_text.get_rect(center=play_button_rect.center)
    screen.blit(play_text, play_text_rect)

    instructions_text = font.render('Instruções', True, (255, 255, 255))
    instructions_text_rect = instructions_text.get_rect(center=instructions_button_rect.center)
    screen.blit(instructions_text, instructions_text_rect)

    sound_text = font.render('Som: ' + ('Ligado' if sound_on else 'Desligado'), True, (255, 255, 255))
    sound_text_rect = sound_text.get_rect(center=sound_button_rect.center)
    screen.blit(sound_text, sound_text_rect)

    exit_text = font.render('EXIT', True, (255, 255, 255))
    exit_text_rect = exit_text.get_rect(center=exit_button_rect.center)
    screen.blit(exit_text, exit_text_rect)

    pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.mixer.music.stop()
            pygame.quit()
            exit()
        elif event.type == TIMEREVENT and not show_initial_screen and not game_over:
            game_time -= 1 
            if game_time <= 0: 
                show_initial_screen = True
                game_over = True

        elif event.type == MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos

            if sound_button_rect.collidepoint(mouse_x, mouse_y):
                sound_on = not sound_on
                if sound_on:
                    pygame.mixer.music.set_volume(0.1)
                else:
                    pygame.mixer.music.set_volume(0.0)

    keys = pygame.key.get_pressed()
    boat.move(keys, clock.get_time() / 1000.0)
    boat.check_bounds(screen.get_width(), screen.get_height())

    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))

    boat.draw(screen)
    
    for doll in dolls:
        doll.draw(screen)
        if doll.check_collision(boat):
            game_time += 0
            som_barco.play()
            score += 10

    dolls_left = sum(not doll.saved for doll in dolls)
    dolls_text = font.render('Resgatar: ' + str(dolls_left), True, (255, 255, 255))
    screen.blit(dolls_text, (10, 50)) 

    score_text = font.render('Pontuação: ' + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 70))

    font = pygame.font.Font(None, 36)
    time_text = font.render('Time: ' + str(game_time), True, (255, 255, 255))
    screen.blit(time_text, (10, 10))
    
    level_text = font.render('Level: ' + str(current_level), True, (255, 255, 255))
    screen.blit(level_text, (10, 90))

    if dolls_left == 0:
        current_level += 1
        game_time = 60

        if current_level == 1:
            dolls = dolls_level1
        elif current_level == 2:
            dolls = dolls_level2
        elif current_level == 3:
            dolls = dolls_level3

    pygame.display.update()
    clock.tick(60)

    if game_over:
            while game_over:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        exit()
                    elif event.type == MOUSEBUTTONDOWN:
                        mouse_x, mouse_y = event.pos

                        if play_button_rect.collidepoint(mouse_x, mouse_y):
                            game_over = False
                            show_initial_screen = True
                            game_time = original_game_time

                        elif exit_button_rect.collidepoint(mouse_x, mouse_y):
                            pygame.quit()
                            exit()        

                font = pygame.font.Font(None, 72)

                pygame.draw.rect(screen, (200, 200, 200, 128), play_button_rect)
                pygame.draw.rect(screen, (200, 200, 200, 128), exit_button_rect)


                game_over_text = font.render('Game Over', True, (255, 0, 0))
                game_over_rect = game_over_text.get_rect(center=(screen_width // 2, screen_height // 4))
                screen.blit(game_over_text, game_over_rect)

                restart_text = font.render('Restart', True, (0, 0, 0))
                restart_rect = restart_text.get_rect(center=play_button_rect.center)
                screen.blit(restart_text, restart_rect)

                exit_text = font.render('Exit', True, (0, 0, 0))
                exit_rect = exit_text.get_rect(center=exit_button_rect.center)
                screen.blit(exit_text, exit_rect)

                pygame.display.update()
