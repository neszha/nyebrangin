import pygame as pg
from src.config import *

class Car(pg.sprite.Sprite):
    
    def __init__(self, path, position, direction, speed):
        super().__init__()
        self.__direction = direction
        self.__speed = speed
        self.__load_car(path, position)
    
    def __load_car(self, path, position):
        self.image = pg.image.load(path).convert_alpha()
        self.rect = self.image.get_rect(topleft=position)
        if self.__direction == 'left': self.image = pg.transform.flip(self.image, True, False)

    def update(self): 
        if self.__direction == 'left': 
            self.rect.x += self.__speed
            if self.rect.x >= WIDTH + 120: self.kill()

        if self.__direction == 'right':
            self.rect.x -= self.__speed
            if self.rect.x < -120: self.kill()