import pygame
import random

class Powerup:
    def __init__(self, screen,app,powerup_type):
        self.app = app
        self.screen = screen
        self.colors = [(0,255,0),(255,0,0),(0,0,255)]
        self.type = powerup_type
        self.reset()
        
    def scale(self):
        BASE_WIDTH = self.app.width
        BASE_HEIGHT = self.app.height

        current_screen_width,current_screen_height = self.screen.get_size()
        width_scale_factor = current_screen_width / BASE_WIDTH
        height_scale_factor = current_screen_height / BASE_HEIGHT

        original_powerup_width = self.size
        scaled_powerup_width = int(original_powerup_width * width_scale_factor)
        self.width = scaled_powerup_width

        original_powerup_height = self.size
        scaled_powerup_height = int(original_powerup_height * height_scale_factor)
        self.height = scaled_powerup_height
    
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
