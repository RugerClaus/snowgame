import pygame
import random

from entities.collision import *
from entities.snow import Snow
from entities.rocks import Rock
from entities.powerup import Powerup
from ui.ui import PlayerUI

from state import APPSTATE

class Mode:
    def __init__(self,screen,player,state):
        self.screen = screen
        self.player = player
        self.state = state

        self.start_time = pygame.time.get_ticks()

        self.ui = PlayerUI(self.screen,self.player,self.start_time)

        self.last_flake_spawn_time = pygame.time.get_ticks()
        self.flake_spawn_interval = random.randint(0,2000)

        self.last_power_up_start_time = pygame.time.get_ticks()
        self.power_up_spawn_interval = random.randint(0,4000)

        self.last_rock_stop_time = pygame.time.get_ticks()
        self.rock_spawn_interval = random.randint(1000,4000)

        self.snow_flakes = []
        self.rocks = []
        self.power_ups = []

    def reset_entities(self):
        self.snow_flakes = []
        self.rocks = []
        self.power_ups = []


    def endless(self,current_time,sound):
        

        if current_time - self.last_flake_spawn_time > self.flake_spawn_interval and len(self.snow_flakes) < self.player.snow_fall_threshold:
            self.snow_flakes.append(Snow(self.screen))
            self.last_flake_spawn_time = current_time
            self.flake_spawn_interval = random.randint(0,200)

        if current_time - self.last_rock_stop_time > self.rock_spawn_interval and len(self.rocks) < 30 and self.player.current_level >= 3:
            self.rocks.append(Rock(self.screen))
            self.last_rock_stop_time = current_time
            self.rock_spawn_interval = random.randint(2000,6000)
        elif self.player.current_level < 3:
            self.rocks = []

        if current_time - self.last_power_up_start_time > self.power_up_spawn_interval and len(self.power_ups) < 15 and self.player.current_level >= 5:
            if self.player.current_level >= 20:
                powerup_type = random.choice(["absorb_rock","anti_shrink","grow_small"])
            elif self.player.current_level >= 10:
                powerup_type = random.choice(["absorb_rock", "anti_shrink"])
            elif self.player.current_level < 10:
                powerup_type = random.choice(["absorb_rock"])

            self.power_ups.append(Powerup(self.screen, powerup_type=powerup_type))
            self.last_power_up_start_time = current_time
            self.power_up_spawn_interval = random.randint(4000, 10000)
        elif self.player.current_level < 5:
            self.power_ups = []
                
        self.screen.fill((0,0,0))



        self.player.handle_input()
        
        self.player.update()
        self.player.draw()
        if self.player.powerup:
            sound.play_sfx("powerup_active")
        else:
            sound.stop_sfx()

        for snow_flake in self.snow_flakes:
            
            snow_flake.update(self.player.current_level)
            snow_flake.draw()
            if collide(self.player,snow_flake):
                sound.play_sfx("pickup_snow")
                self.player.width += snow_flake.rect.width
                self.player.height += snow_flake.rect.width
                self.player.score += snow_flake.rect.width * 10
                snow_flake.reset()

        if self.player.check_level_up():
            print("clearing screen...")
            self.reset_entities()

        for rock in self.rocks:
            rock.update()
            rock.draw()
            if collide(self.player,rock):
                if self.player.powerup and self.player.powerup_type == "absorb_rock":
                    self.player.width += rock.rect.width
                    self.player.height += rock.rect.width
                    self.player.score += rock.rect.width * 20
                    
                    if self.player.check_level_up():
                        self.reset_entities()
                else:
                    self.player.alive = False
                rock.reset()
        
        for power_up in self.power_ups:
            power_up.update()
            power_up.draw()
            if collide(self.player,power_up):
                
                self.player.powerup = True
                self.player.powerup_type = power_up.type
                self.player.powerup_start_time = pygame.time.get_ticks()
                power_up.reset()
                
        self.ui.update()
        self.ui.draw()
        self.ui.draw_track_playing(sound.current_track)

        if not self.player.alive:
            self.state.set_app_state(APPSTATE.GAME_OVER)