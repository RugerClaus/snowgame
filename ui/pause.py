import pygame
from ui.button import Button
from ui.font import FontEngine

class PauseMenu:
    def __init__(self, screen, resume_callback, restart_callback, go_to_menu_callback, quit_callback):
        self.screen = screen
        self.resume_callback = resume_callback
        self.restart_callback = restart_callback
        # self.music_toggle_callback = music_toggle_callback
        # self.sfx_toggle_callback = sfx_toggle_callback
        self.go_to_menu_callback = go_to_menu_callback
        # self.save_callback = save_callback
        self.quit_callback = quit_callback

        self.font = FontEngine(None).font
        self.buttons = []
        self.create_buttons()

    def create_buttons(self):
        width = 175
        height = 40
        spacing = 60
        screen_w = self.screen.get_width()
        screen_h = self.screen.get_height()
        center_x = screen_w // 4 + screen_w // 2
        start_y = screen_h // 2 - (spacing * 3)

        self.buttons = [
            Button("Resume", center_x, start_y + spacing * 0, width, height, (50, 100, 200), (255, 255, 255), self.resume_callback),
            Button("Restart", center_x, start_y + spacing * 1.25, width, height, (50, 100, 200), (255, 255, 255), self.restart_callback),
            Button("Main Menu", center_x, start_y + spacing * 2.5, width, height, (50, 100, 200), (255, 255, 255), self.go_to_menu_callback),
            Button("Exit", center_x, start_y + spacing * 5, width, height, (200, 50, 50), (255, 255, 255), self.quit_callback),
        ]

    def draw(self):
        mouse_pos = pygame.mouse.get_pos()
        for button in self.buttons:
            button.draw(self.screen, mouse_pos)

        text = self.font.render("PAUSED", True, (255, 255, 255))
        rect = text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
        self.screen.blit(text, rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            for button in self.buttons:
                button.is_clicked(mouse_pos, True)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.resume_callback()

        if event.type == pygame.QUIT:
            pygame.quit()

    def update(self):
        self.create_buttons()  
