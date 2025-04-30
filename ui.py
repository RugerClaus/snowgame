import pygame
import math

class PlayerUI:
    def __init__(self, screen, player, start_time, level_up_size=100):
        self.screen = screen
        self.surface = pygame.surface.Surface((screen.get_width(), screen.get_height()), pygame.SRCALPHA)
        self.rect = self.surface.get_rect()
        self.player = player
        self.start_time = start_time
        self.font = pygame.font.SysFont("Arial", 18)

    def draw(self):
        self.surface.fill((0, 0, 0, 0))  # transparent clear

        # Draw size progress bar
        self.draw_size_bar()

        # Draw timer
        elapsed_ms = pygame.time.get_ticks() - self.start_time
        seconds = (elapsed_ms // 1000) % 60
        minutes = (elapsed_ms // 60000)
        time_text = f"Time: {minutes:02}:{seconds:02}"
        time_surface = self.font.render(time_text, True, (255, 255, 255))
        self.surface.blit(time_surface, (10, 10))

        # Draw current size
        size_text = f"Size: {int(self.player.size)}"
        size_surface = self.font.render(size_text, True, (255, 255, 255))
        self.surface.blit(size_surface, (10, 40))

        # Draw current level
        level_text = f"Level: {self.player.current_level}"
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
        self.surface.blit(score_surface,(1000,10))

        self.screen.blit(self.surface, self.rect)

    def draw_size_bar(self):
        bar_width, bar_height = 25, 150
        size_avg = (self.player.width + self.player.height) / 2
        progress = min(size_avg / self.player.level_up_size, 1.0)
        fill_height = bar_height * progress

        outline_rect = pygame.Rect(10, 190, bar_width, bar_height)
        fill_rect = pygame.Rect(
            10,
            190 + (bar_height - fill_height),
            bar_width,
            fill_height
        )

        fill_color = (
            int(255 * (1 - progress)),  # red to green
            int(255 * progress),
            0
        )

        pygame.draw.rect(self.surface, fill_color, fill_rect)
        pygame.draw.rect(self.surface, (255, 255, 255), outline_rect, 2)


