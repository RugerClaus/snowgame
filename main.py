from player import Player
from snow import Snow
from rocks import Rock
from ui import PlayerUI
from sound import SoundManager
from collision import *
from gameover import GameOverMenu
import pygame
import random

pygame.init()

(width,height) = (1200,800)

screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

run = True
player = Player(screen)

snow_flakes = []
rocks = []
start_time = pygame.time.get_ticks()

last_spawn_time = pygame.time.get_ticks()
flake_spawn_interval = random.randint(0,2000)


last_rock_spawn_time = pygame.time.get_ticks()
rock_spawn_interval = random.randint(1000,4000)
ui = PlayerUI(screen,player,start_time)

sound = SoundManager()

def restart():
    global snow_flakes, rocks, start_time, ui
    player.reset()
    snow_flakes = []
    rocks = []
    start_time = pygame.time.get_ticks()
    ui = PlayerUI(screen,player,start_time)
    sound.play_music("game")
    
    


game_over = GameOverMenu(screen,restart,pygame.quit)

def draw_score(player_score):
    pass

def handle_events():
    global run
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            break
        game_over.handle_event(event)

while run:

    current_time = pygame.time.get_ticks()

    handle_events()

    if not player.alive:
        sound.stop_music()
        game_over.draw()
        
        pygame.display.flip()
        clock.tick(60)
        continue
    else:
        sound.play_music("game")
        if current_time - last_spawn_time > flake_spawn_interval and len(snow_flakes) < player.snow_fall_threshold:
            snow_flakes.append(Snow(screen))
            last_flake_spawn_time = current_time
            flake_spawn_interval = random.randint(random.randint(0,2000),random.randint(2000,4000))
        if current_time - last_rock_spawn_time > rock_spawn_interval and len(rocks) < 20:
            rocks.append(Rock(screen))
            last_rock_spawn_time = current_time
            rock_spawn_interval = random.randint(random.randint(1000,2000),random.randint(2000,6000))

        screen.fill((0,0,0))



        player.handle_input()
        
        player.update()
        player.draw()

        for snow_flake in snow_flakes:
            
            snow_flake.update()
            snow_flake.draw()
            if collide(player,snow_flake):
                player.width += 5
                player.height += 5
                snow_flake.reset()
        if player.check_level_up():
            snow_flakes = []
            rocks = []

        for rock in rocks:
            rock.update()
            rock.draw()
            if collide(player,rock):
                player.alive = False
                rock.reset()
        
        ui.draw()


    


    



    clock.tick(60)

    pygame.display.flip()

pygame.quit()

