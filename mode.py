import pygame
import random

from entities.collision import *
from entities.snow import Snow
from entities.rocks import Rock
from entities.powerup import Powerup
from entities.levelreducer import LevelReducer
from ui.ui import PlayerUI
from ui.tutorial import Tutorial


from FSM.state import APPSTATE,TUTORIALSTATE


# I hate pygame and drawing things frame by frame, but frankly 
# it gives you a lot of control which you don't get with libraries like JavaFX
# not that JavaFX is for making games, but frankly, this isn't either in all honestly. 
# However, pygame.sprite.Sprite and pygame.mixer are fantastic tools.
# This game doesn't really use pygame.sprite.Sprite yet however and probably won't for a long time.

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

        self.last_rock_start_time = pygame.time.get_ticks()
        self.rock_spawn_interval = random.randint(1000,4000)

        self.last_level_reducer_start_time = pygame.time.get_ticks()
        self.level_reducer_spawn_interval = random.randint(7000,14000) # between 7 and 14 seconds

        self.snow_flakes = []
        self.rocks = []
        self.power_ups = []
        
        self.tutorialOBJ = Tutorial(self.screen,self.player)
        self.win_music_played = False

    def reset_entities(self):
        self.snow_flakes = []
        self.rocks = []
        self.power_ups = []
        self.level_reducers = []

        
    ### BEGIN ENDLESS GAME MODE ###

    def handle_snow_flakes(self,sound):
        for snow_flake in self.snow_flakes:
            snow_flake.update(self.player.current_level)
            snow_flake.draw()
            if collide(self.player,snow_flake):
                sound.play_sfx("pickup_snow")
                self.player.width += snow_flake.rect.width
                self.player.height += snow_flake.rect.width
                self.player.score += snow_flake.rect.width * 10
                snow_flake.reset()

    def handle_rocks(self):
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

    def handle_power_ups(self):

        for power_up in self.power_ups:
            power_up.update()
            power_up.draw()
            if collide(self.player,power_up):
                
                self.player.powerup = True
                self.player.powerup_type = power_up.type
                self.player.powerup_start_time = pygame.time.get_ticks()
                power_up.reset()

    def handle_level_reducers(self):
        for reducer in self.level_reducers:
            reducer.update()
            reducer.draw()
            if collide(self.player,reducer):
                self.player.reducer = True
                self.player.reducer_type = reducer.type
                self.player.reducer_start_time = pygame.time.get_ticks()
                reducer.reset()


    def endless(self,current_time,sound):
        
        # BEGIN NON-PLAYER ENTITY SPAWNING

        if current_time - self.last_flake_spawn_time > self.flake_spawn_interval and len(self.snow_flakes) < self.player.snow_fall_threshold:
            self.snow_flakes.append(Snow(self.screen))
            self.last_flake_spawn_time = current_time
            self.flake_spawn_interval = random.randint(0,200)

        if current_time - self.last_rock_start_time > self.rock_spawn_interval and len(self.rocks) < 30 and self.player.current_level >= 4:
            self.rocks.append(Rock(self.screen))
            self.last_rock_start_time = current_time
            self.rock_spawn_interval = random.randint(2000,6000)
        elif self.player.current_level < 4:
            self.rocks = []

        if current_time - self.last_power_up_start_time > self.power_up_spawn_interval and len(self.power_ups) < 8 and self.player.current_level >= 6:
            if self.player.current_level >= 21:
                powerup_type = random.choice(["absorb_rock","anti_shrink","grow_small"])
            elif self.player.current_level >= 11:
                powerup_type = random.choice(["absorb_rock", "anti_shrink"])
            elif self.player.current_level < 11:
                powerup_type = random.choice(["absorb_rock"])

            self.power_ups.append(Powerup(self.screen, powerup_type=powerup_type))
            self.last_power_up_start_time = current_time
            self.power_up_spawn_interval = random.randint(4000, 10000)
        elif self.player.current_level < 6:
            self.power_ups = []

        if current_time - self.last_level_reducer_start_time > self.level_reducer_spawn_interval and len(self.level_reducers) < 10 and self.player.current_level >= 6:
            if self.player.current_level >= 6:
                level_reducer_type = random.choice(["level_reducer_fifty"])
            
            self.level_reducers.append(LevelReducer(self.screen,level_reducer_type))
            self.last_level_reducer_start_time = current_time
            self.level_reducer_spawn_interval = random.randint(7000,14000)
        elif self.player.current_level < 6:
            self.level_reducers = []

        # END NON-PLAYER ENTITY SPAWNING

        # DRAW SCREEN BACKGROUND - WILL REPLACE LATER

        self.screen.fill((0,0,0))

        # WILL WANT TO DRAW A GROUND HERE.

        # SET UP PLAYER HANDLING

        self.player.handle_input()
        self.player.update()
        self.player.draw()
        if self.player.powerup:
            sound.play_sfx("powerup_active")
        else:
            sound.stop_sfx()

        if not self.player.alive:
            self.state.set_previous_app_state(self.state.get_app_state())
            self.state.set_app_state(APPSTATE.GAME_OVER)

        # HANDLE ENTITIES

        self.handle_snow_flakes(sound)

        self.handle_rocks()
        
        self.handle_power_ups()

        self.handle_level_reducers()
                
        if self.player.check_level_up(): # have to have this here to clear the entities at the right time. 
            print("clearing screen...") # This way the level clears after the collision logic
            self.reset_entities()

        # UPDATE UI: SIZE BAR, CURRENT MUSIC TRACK
        self.ui.update()
        self.ui.draw()
        self.ui.draw_track_playing(sound.current_track)

    ### END ENDLESS GAME MODE ###
    
    ### START TUTORIAL GAME MODE ###

    def prompt_player_start_tutorial(self):
        self.tutorialOBJ.display_movement_prompt()
        self.tutorialOBJ.handle_start()
        
        if self.tutorialOBJ.player_has_moved:
            self.state.set_tutorial_state(TUTORIALSTATE.BEGIN)

    def start_tutorial(self,current_time):
        self.player.handle_input()
        self.player.update()
        self.ui.update()
        self.ui.draw()
        if current_time - self.last_flake_spawn_time > self.flake_spawn_interval and len(self.snow_flakes) < self.player.snow_fall_threshold:
            self.snow_flakes.append(Snow(self.screen))
            self.last_flake_spawn_time = current_time
            self.flake_spawn_interval = random.randint(0,200)
        for snow_flake in self.snow_flakes:
            
            snow_flake.update(self.player.current_level)
            snow_flake.draw()

            if snow_flake.y >= self.screen.get_height() // 4:
                self.state.set_tutorial_state(TUTORIALSTATE.SNOW_PROMPT)

    def prompt_player_start_snow(self):
        self.tutorialOBJ.display_snow_instructions()
        self.tutorialOBJ.player_has_continued = False
        self.tutorialOBJ.handle_continue()
        if self.tutorialOBJ.player_has_continued:
            self.state.set_tutorial_state(TUTORIALSTATE.SNOW)

    def start_snow(self,current_time,sound):
        self.player.handle_input()
        self.player.update()
        self.ui.update()
        self.ui.draw()

        if current_time - self.last_flake_spawn_time > self.flake_spawn_interval and len(self.snow_flakes) < self.player.snow_fall_threshold:
            self.snow_flakes.append(Snow(self.screen))
            self.last_flake_spawn_time = current_time
            self.flake_spawn_interval = random.randint(0,200)
        if current_time - self.last_rock_start_time > self.rock_spawn_interval and len(self.rocks) < 30 and self.player.current_level >= 4:
            self.rocks.append(Rock(self.screen))
            self.last_rock_start_time = current_time
            self.rock_spawn_interval = random.randint(2000,6000)
        elif self.player.current_level < 4:
            self.rocks = []

        self.handle_snow_flakes(sound)

        # no need to create another function for this, but I can't reuse the initial due to the state change

        for rock in self.rocks:
            rock.update()
            rock.draw()
            if collide(self.player,rock):
                self.state.set_previous_app_state(self.state.get_app_state())
                self.state.set_app_state(APPSTATE.GAME_OVER)
                self.player.alive = False
                rock.reset()
            
            if rock.y >= self.screen.get_height() // 2:
                self.state.set_tutorial_state(TUTORIALSTATE.ROCKS_PROMPT)      
    
        if self.player.check_level_up():
            print("clearing screen...")
            self.reset_entities()

    def prompt_player_start_rocks(self):
        self.tutorialOBJ.display_rock_instructions()
        self.tutorialOBJ.player_has_continued = False
        self.tutorialOBJ.handle_continue()
        if self.tutorialOBJ.player_has_continued:
            self.state.set_tutorial_state(TUTORIALSTATE.ROCKS)

    def start_rocks(self,current_time,sound):
        self.player.handle_input()
        self.player.update()
        self.ui.update()
        self.ui.draw()

        if current_time - self.last_flake_spawn_time > self.flake_spawn_interval and len(self.snow_flakes) < self.player.snow_fall_threshold:
            self.snow_flakes.append(Snow(self.screen))
            self.last_flake_spawn_time = current_time
            self.flake_spawn_interval = random.randint(0,200)
        if current_time - self.last_rock_start_time > self.rock_spawn_interval and len(self.rocks) < 30 and self.player.current_level >= 4:
            self.rocks.append(Rock(self.screen))
            self.last_rock_start_time = current_time
            self.rock_spawn_interval = random.randint(2000,6000)
        elif self.player.current_level < 4:
            self.rocks = []
        if current_time - self.last_power_up_start_time > self.power_up_spawn_interval and len(self.power_ups) < 15 and self.player.current_level >= 6:
            if self.player.current_level < 10:
                powerup_type = random.choice(["absorb_rock"])

            self.power_ups.append(Powerup(self.screen, powerup_type=powerup_type))
            self.last_power_up_start_time = current_time
            self.power_up_spawn_interval = random.randint(4000, 10000)
        elif self.player.current_level < 6:
            self.power_ups = []

        self.handle_snow_flakes(sound)

        self.handle_rocks()
        
        if self.player.check_level_up():
            print("clearing screen...")
            self.reset_entities()

        for power_up in self.power_ups:
            power_up.update()
            power_up.draw()
            
            if power_up.y >= self.screen.get_height() // 2:
                self.state.set_tutorial_state(TUTORIALSTATE.POWERUPS_PROMPT)

    def prompt_player_start_power_ups(self):
        self.tutorialOBJ.display_powerup_instructions()
        self.tutorialOBJ.player_has_continued = False
        self.tutorialOBJ.handle_continue()
        if self.tutorialOBJ.player_has_continued:
            self.state.set_tutorial_state(TUTORIALSTATE.POWERUPS)

    def start_power_ups(self,current_time,sound):
        self.player.handle_input()
        self.player.update()
        self.ui.update()
        self.ui.draw()
        if self.player.powerup:
            sound.play_sfx("powerup_active")
        else:
            sound.stop_sfx()
        if current_time - self.last_flake_spawn_time > self.flake_spawn_interval and len(self.snow_flakes) < self.player.snow_fall_threshold:
            self.snow_flakes.append(Snow(self.screen))
            self.last_flake_spawn_time = current_time
            self.flake_spawn_interval = random.randint(0,200)
        if current_time - self.last_rock_start_time > self.rock_spawn_interval and len(self.rocks) < 30 and self.player.current_level >= 4:
            self.rocks.append(Rock(self.screen))
            self.last_rock_start_time = current_time
            self.rock_spawn_interval = random.randint(2000,6000)
        elif self.player.current_level < 4:
            self.rocks = []
        if current_time - self.last_power_up_start_time > self.power_up_spawn_interval and len(self.power_ups) < 15 and self.player.current_level >= 6:
            if self.player.current_level >= 20:
                powerup_type = random.choice(["absorb_rock","anti_shrink","grow_small"])
            elif self.player.current_level >= 11:
                powerup_type = random.choice(["absorb_rock", "anti_shrink"])
            elif self.player.current_level < 11:
                powerup_type = random.choice(["absorb_rock"])

            self.power_ups.append(Powerup(self.screen, powerup_type=powerup_type))
            self.last_power_up_start_time = current_time
            self.power_up_spawn_interval = random.randint(4000, 10000)
        elif self.player.current_level < 6:
            self.power_ups = []

        self.handle_snow_flakes(sound)

        self.handle_rocks()

        self.handle_power_ups()
        
        if self.player.check_level_up():
            print("clearing screen...")
            self.reset_entities()

        if self.player.current_level > 21:
            self.state.set_tutorial_state(TUTORIALSTATE.WIN)

    def tutorial(self,current_time,sound):
        
        # if self.state.get_tutorial_state() is None:
        #     self.state.set_tutorial_state(TUTORIALSTATE.MOVEMENT_PROMPT)

        self.state.set_tutorial_state(TUTORIALSTATE.MOVEMENT_PROMPT)
        self.screen.fill((0,0,0))
        
        self.player.draw()
        self.ui.draw()
        for snow_flake in self.snow_flakes:
            snow_flake.draw()
        for rock in self.rocks:
            rock.draw()
        for powerup in self.power_ups:
            powerup.draw()
        
        if not self.player.alive:
            self.state.set_previous_app_state(self.state.get_app_state())
            self.state.set_app_state(APPSTATE.GAME_OVER)

        if self.state.is_tutorial_state(TUTORIALSTATE.MOVEMENT_PROMPT):
            
            self.prompt_player_start_tutorial()

        elif self.state.is_tutorial_state(TUTORIALSTATE.BEGIN):

            self.start_tutorial(current_time)    
        
        elif self.state.is_tutorial_state(TUTORIALSTATE.SNOW_PROMPT):

            self.prompt_player_start_snow()
        
        elif self.state.is_tutorial_state(TUTORIALSTATE.SNOW):
            
            self.start_snow(current_time,sound)

        elif self.state.is_tutorial_state(TUTORIALSTATE.ROCKS_PROMPT):
            self.prompt_player_start_rocks()

        elif self.state.is_tutorial_state(TUTORIALSTATE.ROCKS):

            self.start_rocks(current_time,sound)

        elif self.state.is_tutorial_state(TUTORIALSTATE.POWERUPS_PROMPT):

            self.prompt_player_start_power_ups()
        
        elif self.state.is_tutorial_state(TUTORIALSTATE.POWERUPS):
            
            self.start_power_ups(current_time,sound)

        elif self.state.is_tutorial_state(TUTORIALSTATE.WIN):
            self.player.reset()
            sound.stop_sfx()
            self.tutorialOBJ.display_end_screen()
            self.tutorialOBJ.player_has_continued = False
            self.tutorialOBJ.handle_continue()
            if self.tutorialOBJ.player_has_continued:
                self.state.set_app_state(APPSTATE.MAIN_MENU)

    ### END TUTORIAL GAME MODE ###