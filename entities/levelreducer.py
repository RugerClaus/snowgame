import pygame
import random

from ui.font import FontEngine

class LevelReducer:
    def __init__(self, screen, level_reducer_type):
        self.screen = screen
        self.size = 40
        self.color = (200,200,0)  # yellow for visibility
        self.type = level_reducer_type
        self.font = FontEngine("reducer").font
        self.reset()

    def reset(self):
        if self.type == 'level_reducer_twenty':
            self.x = random.randint(0, self.screen.get_width() - self.size)
            self.y = random.randint(-800, -self.size)
            self.speed = 8
            self.surface = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
            self.surface.fill(self.color)
            self.rect = self.surface.get_rect(topleft=(self.x, self.y))
            text = self.font.render("20",True,(255,0,0))
            text_rect = text.get_rect(center=(self.size // 2, self.size // 2)) 
            self.surface.blit(text,text_rect)
        elif self.type == 'level_reducer_fifty':
            self.x = random.randint(0, self.screen.get_width() - self.size)
            self.y = random.randint(-800, -self.size)
            self.speed = 8
            self.surface = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
            self.surface.fill(self.color)
            self.rect = self.surface.get_rect(topleft=(self.x, self.y))
            text = self.font.render("50",True,(255,0,0))
            text_rect = text.get_rect(center=(self.size // 2, self.size // 2)) 
            self.surface.blit(text,text_rect)
        elif self.type == 'level_reducer_seventy':
            self.x = random.randint(0, self.screen.get_width() - self.size)
            self.y = random.randint(-800, -self.size)
            self.speed = 8
            self.surface = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
            self.surface.fill(self.color)
            self.rect = self.surface.get_rect(topleft=(self.x, self.y))
            text = self.font.render("70",True,(255,0,0))
            text_rect = text.get_rect(center=(self.size // 2, self.size // 2)) 
            self.surface.blit(text,text_rect)

    def update(self):
        self.y += self.speed
        self.rect.topleft = (self.x, self.y)
        if self.y > self.screen.get_height() - 100:
            self.reset()

    def draw(self):
        self.screen.blit(self.surface, self.rect)