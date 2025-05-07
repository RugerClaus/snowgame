import pygame
import random

class Player:
    def __init__(self, screen):
        self.screen = screen
        self.reset()
        self.size = self.width
        self.powerup_duration = 5000
        self.powerup_start_time = 0
        self.powerup_type = ""
        
    def draw(self):
        
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
        
        if self.width >= 50:
            self.shrink_rate = 1
        elif self.width >= 40:
            self.shrink_rate = 0.5
        elif self.width >= 10:
            self.shrink_rate = 0.1
        else:
            self.shrink_rate = 0.01

        if self.powerup:
            current_time = pygame.time.get_ticks()
            if self.powerup_type == "anti_shrink":
                self.shrink_rate = 0
                self.surface.fill((0,255,22))
            elif self.powerup_type == "grow_small":
                self.shrink_rate = -0.02
                self.surface.fill((255,22,0))
            elif self.powerup_type == "absorb_rock":
                self.surface.fill((22,0,255))
                if current_time - self.powerup_start_time >= self.powerup_duration:
                    self.powerup = False

            if current_time - self.powerup_start_time >= self.powerup_duration:
                self.powerup = False

        if self.width <= 1:
            self.alive = False 
        self.width = max(1, self.width - self.shrink_rate)
        self.height = max(1, self.height - self.shrink_rate)

        self.size = self.width
        self.rect.bottom = self.screen.get_height() - 100

        if self.score >= 10000:
            self.powerup_duration = 6000
        elif self.score >= 20000:
            self.powerup_duration = 6500
        elif self.score >= 50000:
            self.powerup_duration = 6870
        elif self.score >= 100000:
            self.powerup_duration = 7500
        elif self.score >= 175000:
            self.powerup_duration = 8000


    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.centerx -= self.speed
        if keys[pygame.K_d]:
            self.rect.centerx += self.speed

    def reset(self):
        self.width = 10
        self.height = 10
        self.surface = pygame.surface.Surface((self.width, self.height))
        self.rect = self.surface.get_rect()
        self.surface.fill((255, 255, 255))
        self.rect.bottom = self.screen.get_height() - 100
        self.start = self.screen.get_width() // 2
        self.rect.centerx = self.start
        self.speed = 5
        self.alive = True

        self.current_level = 1
        self.level_up_size = self.calculate_level_up_size(self.current_level)
        self.snow_fall_threshold = self.calculate_snow_fall_threshold(self.current_level)
        self.score = 0
        self.powerup = False

    def check_level_up(self):
        if self.width >= self.level_up_size:
            self.current_level += 1
            self.level_up_size = self.calculate_level_up_size(self.current_level)
            self.snow_fall_threshold = self.calculate_snow_fall_threshold(self.current_level)

            self.width = 10
            self.height = 10
            self.powerup = False
            return True

        return False
            
    def randomize_snowfall_behavior(self):

        if random.random() < 0.1:
            self.snow_fall_threshold = max(100,self.snow_fall_threshold - random.randint(50,200))
    def calculate_level_up_size(self, level):
        return 10 + (level - 1) * 10  # e.g., level 1 = 10, level 2 = 20, etc.

    def calculate_snow_fall_threshold(self, level):
        return max(100, 600 - level * 50)