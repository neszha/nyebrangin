import pygame as pg
from src.config import *
from src.components.Audio import Audio

# Membangun sebuah karakter mobil.
class Car(pg.sprite.Sprite):
    
    def __init__(self, path, position, direction, speed):
        super().__init__()
        self.__direction = direction
        self.__speed = speed
        self.__horn_fx = Audio('assets/audios/effects/car-horn.mp3', 'sound_fx', 0.2)
        self.__is_horn = False
        self.__load_car(path, position)
    
    def __load_car(self, path, position):
        self.image = pg.image.load(path).convert_alpha()
        self.rect = self.image.get_rect(topleft=position)
        if self.__direction == 'right': self.image = pg.transform.flip(self.image, True, False)

    def update(self): 
        if self.__direction == 'left': 
            self.rect.x += self.__speed
            if self.rect.x >= WIDTH + 120: self.kill()
            if not self.__is_horn and self.rect.x > -100:
                self.__horn_fx.play()
                self.__is_horn = True

        if self.__direction == 'right':
            self.rect.x -= self.__speed
            if self.rect.x < -120: self.kill()
            if not self.__is_horn and self.rect.x < WIDTH - 120:
                self.__horn_fx.play()
                self.__is_horn = True