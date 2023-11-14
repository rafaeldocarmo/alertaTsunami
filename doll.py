import pygame
from pygame.locals import *
from gameobjects.Vector2 import Vector2

class Doll:
    def __init__(self, image_filename, position):
        self.image = pygame.image.load(image_filename)
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.position = Vector2(*position)
        self.saved = False

    def draw(self, screen):
        if not self.saved:
            screen.blit(self.image, (self.position.x, self.position.y))

    def check_collision(self, boat):
      if not self.saved:
         boat_rect = pygame.Rect(boat.position.x, boat.position.y, boat.image.get_width(), boat.image.get_height())
         doll_rect = pygame.Rect(self.position.x, self.position.y, self.image.get_width(), self.image.get_height())
         if boat_rect.colliderect(doll_rect):
               self.saved = True
               return True
      return False