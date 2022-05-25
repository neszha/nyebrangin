import pygame as pg
from src.config import *
from random import randrange

# Membuat karakter animasi mobil untuk halaman menu.
class CarMenuAnimation:

    def __init__(self, direction, speed):
        self.__direction = direction # ('to-left', 'to-right')
        self.__speed = speed
        self.__position = [0, 566]
        self.__patch_cars = [
            'assets/images/cars/horizontal/baby.png',
            'assets/images/cars/horizontal/sedan.png',
            'assets/images/cars/horizontal/sport.png',
        ]
        
        self.__load_components()

    def __load_components(self):
        # Mengacak jenis mobil.
        use_car = self.__patch_cars[randrange(0, len(self.__patch_cars))]
        self.__car = pg.image.load(use_car).convert_alpha()
        if self.__direction == 'to-left':
            self.__car = pg.transform.flip(self.__car, True, False)
            self.__position[1] -= 12

        # Mengacak poisis x mobil.
        self.__position[0] = randrange(0, WIDTH)

    def render(self, screen):
        # Update posisi mobil berdasarkan arah gerak.
        if self.__direction == 'to-right':
            self.__position[0] += self.__speed
            if self.__position[0] > (WIDTH + 100): 
                self.__position[0] = -100
                self.__speed = randrange(2, 6)
        elif self.__direction == 'to-left':
            self.__position[0] -= self.__speed
            if self.__position[0] < -100: 
                self.__position[0] = WIDTH + 100
                self.__speed = randrange(2, 6)

        # Render mobil ke layar.
        car_rect = self.__car.get_rect(midbottom = self.__position)
        screen.blit(self.__car, car_rect)