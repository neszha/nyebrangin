from time import sleep
import pygame as pg
import src.state as state
from src.config import *
from src.components.Text import Text
from src.components.PopUp import PopUp
from src.components.Button import Button

class Data: pass
class Finish(PopUp):

    def __init__(self):
        self.__time_left = '00:00'
        self.__trophy_number = 1
        super().__init__('FINISH!', 'assets/images/backgrounds/end.png', False)
        self.__load_local_componenets()

    def __load_local_componenets(self):
        [bg_size_x, bg_size_y] = self.background.get_size()
        self.__texts = [
            Text(
                'Time Left', 
                [(WIDTH/2) - (bg_size_x/4), (HEIGTH/2) - 70],
                36
            ),
            Text(
                self.__time_left, 
                [(WIDTH/2) + (bg_size_x/4), (HEIGTH/2) - 70],
                36
            )
        ]
        self.__btns = [
            Button(
                f'assets/images/trophy{self.__trophy_number}.png',
                [(WIDTH/2), (HEIGTH/2) + 40],
            ),
            Button(
                'assets/images/buttons/next-level.png', 
                [(WIDTH/2), (HEIGTH/2) + (bg_size_y/2) - 60],
                command0=self.__next_level
            )
        ]
    
    def set_item(self, time_left, trophy_number):
        self.__time_left = time_left
        self.__trophy_number = trophy_number
        self.__load_local_componenets()
        print(self.__time_left)

    def __next_level(self): 
        state.PAGE = 'menu'
        state.LEVEL_RUNNING += 1
        if state.CURRENT_LEVEL < state.LEVEL_RUNNING: state.CURRENT_LEVEL = state.LEVEL_RUNNING
        self.close()

    def render(self, screen):
        if self._show:
            self.render_popup(screen)
            for text in self.__texts: text.render(screen)
            for btn in self.__btns: btn.render(screen)