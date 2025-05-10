import pygame

class FontEngine():
    def __init__(self,type):
        pygame.font.init()
        self.type = type
        self.font = None
        if self.type == "button":
            self.button_font()
        elif self.type == "UI":
            self.ui_font()
        elif self.type == "GameOver":
            self.game_over_font()
        elif self.type == "back":
            self.go_back_font()
        elif self.type == "tutorial":
            self.tutorial_font()
        elif self.type == "reducer":
            self.reducer_font()
        else:
            self.default_font()

    def button_font(self):
        self.font = pygame.font.Font('font/Pixeltype.ttf', 50)
        
    def ui_font(self):
        self.font = pygame.font.SysFont('Arial', 18)
    def game_over_font(self):
        self.font = pygame.font.Font('font/Pixeltype.ttf', 120)
    
    def go_back_font(self):
        self.font = pygame.font.Font("font/Pixeltype.ttf", 60)

    def tutorial_font(self):
        self.font = pygame.font.Font("font/Pixeltype.ttf", 60)

    def reducer_font(self):
        self.font = pygame.font.Font("font/Pixeltype.ttf", 40)

    def default_font(self):
        self.font = pygame.font.Font('font/Pixeltype.ttf', 25)