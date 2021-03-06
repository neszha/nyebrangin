import pygame as pg
import src.state as state
from src.config import *
from src.Menu import Menu
from src.Level import Level
from src.Store import Store

# Kelas utama sebagai game loop.
class Main:

    def __init__(self, game_name):
        self.__game_name = game_name
        self.__menu = None
        self.__level = None

        # Menyiapkan game.
        pg.init()
        pg.mixer.init() 
        pg.display.set_caption(self.__game_name)
        self.__clock = pg.time.Clock()

        # Load file temporary.
        store = Store()
        store.load_checkpoints()

    def __watch_page(self):
        if state.PAGE == 'menu':
            if not self.__menu: 
                self.__menu = Menu()
                if self.__level:
                    self.__level.backsong.stop()
                    self.__level = None
            self.__menu.render()
        elif state.PAGE == 'game-run':
            if not self.__level: 
                self.__level = Level()
                if self.__menu:
                    self.__menu.backsong.stop()
                    self.__menu = None
            if state.LEVEL_RESET:
                self.__level.backsong.stop()
                self.__level = None
                self.__level = Level()
                state.LEVEL_RESET = False
            self.__level.render()
        elif state.PAGE == 'loading-screen':
            if self.__menu: self.__menu = None
            if self.__level: self.__level = None

    def run(self):
        while True:
            # Mengawasi event exit.
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.menu.exit()
                # if event.type == pg.MOUSEMOTION:
                #     # print(pg.mouse.get_pos())
            
            # Update tampilan game.
            self.__watch_page()
            pg.display.update()
            self.__clock.tick(FPS)