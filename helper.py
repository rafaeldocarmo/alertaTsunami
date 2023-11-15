import pygame
import math
from pygame.locals import *
from gameobjects.Vector2 import Vector2

class Helper(pygame.sprite.Sprite):
    def __init__(self, image_filename, initial_position, speed):
        super().__init__()
        self.original_image = pygame.transform.scale(pygame.image.load(image_filename), (70, 70))  # Armazene a imagem original
        self.image = self.original_image.copy()  # A imagem que será desenhada
        self.rect = self.image.get_rect()
        self.position = Vector2(*initial_position)  # Armazene a posição como um Vector2
        self.previous_position = Vector2(*initial_position)
        self.rect.topleft = initial_position
        self.speed = speed
        self.target = None
        self.visible = False
        self.timer = 0

    def move_to(self, doll):
        self.target = Vector2(*doll.rect.topleft)  # Armazene o alvo como um Vector2

    def update(self, dt):
         if self.timer > 0:
            self.timer -= dt
            if self.timer <= 0:
                self.visible = False
         if self.target:
            direction = self.target - self.position
            if direction.get_magnitude() > 0: 
                direction.normalize()
                self.position += direction * self.speed * dt
                self.rect.topleft = (int(self.position.x), int(self.position.y)) 
                angle = -math.degrees(math.atan2(direction.y, direction.x)) 
                self.image = pygame.transform.rotate(self.original_image, -angle + 90)
                if (self.target - self.position).get_magnitude() < 5:
                    self.target = None

    def draw(self, screen):
        if self.visible:
            screen.blit(self.image, (self.rect.x, self.rect.y))
