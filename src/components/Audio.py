import pygame as pg
import src.state as state

class Audio:

    def __init__(self, path, audio_type='sound_fx'):
        self.__type = audio_type # (music, sound_fx)
        self.__audio = pg.mixer.Sound(path)
        self.__temp_enable = False
        self.watch_setting()

    def set_volume(self, volume=0.5):
        if self.__type == 'sound_fx':
            if not state.SOUND_FX: volume = 0 
        elif self.__type == 'music': 
            if not state.MUSIC: volume = 0
        self.__audio.set_volume(volume)

    def watch_setting(self):
        volume = 0
        if self.__type == 'sound_fx' and self.__temp_enable != state.SOUND_FX:
            if state.SOUND_FX: volume = 0.5
            self.set_volume(volume)
            self.__temp_enable = state.SOUND_FX
            print('change volume sound fx')
        elif self.__type == 'music' and self.__temp_enable != state.MUSIC:
            if state.MUSIC: volume = 0.5
            self.set_volume(volume)
            self.__temp_enable = state.MUSIC
            print('change volume music')

    def play(self, loops=False):
        self.set_volume()
        self.__audio.play(loops)
        
    def stop(self):
        self.__audio.stop()
        