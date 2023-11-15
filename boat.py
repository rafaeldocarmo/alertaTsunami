import pygame
from pygame.locals import *
from gameobjects.Vector2 import Vector2

class Boat(pygame.sprite.Sprite):
    def __init__(self, image_filename, initial_position, speed, mask):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(image_filename), (40, 14))
        self.boatInicial = self.image
        self.rect = self.image.get_rect()
        self.rect.topleft = initial_position
        self.speed = speed
        self.heading = Vector2()  # Inicialmente sem direção
        self.mask = mask

    def move(self, keys, dt):
        # Movimento apenas com as setas
        old_position = Vector2(self.rect.x, self.rect.y)
        if keys[K_LEFT]:
            self.rect.x -= self.speed * dt
            self.image = pygame.transform.rotate(self.boatInicial, 0)
        if keys[K_RIGHT]:
            self.rect.x += self.speed * dt
            self.image = pygame.transform.rotate(self.boatInicial, 180)
        if keys[K_UP]:
            self.rect.y -= self.speed * dt
            self.image = pygame.transform.rotate(self.boatInicial, -90)
        if keys[K_DOWN]:
            self.rect.y += self.speed * dt
            self.image = pygame.transform.rotate(self.boatInicial, 90)

        if not self.can_move_to(self.rect.x, self.rect.y):
            self.rect.x, self.rect.y = old_position

    def can_move_to(self, x, y):
        # Verifica os quatro cantos do barco
        for dx in [0, self.image.get_width()]:
            for dy in [0, self.image.get_height()]:
                # Verifica se as coordenadas estão dentro dos limites da máscara
                if 0 <= x + dx < self.mask.get_size()[0] and 0 <= y + dy < self.mask.get_size()[1]:
                    if self.mask.get_at((int(x + dx), int(y + dy))) != (255, 255, 255, 255):
                        return False
        return True

    def check_bounds(self, screen_width, screen_height):
        # Verifica os limites da tela
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x >= screen_width - self.image.get_width():
            self.rect.x = screen_width - self.image.get_width()

        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y >= screen_height - self.image.get_height():
            self.rect.y = screen_height - self.image.get_height()

    def draw(self, screen):
        # Desenha o barco na tela
        screen.blit(self.image, (self.rect.x, self.rect.y))
