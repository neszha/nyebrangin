from src.config import *
import src.state as state
from src.components.PopUp import PopUp
from src.components.Button import Button

class Data: pass

class BoxLevels(PopUp):

    def __init__(self):
        super().__init__('Levels', 'assets/backgrounds/levels.png')
        self.__load_local_componenets()

    def __load_local_componenets(self):
        [bg_size_x, bg_size_y] = self.background.get_size()

        # Mengambil lokasi gambar.
        path_level_lock = 'assets/buttons/levels/lock.png'
        path_levels = []
        for i in range(8): path_levels.append(f'assets/buttons/levels/{i+1}.png')

        # Inisialisasi tombol level.
        self.__btn_levels = []
        btn_pos_x = (WIDTH/2) - (bg_size_x/2) + 136
        btn_pos_y = (HEIGTH/2) - (bg_size_y/2) + 160
        for i in range(8):
            btn = Data()
            btn.level = i + 1
            btn.active = Button(path_levels[i], [btn_pos_x, btn_pos_y], command_data=self.__start_level, data=btn.level)
            btn.not_active = Button(path_level_lock, [btn_pos_x, btn_pos_y])
            self.__btn_levels.append(btn)
            btn_pos_x += 220
            if not (i+1) % 4:
                btn_pos_x = (WIDTH/2) - (bg_size_x/2) + 136
                btn_pos_y += 140

    def __start_level(self, index_level):
        state.LEVEL_RUNNING = index_level
        state.PAGE_FRAME = -1
        state.PAGE = 'game-run'

    def render(self, screen):
        if self._show:
            self.render_popup(screen)
            for i in range(len(self.__btn_levels)):
                btn = self.__btn_levels[i]
                if (i+1) <= state.CURRENT_LEVEL: btn.active.render(screen)
                else: btn.not_active.render(screen)