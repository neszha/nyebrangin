import pygame as pg
from src.config import *
from src.state import *
from src.components.Button import Button
from src.components.Text import Text

class PopUp:
    
    def __init__(self, title, background_path):
        self._show = True
        self.__title = title
        self.__background = background_path

        self.__load_componenets()

    def __load_componenets(self):
        # Load background.
        self.background = pg.image.load(self.__background).convert_alpha()
        self.background_rect = self.background.get_rect(center = (WIDTH/2, HEIGTH/2))
        [bg_size_x, bg_size_y] = self.background.get_size()

        # Load title
        title_pos_x = (WIDTH/2)
        title_pos_y = (HEIGTH/2) - (bg_size_y/2) + 50
        self.title = Text(self.__title, [title_pos_x, title_pos_y], 40)

        # Load tombol tutup popup.
        btn_pos_x = (WIDTH/2) + (bg_size_x/2) - 60
        btn_pos_y = (HEIGTH/2) - (bg_size_y/2) + 50
        self.btn_close = Button('assets/buttons/btn-close.png', [btn_pos_x, btn_pos_y], self.close)
    
    def render_popup(self, screen):
        if self._show:
            screen.blit(self.background, self.background_rect)
            self.btn_close.render(screen)
            self.title.render(screen)

    def open(self):
        self._show = True
        SHOW_POPUP = True

    def close(self):
        self._show = False
        SHOW_POPUP = False