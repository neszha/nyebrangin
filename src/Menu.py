import sys
import pygame as pg
import src.state as state
from src.config import *
from random import randrange
from src.components.Audio import Audio
from src.components.Button import Button
from src.components.popups.Settings import Settings
from src.components.popups.BoxLevels import BoxLevels
from src.components.CarMenuAnimation import CarMenuAnimation as Car
from src.components.CloudMenuAnimation import CloudMenuAnimation as Cloud

# Menangani tampilan dan fitur menu utama game.
class Menu:
    
    def __init__(self):
        self.__screen = pg.display.set_mode((WIDTH, HEIGTH))
        self.__load_components()

    def __load_components(self):
        # Load basksong menu.
        self.backsong = Audio('assets/audios/backsongs/bs-menu.mp3', 'music')
        self.backsong.play(loops=-1)

        # Membuat background.
        self.__background = pg.Surface((WIDTH, HEIGTH))
        self.__background.fill(pg.Color(175, 208, 233))

        # Menyiapkan komponen gambar.
        self.__grass = pg.image.load('assets/images/menu-grass.png').convert()
        self.__road = pg.image.load('assets/images/menu-road.png').convert()
        self.__text_logo = pg.image.load('assets/images/text-logo.png').convert_alpha()
        self.__arrow_direction = pg.image.load('assets/images/arrow-direction.png').convert_alpha()
        self.__note_board = pg.image.load('assets/images/note-board.png').convert_alpha()
        self.__cars = []
        self.__clouds = []
        for i in range(4): self.__cars.append(Car('to-left', randrange(2, 6)))            
        for i in range(4): self.__cars.append(Car('to-right', randrange(2, 6)))
        for i in range(8): self.__clouds.append(Cloud())            

        # Menetapkan poisis komponene mengunakan rectangle.
        self.__grass_rect = self.__grass.get_rect(bottomleft = (0, HEIGTH))
        self.__road_rect = self.__road.get_rect(bottomleft = (0, HEIGTH - self.__grass.get_size()[1]))
        self.__text_logo_rect = self.__text_logo.get_rect(center = (WIDTH/2, 138))
        self.__arrow_direction_rect = self.__arrow_direction.get_rect(center = (160, 590))
        self.__note_board_rect = self.__note_board.get_rect(topleft=(977, 500))

        # Load komponen pop-up.
        self.__settings = Settings()
        self.__box_levels = BoxLevels()

        # Load komponen tombol.
        self.__buttons = [
            Button('assets/images/buttons/setting.png', [40, 40], self.__settings.open),
            Button('assets/images/buttons/start.png', [WIDTH/2, 280], self.__box_levels.open),
            Button('assets/images/buttons/exit.png', [WIDTH/2, 380], self.exit),
        ]

    def render(self):
        self.backsong.watch_setting()
        self.__screen.blit(self.__background, (0, 0))
        self.__screen.blit(self.__grass, self.__grass_rect)
        self.__screen.blit(self.__road, self.__road_rect)
        for car in self.__cars: car.render(self.__screen)
        for cloud in self.__clouds: cloud.render(self.__screen)
        self.__screen.blit(self.__text_logo, self.__text_logo_rect)
        self.__screen.blit(self.__arrow_direction, self.__arrow_direction_rect)
        self.__screen.blit(self.__note_board, self.__note_board_rect)
        for btn in self.__buttons: btn.render(self.__screen)
        self.__settings.render(self.__screen)
        self.__box_levels.render(self.__screen)
    
    def exit(self):
        if not state.SHOW_POPUP:
            pg.quit()
            sys.exit()