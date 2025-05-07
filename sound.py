import pygame
import random

class SoundManager:
    def __init__(self, volume=0.5):
        pygame.mixer.init()
        self.MUSIC_END_EVENT = pygame.USEREVENT + 1
        pygame.mixer.music.set_endevent(self.MUSIC_END_EVENT)

        self.music_tracks = {
            "Winter Waves": "sounds/music0.wav",
            "Isle Of Atmospheres": "sounds/music1.wav",
            "Wobble Doom": "sounds/music2.wav",
            "Millenia": "sounds/music3.wav",
            "Late Night Sezsh": "sounds/music4.wav",
            "Dances With Synths": "sounds/music5.wav",
            "Minty Awakening": "sounds/music6.wav",
        }
        self.sound_effects = {
            "win": "sounds/win.mp3",
            "pickup_snow": "sounds/snow.wav",
            "powerup_active": "sounds/powerup_active.wav"
        }
        self.volume = volume
        self.music_active = True
        self.sfx_active = True
        self.music_queue = list(self.music_tracks.keys())
        random.shuffle(self.music_queue)
        self.current_track = None

    def _play_next_track(self):
        if not self.music_active:
            return

        if not self.music_queue:
            
            tracks = list(self.music_tracks.keys())
            if self.current_track in tracks:
                tracks.remove(self.current_track)
            random.shuffle(tracks)
            self.music_queue = tracks

        next_track = self.music_queue.pop(0)
        pygame.mixer.music.load(self.music_tracks[next_track])
        pygame.mixer.music.set_volume(self.volume)
        pygame.mixer.music.play()  
        self.current_track = next_track
        print(f"Now playing: {next_track}")

    def handle_event(self, event):
        if event.type == self.MUSIC_END_EVENT and self.music_active:
            self.current_track = None
            self._play_next_track()

    def start_music(self):
        if not pygame.mixer.music.get_busy() and self.current_track is None:
            self._play_next_track()
    def stop_music(self):
        pygame.mixer.music.stop()
        self.current_track = None

    def toggle_music(self, state=None):
        if self.music_active:
            pygame.mixer.music.stop()
            print("Music off")
            self.current_track = None
        else:
            if state and state in self.music_tracks:
                pygame.mixer.music.load(self.music_tracks[state])
                pygame.mixer.music.set_volume(self.volume)
                pygame.mixer.music.play()  
                self.current_track = state
                print(f"Music on: {state}")
            else:
                self.start_music()
        self.music_active = not self.music_active

    def set_volume(self, volume):
        self.volume = max(0, min(volume, 1))
        pygame.mixer.music.set_volume(self.volume)

    def play_sfx(self, sfx_name):
        if self.sfx_active and sfx_name in self.sound_effects:
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
        return "On" if self.music_active else "Off"

    def force_play_music(self):
        self.stop_music()
        if self.music_tracks:
            track_name = random.choice(list(self.music_tracks.keys()))
            pygame.mixer.music.load(self.music_tracks[track_name])
            pygame.mixer.music.set_volume(self.volume)
            pygame.mixer.music.play()  
            self.current_track = track_name
            print(f"Forced play: {track_name}")
