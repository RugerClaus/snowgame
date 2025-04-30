import pygame
import random

class Snow:
    def __init__(self, screen):
        self.screen = screen
        self.size = random.randint(1,9)
        self.surface = pygame.Surface((self.size,self.size))  # create a 3x3 surface
        self.surface.fill((255, 255, 255))     # fill it white (very important!)
        self.reset()

    def reset(self):
        self.x = random.randint(0, self.screen.get_width())
        self.y = random.randint(-600, 0)
        self.speed = random.uniform(1, 3)
        self.rect = self.surface.get_rect(topleft=(self.x, self.y))

    def update(self):
        self.y += self.speed
        self.rect.topleft = (self.x, self.y)
        if self.y > self.screen.get_height():
            self.reset()

    def draw(self):
        self.screen.blit(self.surface, self.rect)

    def freeze(self):
        self.speed = 0