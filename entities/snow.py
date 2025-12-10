import pygame
import random

class Snow:
    def __init__(self, screen,app):
        self.app = app
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
        self.scale()

    
    def scale(self):
        BASE_WIDTH = self.app.width
        BASE_HEIGHT = self.app.height

        current_screen_width,current_screen_height = self.screen.get_size()
        width_scale_factor = current_screen_width / BASE_WIDTH
        height_scale_factor = current_screen_height / BASE_HEIGHT

        original_snow_width = self.size
        scaled_snow_width = int(original_snow_width * width_scale_factor)
        self.width = scaled_snow_width

        original_snow_height = self.size
        scaled_snow_height = int(original_snow_height * height_scale_factor)
        self.height = scaled_snow_height
        

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