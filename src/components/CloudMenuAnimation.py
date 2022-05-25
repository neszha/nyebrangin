import pygame as pg
from src.config import *
from random import randrange, uniform

# Membuat karakter animasi awan untuk halaman menu.
class CloudMenuAnimation:

    def __init__(self):
        self.__direction = ('to-left', 'to-right')
        self.__scale = 1
        self.__speed = 0
        self.__position = [0, 0]
        self.__image_patch = 'assets/images/cloud.png'

        self.__load_components()

    def __load_components(self):
        # Random arah, ukuran, poisis, dan kecepatan awan.
        self.__direction = self.__direction[randrange(0, 2)]
        self.__scale = uniform(1.0, 1.8)
        self.__speed = uniform(0.5, 1.5)
        self.__position = [randrange(25, WIDTH-25), randrange(50, 450)]
        
        # Menyiapkan awan.
        self.__cloud = pg.image.load(self.__image_patch).convert_alpha()
        [size_x, size_y] = self.__cloud.get_size()
        self.__cloud = pg.transform.scale(self.__cloud, (size_x * self.__scale, size_y * self.__scale))
        if self.__direction == 'to-left':
            self.__cloud = pg.transform.flip(self.__cloud, True, False)
        
    def render(self, screen):
        # Update lokasi awan berdasarkan arah gerak.
        if self.__direction == 'to-right':
            self.__position[0] += self.__speed
            if self.__position[0] > (WIDTH + 100): 
                self.__position[0] = -100
        elif self.__direction == 'to-left':
            self.__position[0] -= self.__speed
            if self.__position[0] < -100: 
                self.__position[0] = WIDTH + 100

        # Render awan ke layar.
        cloud_rect = self.__cloud.get_rect(midbottom = self.__position)
        screen.blit(self.__cloud, cloud_rect)