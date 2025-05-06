import pygame
import random

class Snow:
    def __init__(self, screen):
        self.screen = screen
        self.current_level = 1
        self.size = random.randint(1,self.current_level * self.current_level + 1)
        self.surface = pygame.Surface((self.size,self.size))  # create a 3x3 surface
        self.surface.fill((255, 255, 255))     # fill it white (very important!)
        self.reset()
        self.rect = self.surface.get_rect()

    def reset(self):
        self.x = random.randint(0, self.screen.get_width())
        self.y = random.randint(-600, 0)
        self.size = random.randint(1,self.current_level + 9)
        self.speed = self.size
        self.surface = pygame.Surface((self.size,self.size))
        self.surface.fill((255,255,255))
        self.rect = self.surface.get_rect()
        

    def update(self,current_level):
        self.current_level = current_level
        self.y += self.speed // 4
        self.rect.topleft = (self.x, self.y)
        if self.y > self.screen.get_height():
            self.reset()

    def draw(self):
        self.screen.blit(self.surface, self.rect)

    def freeze(self):
        self.speed = 0