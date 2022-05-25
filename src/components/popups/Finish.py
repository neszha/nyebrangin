import src.state as state
from src.config import *
from src.Store import Store
from src.components.Text import Text
from src.components.PopUp import PopUp
from src.components.Button import Button

class Data: pass

# Menampilkan popup game finish.
class Finish(PopUp):

    def __init__(self):
        self.__time_left = '00:00'
        self.__trophy_number = 1
        self.__store = Store()
        super().__init__('FINISH!', 'assets/images/backgrounds/end.png', False)
        self._load_local_components()

    def _load_local_components(self):
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
                [(WIDTH/2), (HEIGTH/2) + 40], index=2
            ),
            Button(
                'assets/images/buttons/next-level.png', 
                [(WIDTH/2), (HEIGTH/2) + (bg_size_y/2) - 60],
                command0=self.__next_level, index=2
            )
        ]

    def __next_level(self): 
        state.PAGE = 'menu'
        self.__store.save_checkpoint(self.__time_left, self.__trophy_number)
        state.LEVEL_RUNNING += 1
        if state.LEVEL_RUNNING > state.MAX_LEVEL:
            state.LEVEL_RUNNING = state.MAX_LEVEL
        if state.CURRENT_LEVEL < state.LEVEL_RUNNING: 
            state.CURRENT_LEVEL = state.LEVEL_RUNNING
        self.close()

    def set_item(self, time_left, trophy_number):
        self.__time_left = time_left
        self.__trophy_number = trophy_number
        self.__load_local_componenets()

    def render(self, screen):
        if self._show:
            self.render_popup(screen)
            for text in self.__texts: text.render(screen)
            for btn in self.__btns: btn.render(screen)