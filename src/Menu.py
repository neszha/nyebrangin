import pygame
from random import randrange, uniform
from src.config import *

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


class CloudMenuAnimation:

    def __init__(self):
        self.directions = ('to-left', 'to-right')
        self.scale = 1
        self.speed = 0
        self.positions = [0, 0]
        self.image_patch = 'assets/images/cloud.png'

        self.__load_components()

    def __load_components(self):
        # Random arah, ukuran, poisis, dan kecepatan awan.
        self.direction = self.directions[randrange(0, 2)]
        self.scale = uniform(1.0, 1.8)
        self.speed = uniform(0.5, 1.5)
        self.positions = [randrange(25, WIDTH-25), randrange(50, 450)]
        
        # Menyiapkan awan.
        self.cloud = pygame.image.load(self.image_patch).convert_alpha()
        [size_x, size_y] = self.cloud.get_size()
        self.cloud = pygame.transform.scale(self.cloud, (size_x * self.scale, size_y * self.scale))
        if self.direction == 'to-left':
            self.cloud = pygame.transform.flip(self.cloud, True, False)
        
    def render(self, screen):
        # Update lokasi awan berdasarkan arah gerak.
        if self.direction == 'to-right':
            self.positions[0] += self.speed
            if self.positions[0] > (WIDTH + 100): 
                self.positions[0] = -100
        elif self.direction == 'to-left':
            self.positions[0] -= self.speed
            if self.positions[0] < -100: 
                self.positions[0] = WIDTH + 100

        # Render awan ke layar.
        self.cloud_rect = self.cloud.get_rect(midbottom = self.positions)
        screen.blit(self.cloud, self.cloud_rect)


class Menu:
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((WIDTH, HEIGTH))
        self.__load_components()

    def __load_components(self):
        # Membuat background.
        self.__background = pygame.Surface((WIDTH, HEIGTH))
        self.__background.fill(pygame.Color(175, 208, 233))

        # Menyiapkan komponen gambar.
        self.__grass = pygame.image.load('assets/grasses/menu-grass.png').convert()
        self.__road = pygame.image.load('assets/roads/menu-road.png').convert()
        self.__text_logo = pygame.image.load('assets/images/text-logo.png').convert_alpha()
        self.__cars = []
        for i in range(4): self.__cars.append(CarMenuAnimation('to-left', randrange(2, 6)))            
        for i in range(4): self.__cars.append(CarMenuAnimation('to-right', randrange(2, 6)))
        self.__clouds = []
        for i in range(8): self.__clouds.append(CloudMenuAnimation())            

        # Menetapkan poisis komponene mengunakan rectangle.
        self.__grass_rect = self.__grass.get_rect(bottomleft = (0, HEIGTH))
        self.__road_rect = self.__road.get_rect(bottomleft = (0, HEIGTH - self.__grass.get_size()[1]))
        self.__text_logo_rect = self.__text_logo.get_rect(center = (WIDTH/2, 138))

    def render(self):
        # Render komponene ke layar.
        self.__screen.blit(self.__background, (0, 0))
        self.__screen.blit(self.__grass, self.__grass_rect)
        self.__screen.blit(self.__road, self.__road_rect)
        for car in self.__cars: car.render(self.__screen)
        for cloud in self.__clouds: cloud.render(self.__screen)
        self.__screen.blit(self.__text_logo, self.__text_logo_rect)
    
        