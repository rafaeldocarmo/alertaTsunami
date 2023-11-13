import pygame
from pygame.locals import *
from gameobjects.Vector2 import Vector2

class Boat:
    def __init__(self, image_filename, initial_position, speed, mask):
        self.image = pygame.transform.scale(pygame.image.load(image_filename), (53, 46))
        self.boatInicial = self.image
        self.position = Vector2(*initial_position)
        self.speed = speed
        self.heading = Vector2()  # Inicialmente sem direção
        self.mask = mask

    def move(self, keys, dt):
        # Movimento apenas com as setas
        old_position = Vector2(self.position.x, self.position.y)
        if keys[K_LEFT]:
            self.position.x -= self.speed * dt
            self.image = pygame.transform.rotate(self.boatInicial, 0)
        if keys[K_RIGHT]:
            self.position.x += self.speed * dt
            self.image = pygame.transform.rotate(self.boatInicial, 180)
        if keys[K_UP]:
            self.position.y -= self.speed * dt
            self.image = pygame.transform.rotate(self.boatInicial, -90)
        if keys[K_DOWN]:
            self.position.y += self.speed * dt
            self.image = pygame.transform.rotate(self.boatInicial, 90)


        if not self.can_move_to(self.position.x, self.position.y):
            self.position = old_position
    
    def can_move_to(self, x, y):
        # Verifica os quatro cantos do barco
        for dx in [0, self.image.get_width()]:
            for dy in [0, self.image.get_height()]:
                if self.mask.get_at((int(x + dx), int(y + dy))) != (255, 255, 255, 255):
                    return False
        return True

    def check_bounds(self, screen_width, screen_height):
        # Verifica os limites da tela
        if self.position.x < 0:
            self.position.x = 0
        elif self.position.x >= screen_width - self.image.get_width():
            self.position.x = screen_width - self.image.get_width()

        if self.position.y < 0:
            self.position.y = 0
        elif self.position.y >= screen_height - self.image.get_height():
            self.position.y = screen_height - self.image.get_height()

    def draw(self, screen):
        # Desenha o barco na tela
        screen.blit(self.image, (self.position.x, self.position.y))
