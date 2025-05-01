import pygame
import random

class Rock:
    def __init__(self, screen):
        self.screen = screen
        self.y = -50
        self.width = random.randint(30,50)
        self.height = random.randint(30,50)
        self.surface = pygame.Surface((self.width, self.height))  # create a 3x3 surface
        colors = [
            (112, 128, 144),  # Slate Gray
            (169, 169, 169),  # Dark Gray
            (105, 105, 105),  # Dim Gray
            (128, 128, 128),  # Classic Gray
            (192, 192, 192),  # Light Gray
            (101, 67, 33),    # Brown (earthy rock)
            (87, 85, 83),     # Granite
            (70, 70, 70),     # Charcoal
            (115, 105, 92),   # Weathered limestone
            (143, 129, 118),  # Sandstone
            (88, 80, 68),     # Basalt
            (108, 122, 137),  # Cool-toned shale
            (135, 115, 90),   # Desert rock
        ]
        self.surface.fill((255,0,0))     # fill it white (very important!)
        self.reset()

    def reset(self):
        self.x = random.randint(0, self.screen.get_width())
        self.y = random.randint(-600, 0)
        self.speed = 5
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