from player import Player
from snow import Snow
from rocks import Rock
from ui.ui import PlayerUI
from ui.win import WinMenu
from powerup import Powerup
from sound import SoundManager
from collision import *
from ui.gameover import GameOverMenu
import pygame
import random

pygame.init()
class App:
    
    def __init__(self,version):
    
        
        (self.width,self.height) = (1200,800)

        self.screen = pygame.display.set_mode((self.width,self.height),pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        self.title = pygame.display.set_caption(f"Snow Blitz - v{version}")

        self.run = True
        self.player = Player(self.screen)

        self.snow_flakes = []
        self.rocks = []
        self.power_ups = []
        self.start_time = pygame.time.get_ticks()

        self.last_flake_spawn_time = pygame.time.get_ticks()
        self.flake_spawn_interval = random.randint(0,2000)


        self.last_rock_stop_time = pygame.time.get_ticks()
        self.rock_spawn_interval = random.randint(1000,4000)

        self.last_power_up_start_time = pygame.time.get_ticks()
        self.power_up_spawn_interval = random.randint(0,4000)

        self.ui = PlayerUI(self.screen,self.player,self.start_time)

        self.sound = SoundManager()

        self.win_music_played = False
        self.game_over = GameOverMenu(self.screen,self.restart,pygame.quit)
        self.win = WinMenu(self.screen,self.restart,pygame.quit)

    def restart(self):
        self.sound.stop_music()
        self.player.reset()
        self.snow_flakes = []
        self.rocks = []
        start_time = pygame.time.get_ticks()
        self.ui = PlayerUI(self.screen,self.player,start_time)
        self.win_music_played = False
        
        

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.sound.stop_music()
                pygame.quit()
                
                break

            elif event.type == pygame.VIDEORESIZE:
                width, height = event.size
                screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)

                self.ui.screen = screen
                self.player.screen = screen
                self.game_over.screen = screen
                self.win.screen = screen
                self.win.update()
            self.game_over.handle_event(event)
            self.win.handle_event(event)

    def main(self):

        while True:

            current_time = pygame.time.get_ticks()

            self.handle_events()

            if not self.player.alive:
                self.sound.stop_music()
                self.game_over.update()
                self.game_over.draw()
                
                pygame.display.flip()
                self.clock.tick(60)
                continue
            elif self.player.hasWon:
                if not self.win_music_played:
                    self.sound.stop_music()
                    self.sound.play_music("win", loop=False)
                    self.win_music_played = True

                self.win.draw()
                pygame.display.flip()
                self.clock.tick(60)
                continue
            else:
                self.sound.play_music("game")

                
                if current_time - self.last_flake_spawn_time > self.flake_spawn_interval and len(self.snow_flakes) < self.player.snow_fall_threshold:
                    self.snow_flakes.append(Snow(self.screen))
                    self.last_flake_spawn_time = current_time
                    self.flake_spawn_interval = random.randint(0,200)
                    if self.player.current_level > 3:
                        if current_time - self.last_rock_stop_time > self.rock_spawn_interval and len(self.rocks) < 30:
                            self.rocks.append(Rock(self.screen))
                            self.last_rock_stop_time = current_time
                            self.rock_spawn_interval = random.randint(2000,6000)
                    if self.player.current_level > 1:
                        if current_time - self.last_power_up_start_time > self.power_up_spawn_interval and len(self.power_ups) < 15:
                            self.power_ups.append(Powerup(self.screen))
                            self.last_power_up_start_time = current_time
                            self.power_up_spawn_interval = random.randint(4000,10000)

                self.screen.fill((0,0,0))



                self.player.handle_input()
                
                self.player.update()
                self.player.draw()

                for snow_flake in self.snow_flakes:
                    
                    snow_flake.update(self.player.current_level)
                    snow_flake.draw()
                    if collide(self.player,snow_flake):
                        self.player.width += snow_flake.rect.width
                        self.player.height += snow_flake.rect.width
                        self.player.score += snow_flake.rect.width * 10
                        snow_flake.reset()
                if self.player.check_level_up():
                    self.snow_flakes = []
                    self.rocks = []
                    self.power_ups = []

                for rock in self.rocks:
                    rock.update()
                    rock.draw()
                    if collide(self.player,rock):
                        self.player.alive = False
                        rock.reset()
                
                for power_up in self.power_ups:
                    power_up.update()
                    power_up.draw()
                    if collide(self.player,power_up):
                        
                        self.player.powerup = True
                        self.player.powerup_start_time = pygame.time.get_ticks()
                        power_up.reset()
                        
                
                self.ui.draw()

            self.clock.tick(60)

            pygame.display.flip()


