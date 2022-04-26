import pygame
from src.config import *
from random import randrange

class CarMenuAnimation:

    def __init__(self, direction, speed):
        self.direction = direction #('to-left', 'to-right')
        self.speed = speed
        self.positions = [0, 566]
        self.patch_cars = [
            'assets/cars/horizontal/baby.png',
            'assets/cars/horizontal/sedan.png',
            'assets/cars/horizontal/sport.png',
        ]
        
        self.__load_components()

    def __load_components(self):
        # Mengacak jenis mobil.
        use_car = self.patch_cars[randrange(0, len(self.patch_cars))]
        self.car = pygame.image.load(use_car).convert_alpha()
        if self.direction == 'to-left':
            self.car = pygame.transform.flip(self.car, True, False)
            self.positions[1] -= 12

        # Mengacak poisis x mobil.
        self.positions[0] = randrange(0, WIDTH)

    def render(self, screen):
        # Update posisi mobil berdasarkan arah gerak.
        if self.direction == 'to-right':
            self.positions[0] += self.speed
            if self.positions[0] > (WIDTH + 100): 
                self.positions[0] = -100
                self.speed = randrange(2, 6)
        elif self.direction == 'to-left':
            self.positions[0] -= self.speed
            if self.positions[0] < -100: 
                self.positions[0] = WIDTH + 100
                self.speed = randrange(2, 6)

        # Render mobil ke layar.
        self.car_rect = self.car.get_rect(midbottom = self.positions)
        screen.blit(self.car, self.car_rect)