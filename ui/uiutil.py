import pygame
from ui.font import FontEngine

class UIUTIL():
    def __init__(self,screen):
        self.screen = screen
        self.surface = pygame.surface.Surface((screen.get_width(), screen.get_height()), pygame.SRCALPHA)
        self.rect = self.surface.get_rect()
        self.font = FontEngine("tutorial").font
        self.player_has_moved = False
        self.player_has_continued = False

    def INCOMPLETE(self):
        text = self.font.render("This is under construction. \n Press ESC to PAUSE and return to MAIN MENU",True,(255,255,255))
        text_rect = text.get_rect(center = (self.screen.get_width() // 2, self.screen.get_height() // 2))
        self.screen.blit(text,text_rect)