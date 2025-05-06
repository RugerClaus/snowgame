import pygame
from ui.button import Button
from ui.font import FontEngine

class GameOverMenu:
    def __init__(self,screen, restart_callback, main_menu_callback, quit_callback):
        self.screen = screen
        self.buttons = []
        self.restart_callback = restart_callback
        self.main_menu_callback = main_menu_callback
        self.quit_callback = quit_callback
        self.font = FontEngine("GameOver").font

        self.create_buttons()

    def create_buttons(self):
        self.buttons = [
            Button("Restart", self.screen.get_width() / 4, self.screen.get_height() // 2, 175, 40, (200, 50, 50), (255, 255, 255), self.restart_callback),
            Button("Main Menu",self.screen.get_width() / 2, self.screen.get_height() // 2+100, 175, 40, (200,50,50),(255,255,255),self.main_menu_callback),
            Button("Exit", self.screen.get_width() / 2 + self.screen.get_width() / 4, self.screen.get_height() // 2, 175, 40, (200, 50, 50), (255, 255, 255), self.quit_callback),
        ]

    def draw(self):
        mouse_pos = pygame.mouse.get_pos()
        for button in self.buttons:
            button.draw(self.screen, mouse_pos)

        text = self.font.render("GAME OVER", True, (255,0,0))
        rect = text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() - 700))
        self.screen.blit(text, rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            for button in self.buttons:
                button.is_clicked(mouse_pos, True)
        if event.type == pygame.QUIT:
            pygame.quit()

    def update(self):
        self.create_buttons()