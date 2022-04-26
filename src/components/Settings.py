from src.state import *
from src.config import *
from src.components.PopUp import PopUp
from src.components.Text import Text
from src.components.Checkbox import CheckBox

class Settings(PopUp):

    def __init__(self):
        super().__init__('Settings', 'assets/backgrounds/layer-settings.png')

        self.__load_local_componenets()

    def __load_local_componenets(self):
        [bg_size_x, bg_size_y] = self.background.get_size()

        ## Load komponen teks.
        txt_pos_x = (WIDTH/2) - (bg_size_x/4)
        txt_pos_y = (HEIGTH/2) - 30
        self.txt_music = Text('Music', [txt_pos_x, txt_pos_y], 40)
        self.txt_sound = Text('Sound FX', [txt_pos_x, txt_pos_y + 80], 40)

        ## Load komponene checkbox.
        self.check_music = CheckBox([100, 100], self.__check_handdler)

    def __check_handdler(self):
        print('check')

    def render(self, screen):
        if self._show:
            self.render_popup(screen)
            self.txt_music.render(screen)
            self.txt_sound.render(screen)
            self.check_music.render(screen)