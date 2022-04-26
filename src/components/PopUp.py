import pygame as pg
from src.config import *
from src.components.Button import Button

class PopUp:
    
    def __init__(self, title, background_image):
        self._show = False
        self.__title = title

        # Load background.
        self.background = pg.image.load(background_image).convert_alpha()
        self.background_rect = self.background.get_rect(center = (WIDTH/2, HEIGTH/2))

        # Load tombol tutup popup.
        [size_x, size_y] = self.background.get_size()
        pos_x = (WIDTH/2) + (size_x/2) - 60
        pos_y = (HEIGTH/2) - (size_y/2) + 50
        self.btn_close = Button('assets/buttons/btn-close.png', [pos_x, pos_y], self.close)
    
    def render_popup(self, screen):
        if self._show:
            screen.blit(self.background, self.background_rect)
            self.btn_close.render(screen)

    def open(self):
        self._show = True

    def close(self):
        self._show = False