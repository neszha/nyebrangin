import src.state as state
from src.config import *
from src.components.Text import Text
from src.components.PopUp import PopUp
from src.components.Button import Button

class GameOver(PopUp):

    def __init__(self):
        super().__init__('GAME OVER!', 'assets/images/backgrounds/settings.png', False)
        self.__load_local_componenets()

    def __load_local_componenets(self):
        [bg_size_x, bg_size_y] = self.background.get_size()
        self.__texts = [
            Text(
                'Never GiveUp!', 
                [(WIDTH/2), (HEIGTH/2) - 16],
                36
            ),
        ]
        self.__btns = [
            Button(
                'assets/images/buttons/home.png', 
                [(WIDTH/2) - (bg_size_x/3.5), (HEIGTH/2) + (bg_size_y/2) - 60],
                command0=self.__to_home
            ),
            Button(
                'assets/images/buttons/play-again.png', 
                [(WIDTH/2) + (bg_size_x/6), (HEIGTH/2) + (bg_size_y/2) - 60],
                command0=self.__play_again
            ),
        ]

    def __to_home(self):
        state.PAGE = 'menu'
        self.close()

    def __play_again(self):
        state.LEVEL_RESET = True

    def render(self, screen):
        if self._show:
            self.render_popup(screen)
            for text in self.__texts: text.render(screen)
            for btn in self.__btns: btn.render(screen)