import pygame
import random

class Powerup:
    def __init__(self, screen):
        self.screen = screen
        self.color = (0,255,0)
        self.reset()
    
    def reset(self):
        self.size = 15
        self.x = random.randint(0, self.screen.get_width() - self.size)
        self.y = random.randint(-600, -self.size)
        self.speed = 4
        self.surface = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        self.surface.fill(self.color)
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
