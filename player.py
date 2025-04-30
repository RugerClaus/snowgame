import pygame
import math

class Player:
    def __init__(self, screen):
        self.screen = screen
        self.levels = [
            20,
            30,
            40,
            50,
            60,
            70,
            80,
            90,
            100,
            110,
            120,
            130,
            140,
            150,
            160,
            170,
            180,
            190,
            200
        ]
        self.snow_fall_thresholds = [
            1000,
            950,
            900,
            850,
            800,
            750,
            700,
            650,
            600,
            550,
            500,
            450,
            400,
            350,
            300,
            250,
            200,
            150,
            100
        ]
        self.reset()
        self.size = self.width
        
    def draw(self):
        
        # Draw the rotated image at the player's center position
        self.screen.blit(self.surface, self.rect)

    def update(self):

        self.check_level_up()

        old_centerx = self.rect.centerx
        old_bottom = self.rect.bottom

        self.surface = pygame.surface.Surface((int(self.width), int(self.height)))
        self.surface.fill((255, 255, 255))
        self.rect = self.surface.get_rect()

        self.rect.centerx = old_centerx
        self.rect.bottom = old_bottom

        if self.width > 200 and self.height > 200:
            shrink_rate = 50
        elif self.width > 150 and self.height > 150:
            shrink_rate = 10
        elif self.width > 100 and self.height > 100:
            shrink_rate = 5
        elif self.width > 50 and self.height > 50:
            shrink_rate = 1
        elif self.width > 40 and self.height > 40:
            shrink_rate = 0.5
        elif self.width > 10 and self.height > 10:
            shrink_rate = 0.1
        else:
            shrink_rate = 0.01

        if self.width <= 1 and self.height <= 1:
            self.alive = False 
        self.width = max(1, self.width - shrink_rate)
        self.height = max(1, self.height - shrink_rate)

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:  # Move left and rotate left
            self.rect.centerx -= self.speed
        if keys[pygame.K_d]:  # Move right and rotate right
            self.rect.centerx += self.speed

    def reset(self):
        self.width = 10
        self.height = 10
        self.surface = pygame.surface.Surface((self.width,self.height))
        self.rect = self.surface.get_rect()
        self.surface.fill((255,255,255))
        self.rect.bottom = self.screen.get_height() - 100
        self.start = self.screen.get_width() // 2
        self.rect.centerx = self.start
        self.speed = 5
        self.alive = True
        self.level_up_size = self.levels[0]
        self.snow_fall_threshold = self.snow_fall_thresholds[0]
        self.current_level = 1


    def check_level_up(self):

        if self.current_level > len(self.levels):
            return False

        if self.width >= self.level_up_size:
            self.current_level += 1
            if self.current_level <= self.levels[self.current_level - 1] and self.current_level <= self.snow_fall_thresholds[self.current_level -1]:
                self.width = 10
                self.height = 10
                self.level_up_size = self.levels[self.current_level - 1]
                self.snow_fall_threshold = self.snow_fall_thresholds[self.current_level - 1]
            print(self.current_level)                
            return True
        return False