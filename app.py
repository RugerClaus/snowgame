from entities.player import Player
from entities.snow import Snow
from entities.rocks import Rock
from ui.ui import PlayerUI
from ui.win import WinMenu
from ui.gameover import GameOverMenu
from ui.pause import PauseMenu
from entities.powerup import Powerup
from sound import SoundManager
from entities.collision import *

from menu import MainMenu

from state import APPSTATE
from statem import StateManager

import pygame
import random

pygame.init()
class App:
    
    def __init__(self,version):
    
        
        (self.width,self.height) = (1200,800)

        self.screen = pygame.display.set_mode((self.width,self.height),pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        self.title = pygame.display.set_caption(f"Snow Blitz - v{version}")

        self.main_menu = MainMenu(self.screen,self.play,pygame.quit)

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
        self.game_over = GameOverMenu(self.screen,self.restart,self.go_to_menu,pygame.quit)
        self.win = WinMenu(self.screen,self.restart,pygame.quit)

        self.pause_menu = PauseMenu(self.screen,self.pause_state_toggle,self.go_to_menu,pygame.quit)

        self.state = StateManager()

    def restart(self):
        self.sound.stop_music()
        self.player.reset()
        self.snow_flakes = []
        self.rocks = []
        start_time = pygame.time.get_ticks()
        self.ui = PlayerUI(self.screen,self.player,start_time)
        self.win_music_played = False
        self.state.set_app_state(APPSTATE.PLAYING)
    
    def pause_state_toggle(self):
        if self.state.is_app_state(APPSTATE.PAUSED):
            self.state.set_app_state(APPSTATE.PLAYING)
            self.sound.set_volume(0.5)
        else:
            self.state.set_app_state(APPSTATE.PAUSED)
            self.sound.set_volume(0.2)
        
    def play(self):
        if not self.state.is_app_state(APPSTATE.PLAYING):
            self.state.set_app_state(APPSTATE.PLAYING)
            self.restart()
            self.sound.play_music("game")
    
    def go_to_menu(self):
        self.state.set_app_state(APPSTATE.MAIN_MENU)
        print("going to menu")
        self.sound.stop_music()
    

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.sound.stop_music()
                self.state.set_app_state(APPSTATE.QUIT_APP)
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
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F7:
                    self.player.size -= 5
            self.pause_menu.handle_event(event)
            self.game_over.handle_event(event)
            self.win.handle_event(event)
            self.main_menu.handle_event(event)

    def main(self):
        self.state.set_app_state(APPSTATE.MAIN_MENU)

        while True:
            
            current_time = pygame.time.get_ticks()

            self.handle_events()
            if self.state.is_app_state(APPSTATE.PLAYING):
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
                        if self.player.current_level > 5:
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
                            
                    self.ui.update()
                    self.ui.draw()
                    if not self.player.alive:
                        self.state.set_app_state(APPSTATE.GAME_OVER)
                    if self.player.hasWon:
                        self.sound.stop_music()
                        self.state.set_app_state(APPSTATE.WON)

            elif self.state.is_app_state(APPSTATE.PAUSED):
                self.pause_menu.update()
                self.pause_menu.draw()
                
            elif self.state.is_app_state(APPSTATE.GAME_OVER):
                self.sound.stop_music()
                self.game_over.update()
                self.game_over.draw()

            elif self.state.is_app_state(APPSTATE.WON):
                self.sound.play_music("win")
                self.win.update()
                self.win.draw()
                
            
            elif self.state.is_app_state(APPSTATE.MAIN_MENU):
                self.main_menu.update()
                self.main_menu.draw()
                

            pygame.display.flip()
            self.clock.tick(60)
            print(f"Current AppState: {self.state.get_app_state()}")
            


