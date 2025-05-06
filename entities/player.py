import pygame
import math

class Player:
    def __init__(self, screen):
        self.screen = screen
        self.levels = [
            20,
            30,

        ]
        self.snow_fall_thresholds = [
            10000,
            9500,
            9000,
            8500,
            8000,
            7500,
            7000,
            6500,
            6000,
            5500,
            5000,
            4500,
            4000,
            3500,
            3000,
            2500,
            2000,
            1500,
            1000,
            750,
            500,
            250,
            50,
        ]
        self.reset()
        self.size = self.width
        self.powerup_duration = 5000
        self.powerup_start_time = 0
        
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

        if self.width > 50 and not self.powerup:
            self.shrink_rate = 1
        elif self.width > 40 and not self.powerup:
            self.shrink_rate = 0.5
        elif self.width > 10 and not self.powerup:
            self.shrink_rate = 0.1
        elif self.powerup:
            current_time = pygame.time.get_ticks()
            self.shrink_rate = 0
            self.surface.fill((0,255,22))
            if current_time - self.powerup_start_time >= self.powerup_duration:
                self.powerup = False
        else:
            self.shrink_rate = 0.01

        if self.width <= 1:
            self.alive = False 
        self.width = max(1, self.width - self.shrink_rate)
        self.height = max(1, self.height - self.shrink_rate)

        if self.current_level > len(self.levels) - 1:
            self.hasWon = True

        self.size = self.width
        self.rect.bottom = self.screen.get_height() - 100



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
        self.hasWon = False
        self.score = 0
        self.powerup = False


    def check_level_up(self):

        if self.current_level > len(self.levels):
            return False

        if self.width >= self.level_up_size:
            self.current_level += 1
            if self.current_level <= self.levels[self.current_level - 1] and self.current_level <= self.snow_fall_thresholds[self.current_level -1]:
                self.width = 10
                self.height = 10
                self.powerup = False
                self.level_up_size = self.levels[self.current_level - 1]
                self.snow_fall_threshold = self.snow_fall_thresholds[self.current_level - 1]
                            
            return True
        return False
    