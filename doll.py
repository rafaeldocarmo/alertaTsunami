import pygame
from pygame.locals import *
from gameobjects.Vector2 import Vector2
class Doll(pygame.sprite.Sprite):
    def __init__(self, image_filename, position):
        super().__init__()
        self.image = pygame.image.load(image_filename)
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.saved = False

    def draw(self, screen):
        if not self.saved:
            screen.blit(self.image, self.rect)

    def check_collision(self, boat, helper=None):
        if pygame.sprite.collide_rect(self, boat) and not self.saved:
            self.saved = True
            return True
        elif helper and pygame.sprite.collide_rect(self, helper) and not self.saved:
            self.saved = True
            helper.timer = 1
            return True
        return False

