import src.state as state
from src.config import *
from src.components.Text import Text
from src.components.PopUp import PopUp
from src.components.Checkbox import CheckBox

# Menampilkan popup pengaturan.
class Settings(PopUp):

    def __init__(self):
        super().__init__('Settings', 'assets/images/backgrounds/settings.png')
        self._load_local_components()

    def _load_local_components(self):
        [bg_size_x, bg_size_y] = self.background.get_size()

        ## Load komponen teks.
        txt_pos_x = (WIDTH/2) - (bg_size_x/4)
        txt_pos_y = (HEIGTH/2) - 30
        self.__txt_music = Text('Music', [txt_pos_x, txt_pos_y], 40)
        self.__txt_sound_fx = Text('Sound FX', [txt_pos_x, txt_pos_y + 80], 40)

        ## Load komponene checkbox.
        check_pos_x = txt_pos_x + (bg_size_x/2)
        check_pos_y = txt_pos_y
        self.__check_music = CheckBox([check_pos_x, check_pos_y], self.__check_music_handdler)
        self.__check_sound_fx = CheckBox([check_pos_x, check_pos_y + 80], self.__check_sound_fx_handdler)
        
        # Load default settings.
        self.__check_music.checked = state.MUSIC
        self.__check_sound_fx.checked = state.SOUND_FX

    def __check_music_handdler(self):
        state.MUSIC = self.__check_music.checked

    def __check_sound_fx_handdler(self):
        state.SOUND_FX = self.__check_sound_fx.checked

    def render(self, screen):
        if self._show:
            self.render_popup(screen)
            self.__txt_music.render(screen)
            self.__txt_sound_fx.render(screen)
            self.__check_music.render(screen)
            self.__check_sound_fx.render(screen)