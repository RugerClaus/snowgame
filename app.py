from entities.player import Player

from ui.gameover import GameOverMenu
from ui.pause import PauseMenu
from ui.win import WinMenu
from sound import SoundManager


from menu import MainMenu
from mode import Mode

from FSM.state import APPSTATE,TUTORIALSTATE
from FSM.statem import StateManager

import pygame
import sys


class App:
    
    def __init__(self,version):
        pygame.init()
        
        (self.width,self.height) = (1200,800)

        self.screen = pygame.display.set_mode((self.width,self.height),pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        self.title = pygame.display.set_caption(f"Snow Blitz - v{version}")
        icon = pygame.image.load("images/icon.png")
        pygame.display.set_icon(icon)

        self.main_menu = MainMenu(self.screen,self.play_endless,self.play_tutorial,self.quit_game)
        self.player = Player(self.screen)

        self.sound = SoundManager()

        self.game_over = GameOverMenu(self.screen,self.restart,self.go_to_menu,self.quit_game)

        self.pause_menu = PauseMenu(self.screen,self.pause_state_toggle, self.restart,self.go_to_menu,self.quit_game)

        self.state = StateManager()
        self.win = WinMenu(self.screen,self.restart,self.go_to_menu,self.quit_game)
        self.mode = Mode(self.screen,self.player,self.state,self.win)
        

    def quit_game(self):
        self.state.set_app_state(APPSTATE.QUIT_APP)

    def restart(self):
        print("clicked restart somewhere")
        self.sound.stop_music()

        if self.state.previous_app_state == APPSTATE.TUTORIAL:
            self._init_tutorial()
        else:
            self.mode.snow_flakes = []
            self.mode.rocks = []
            self.mode.start_time = pygame.time.get_ticks()
            self.player = Player(self.screen)
            self.player.current_level = 1
            self.mode = Mode(self.screen, self.player, self.state,self.win)
            self.state.set_app_state(self.state.previous_app_state)
            self.sound.force_play_music()
        pygame.display.flip()
    
    def pause_state_toggle(self):
        if self.state.is_app_state(APPSTATE.PAUSED):
            self.state.set_app_state(self.state.previous_app_state)
            self.sound.set_volume(0.5)
        else:
            self.state.set_app_state(APPSTATE.PAUSED)
            self.sound.set_volume(0.5)
        

    # HANDLE ENDLESS MODE

    def _init_endless(self):
        self.sound.stop_music()
        
        self.mode.snow_flakes = []
        self.mode.rocks = []
        self.mode.power_ups = []
        self.mode.start_time = pygame.time.get_ticks()
        self.player = Player(self.screen)
        self.player.current_level = 1
        self.mode = Mode(self.screen,self.player,self.state,self.win)
        self.state.set_app_state(APPSTATE.ENDLESS)
        self.sound.force_play_music()

    def play_endless(self):
        if not self.state.is_app_state(APPSTATE.ENDLESS):
            self.state.set_app_state(APPSTATE.ENDLESS)
            self._init_endless()
            self.sound.set_volume(0.5)
            self.sound.force_play_music()
    
    # END HANDLE ENDLESS MODE

    # HANDLE TUTORIAL MODE

    def _init_tutorial(self):
        self.mode.snow_flakes = []
        self.mode.rocks = []
        self.mode.start_time = pygame.time.get_ticks()
        self.player = Player(self.screen)
        self.player.alive = True
        self.player.current_level = 1
        self.mode = Mode(self.screen, self.player, self.state,self.win)

        self.state.set_tutorial_state(TUTORIALSTATE.RESET)
        self.state.set_app_state(APPSTATE.TUTORIAL)
        self.sound.force_play_music()

    def play_tutorial(self):
        if not self.state.is_app_state(APPSTATE.TUTORIAL):
            self.state.set_app_state(APPSTATE.TUTORIAL)
            self.state.set_previous_app_state(self.state.get_app_state())
            self._init_tutorial()
            self.sound.set_volume(0.5)
            self.sound.force_play_music()

    # END TUTORIAL MODE

    def go_to_menu(self):
        print("Going to menu")
        self.player.reset()
        if not self.state.is_tutorial_state(None):
            self.state.set_tutorial_state(None)

        self.sound.stop_music()
        self.sound.stop_sfx()
        self.restart()

        if pygame.display.get_init() == False:
            pygame.display.init()

        self.state.set_app_state(APPSTATE.MAIN_MENU)

        self.player = Player(self.screen)
        self.player.current_level = 1  # <-- Reset level here!

        self.main_menu = MainMenu(self.screen, self.play_endless, self.play_tutorial, self.quit_game)

        self.start_time = pygame.time.get_ticks()  # Optional: reset game timer

        self.screen.fill((0, 0, 0))
        self.main_menu.update()
        self.main_menu.draw()

        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.state.set_app_state(APPSTATE.QUIT_APP)

            elif event.type == pygame.VIDEORESIZE:
                width, height = event.size
                screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
                self.mode.ui.screen = screen
                self.player.screen = screen
                self.game_over.screen = screen
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F7:
                    print(f"current track: {self.sound.current_track}")
            
            self.pause_menu.handle_event(event)
            self.game_over.handle_event(event)
            self.main_menu.handle_event(event)
            self.sound.handle_event(event)


    def main(self):
        self.state.set_app_state(APPSTATE.MAIN_MENU)

        while self.state.get_app_state() != APPSTATE.QUIT_APP:
            
            current_time = pygame.time.get_ticks()

            self.handle_events()
            if self.state.is_app_state(APPSTATE.ENDLESS):

                self.mode.endless(current_time,self.sound)

            elif self.state.is_app_state(APPSTATE.TUTORIAL):

                self.mode.tutorial(current_time,self.sound)

            elif self.state.is_app_state(APPSTATE.WIN):
                self.sound.stop_music()
                self.sound.stop_sfx()
                self.win.update()
                self.win.draw()
                
                self.sound.play_sfx("win")
                
                pygame.display.flip()

            elif self.state.is_app_state(APPSTATE.PAUSED):
                self.pause_menu.update()
                self.pause_menu.draw()
                
                
            elif self.state.is_app_state(APPSTATE.GAME_OVER):
                self.sound.stop_music()
                self.sound.stop_sfx()
                self.game_over.update()
                self.game_over.draw()
            
            elif self.state.is_app_state(APPSTATE.MAIN_MENU): 
                self.sound.play_menu_music()
                self.main_menu.update()
                self.main_menu.draw()

            elif self.state.is_app_state(APPSTATE.QUIT_APP):
                pygame.quit() #no longer gets traceback now that this is only handled in the FSM
                sys.exit()
            pygame.display.flip()
            self.clock.tick(60)     
            # print(f"Current APPSTATE: {self.state.get_app_state()}")
            
        