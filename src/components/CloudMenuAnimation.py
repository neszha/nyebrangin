import pygame
from random import randrange, uniform
from src.config import *


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