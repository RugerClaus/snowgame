import pygame
from ui.font import FontEngine

class PlayerUI:
    def __init__(self, screen, player, start_time, level_up_size=100):
        self.screen = screen
        self.surface = pygame.surface.Surface((screen.get_width(), screen.get_height()), pygame.SRCALPHA)
        self.rect = self.surface.get_rect()
        self.player = player
        self.start_time = start_time
        self.font = FontEngine("UI").font

    def draw(self):
        self.surface.fill((0, 0, 0, 0))  

        
        self.draw_size_bar("bottom")

        
        elapsed_ms = pygame.time.get_ticks() - self.start_time
        seconds = (elapsed_ms // 1000) % 60
        minutes = (elapsed_ms // 60000)
        time_text = f"Time: {minutes:02}:{seconds:02}"
        time_surface = self.font.render(time_text, True, (255, 255, 255))
        self.surface.blit(time_surface, (10, 10))

        
        size_text = f"Size: {int(self.player.size)}"
        size_surface = self.font.render(size_text, True, (255, 255, 255))
        self.surface.blit(size_surface, (10, 40))


        level_text = f"Level: {self.player.current_level -1}"
        level_surface = self.font.render(level_text, True, (255, 255, 255))
        self.surface.blit(level_surface, (10, 70))

        snow_fall_threshold_text = f"Snow Fall Threshold: {self.player.snow_fall_threshold}"
        snow_fall_threshold_surface = self.font.render(snow_fall_threshold_text,True,(255,255,255))
        self.surface.blit(snow_fall_threshold_surface,(10,100))

        size_level_up_text = f"Size to level up: {self.player.level_up_size}"
        size_level_up_surface = self.font.render(size_level_up_text,True,(255,255,255))
        self.surface.blit(size_level_up_surface,(10,130))

        score_text = f"Score: {self.player.score}"
        score_surface = self.font.render(score_text,True,(255,255,255))
        self.surface.blit(score_surface,(self.screen.get_width() - 200,10))

        self.screen.blit(self.surface, self.rect)

    # added location variable to the size bar drawing method
    # this is so that eventually the player can actually change the position of it. I'm thinking this will be more general for the UI library
    # this file is getting really really extensible.
    # this will currently allow me to either choose when the function is called in the draw method, or implement a player's interaction
    # I need to make a pause menu first :)

    def draw_size_bar(self,location):

        if location == "bottom":
            bar_width, bar_height = self.screen.get_width() // 2, 20
            size_avg = (self.player.width + self.player.height) / 2
            progress = min(size_avg / self.player.level_up_size, 1.0)
            fill_width = bar_width * progress

            outline_rect = pygame.Rect(self.screen.get_width() // 4, self.screen.get_height() - 50, bar_width, bar_height)
            fill_rect = pygame.Rect(
                outline_rect.left + 2,       
                outline_rect.top + 2,        
                fill_width - 4,              
                bar_height - 4               
            )

            fill_color = (
                int(255 * (1 - progress)),
                int(255 * progress),
                0
            )
        elif location == "left":
            bar_width = 20
            bar_height = self.screen.get_height() // 2
            size_avg = (self.player.width + self.player.height) / 2
            progress = min(size_avg / self.player.level_up_size, 1.0)
            fill_height = bar_height * progress


            outline_rect = pygame.Rect(50, self.screen.get_height() - bar_height - 50, bar_width, bar_height)
            
            
            fill_rect = pygame.Rect(
                outline_rect.left + 2,
                outline_rect.bottom - fill_height + 2,  
                bar_width - 4,
                fill_height - 4 if fill_height >= 4 else 0  
            )

            fill_color = (
                int(255 * (1 - progress)),  # red to green
                int(255 * progress),
                0
            )


        pygame.draw.rect(self.surface, fill_color, fill_rect)
        pygame.draw.rect(self.surface, (255, 255, 255), outline_rect, 2)

    def draw_track_playing(self,sound): # sound should be the output of App.sound.current_track
        text = self.font.render(f"Now Playing: {sound}", True,(255,255,255))
        
        self.screen.blit(text,(10,160))

    def update(self):
        current_width, current_height = self.screen.get_size()
        if (self.surface.get_width(), self.surface.get_height()) != (current_width, current_height):
            self.surface = pygame.surface.Surface((current_width, current_height), pygame.SRCALPHA)
            self.rect = self.surface.get_rect()
