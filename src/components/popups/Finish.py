from time import sleep
import pygame as pg
import src.state as state
from src.config import *
from src.components.Text import Text
from src.components.PopUp import PopUp
from src.components.Button import Button

class Data: pass
class Finish(PopUp):

    def __init__(self, time_left='00:00', trophy_number=2):
        self.__texts = []
        self.__btns = []
        self.__time_left = time_left
        self.__trophy_number = str(trophy_number)
        super().__init__('FINISH!', 'assets/images/backgrounds/end.png', False)
        self.__load_local_componenets()

    def __load_local_componenets(self):
        [bg_size_x, bg_size_y] = self.background.get_size()  
        self.__texts.append(
            Text(
                'Time Left', 
                [(WIDTH/2) - (bg_size_x/4), (HEIGTH/2) - 70],
                36
            )
        )
        self.__texts.append(
            Text(
                self.__time_left, 
                [(WIDTH/2) + (bg_size_x/4), (HEIGTH/2) - 70],
                36
            )
        )
        self.__btns.append(
            Button(
                f'assets/images/trophy{self.__trophy_number}.png',
                [(WIDTH/2), (HEIGTH/2) + 40],
            )
        )
        self.__btns.append(
            Button(
                'assets/images/buttons/next-level.png', 
                [(WIDTH/2), (HEIGTH/2) + (bg_size_y/2) - 60],
                command0=self.__next_level
            )
        )

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