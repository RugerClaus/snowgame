import pygame

class SoundManager:
    def __init__(self, volume=0.5):
        pygame.mixer.init()
        self.music_tracks = {
            "game": "sounds/music.wav",
        }
        self.sound_effects = {

        }
        self.volume = volume
        self.music_active = True
        self.sfx_active = True

    def play_music(self, track_name, loop=True):
        if not self.music_active:
            return
        if track_name in self.music_tracks:
            if pygame.mixer.music.get_busy() and pygame.mixer.music.get_pos() > 0:
                return
            pygame.mixer.music.load(self.music_tracks[track_name])
            pygame.mixer.music.set_volume(self.volume)
            pygame.mixer.music.play(-1 if loop else 0)

    def stop_music(self):
        pygame.mixer.music.stop()
        self.current_track = None

    def toggle_music(self,state):

        if self.music_active:
            pygame.mixer.music.stop()
            print("Music off")
            self.current_track = None
        else:
            if state in self.music_tracks:
                pygame.mixer.music.load(self.music_tracks[state])
                pygame.mixer.music.set_volume(self.volume)
                pygame.mixer.music.play(-1)
                self.current_track = state
                print(f"Music on: {state}")

        self.music_active = not self.music_active

    def set_volume(self, volume):
        self.volume = max(0, min(volume, 1))
        pygame.mixer.music.set_volume(self.volume)

    def play_sfx(self, sfx_name):
        if self.sfx_active and sfx_name in self.sound_effects:
            print("playing sound")
            sfx = pygame.mixer.Sound(self.sound_effects[sfx_name])
            sfx.set_volume(self.volume)
            sfx.play()

    def stop_sfx(self):
        pygame.mixer.stop()


    def toggle_sfx(self):
        self.sfx_active = not self.sfx_active
        print(f"SFX {'On' if self.sfx_active else 'Off'}")

    
    def sfx_status(self):
        return "On" if self.sfx_active else "Off"

    def music_status(self):
        if self.music_active == True:
            return "On"
        else:
            return "Off"