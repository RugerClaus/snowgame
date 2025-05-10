import pygame
from ui.font import FontEngine

class Tutorial():
    def __init__(self,screen,player):
        self.screen = screen
        self.surface = pygame.surface.Surface((screen.get_width(), screen.get_height()), pygame.SRCALPHA)
        self.rect = self.surface.get_rect()
        self.player = player
        self.font = FontEngine("tutorial").font
        self.player_has_moved = False
        self.player_has_continued = False

    def display_movement_prompt(self):
        if not self.player_has_moved:
            prompt = self.font.render("Press A or D to move",True,(255,255,128))
            prompt_rect = prompt.get_rect(center=(self.screen.get_width()//2,self.screen.get_height()//2))
            self.screen.blit(prompt,prompt_rect)
            
    def display_snow_instructions(self):
        if not self.player_has_continued:
            prompt = self.font.render("Collide with snowflakes to grow \n \n Fill the size bar to level up \n \n \n PRESS SPACE TO CONTINUE",True,(255,255,128))
            prompt_rect = prompt.get_rect(center=(self.screen.get_width()//2,self.screen.get_height()//2))
            self.screen.blit(prompt,prompt_rect)
    
    def display_rock_instructions(self):
        if not self.player_has_continued:
            prompt = self.font.render("Rocks are dangerous and can kill the player \n \n Move left and right to avoid them \n \n \n PRESS SPACE TO CONTINUE",True,(255,255,128))
            prompt_rect = prompt.get_rect(center=(self.screen.get_width()//2,self.screen.get_height()//2))
            self.screen.blit(prompt,prompt_rect)

    def display_powerup_instructions(self):
        if not self.player_has_continued:
            prompt = self.font.render("Powerups are brightly colored \n \n Blue ones let you absorb the rock - Level Start: 5 \n \n Green ones stop you from shrinking - Level Start: 10 \n \n Red ones cause you to grow - Level Start: 20 \n \n \n PRESS SPACE TO CONTINUE",True,(255,255,128))
            prompt_rect = prompt.get_rect(center=(self.screen.get_width()//2,self.screen.get_height()//2))
            self.screen.blit(prompt,prompt_rect)

    def display_level_reducer_instructions(self):
        if not self.player_has_continued:
            prompt = self.font.render("Level Reducers start at level 15 \n \n They lower the size threshold to level \n up based on the number on the item\n \n This will help in later levels so \n you don't grow bigger than the screen \n \n Press SPACE to continue",True,(255,255,128))
            prompt_rect = prompt.get_rect(center=(self.screen.get_width()//2,self.screen.get_height()//2))
            self.screen.blit(prompt,prompt_rect)

    def display_end_screen(self):
        if not self.player_has_continued:
            prompt = self.font.render("Tutorial Complete! \n Good Job! \n \n Press SPACE to go to the main menu",True,(255,255,128))
            prompt_rect = prompt.get_rect(center=(self.screen.get_width()//2,self.screen.get_height()//2))
            self.screen.blit(prompt,prompt_rect)

    def handle_start(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_d]:
            self.player_has_moved = True

    def handle_continue(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.player_has_continued = True