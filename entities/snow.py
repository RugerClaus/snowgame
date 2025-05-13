import pygame
import random

class Snow:
    def __init__(self, screen):
        self.screen = screen
        self.current_level = 1
        self.size = random.randint(1,self.current_level * self.current_level + 1)
        if self.size >= 30:
            self.size = 30
        self.surface = pygame.Surface((self.size,self.size))
        self.surface.fill((255, 255, 255))     
        self.reset()
        self.rect = self.surface.get_rect()

    def reset(self):
        self.x = random.randint(0, self.screen.get_width())
        self.y = random.randint(-600, 0)
        self.size = random.randint(1,self.current_level + 9)
        self.speed = 0.01
        self.surface = pygame.Surface((self.size,self.size))
        self.surface.fill((255,255,255))
        self.rect = self.surface.get_rect()
        

    def update(self,current_level):
        self.current_level = current_level
        acceleration = 0.03
        self.speed += acceleration
        self.y += self.speed
        if self.speed >= 10:
            acceleration = 0
        self.rect.topleft = (self.x, self.y)
        if self.y > self.screen.get_height() - 100:
            self.reset()

    def draw(self):
        self.screen.blit(self.surface, self.rect)

    def freeze(self):
        self.speed = 0