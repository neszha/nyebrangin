import pygame as pg
import src.state as state
from src.config import *
from src.components.Text import Text
from src.components.PopUp import PopUp
from src.components.Button import Button

class Data: pass
class WaitingPlay(PopUp):

    def __init__(self, start_command):
        self.__start_command = start_command
        self.__texts = []
        
        level = f'Level {state.LEVEL_RUNNING}'
        bg = 'assets/images/backgrounds/settings.png'
        super().__init__(level, bg, False)
        self.__load_local_componenets()

    def __load_local_componenets(self):
        [bg_size_x, bg_size_y] = self.background.get_size()
        text_pos_x = (WIDTH/2)
        text_pos_y = (HEIGTH/2) - (bg_size_y/2) + 140
        self.__texts.append(Text('Press Enter to Play Game.', [text_pos_x, text_pos_y], 36))
        self.__btn = Button('assets/images/buttons/to-home.png', [text_pos_x, text_pos_y + 100], command0=self.__back_to_menu)

    def __input_keys(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_RETURN]:
            self.__start_command()
            self.close()

    def __back_to_menu(self):
        state.PAGE = 'menu'
        self.close()

    def render(self, screen):
        if self._show:
            self.__input_keys()
            self.render_popup(screen)
            for text in self.__texts: text.render(screen)
            self.__btn.render(screen)