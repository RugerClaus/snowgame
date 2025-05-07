import pygame
import random

class Powerup:
    def __init__(self, screen,powerup_type):
        self.screen = screen
        self.colors = [(0,255,0),(255,0,0),(0,0,255)]
        self.type = powerup_type
        self.reset()
        
    
    def reset(self):
        if self.type == "anti_shrink":
            self.size = 7
            self.x = random.randint(0, self.screen.get_width() - self.size)
            self.y = random.randint(-600, -self.size)
            self.speed = 4
            self.surface = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
            self.surface.fill(self.colors[0])
            self.rect = self.surface.get_rect(topleft=(self.x, self.y))
        elif self.type == "grow_small":
            self.size = 3
            self.x = random.randint(0, self.screen.get_width() - self.size)
            self.y = random.randint(-600, -self.size)
            self.speed = 8
            self.surface = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
            self.surface.fill(self.colors[1])
            self.rect = self.surface.get_rect(topleft=(self.x, self.y))
        elif self.type == "absorb_rock":
            self.size = 15
            self.x = random.randint(0,self.screen.get_width()- self.size)
            self.y = random.randint(-600, -self.size)
            self.speed = 5
            self.surface = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
            self.surface.fill(self.colors[2])
            self.rect = self.surface.get_rect(topleft=(self.x,self.y))

    def update(self):
        self.y += self.speed
        self.rect.topleft = (self.x, self.y)
        if self.y > self.screen.get_height():
            self.reset()

    def draw(self):
        self.screen.blit(self.surface, self.rect)

    def freeze(self):
        self.speed = 0
