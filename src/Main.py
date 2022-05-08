import pygame as pg
import src.state as state
from src.config import *
from src.Menu import Menu
from src.Level import Level

class Main:

    def __init__(self, game_name):
        self.__game_name = game_name
        self.__menu = None
        self.__level = None

        # Menyiapkan game.
        pg.init()
        pg.display.set_caption(self.__game_name)
        self.clock = pg.time.Clock()

    def __watch_page_change(self):
        if state.PAGE == 'menu':
            if not self.__menu: 
                self.__menu = Menu()
                self.__level = None
            self.__menu.render()
        elif state.PAGE == 'game-run':
            if not self.__level: 
                self.__level = Level()
                self.__menu = None
            self.__level.render()

    def run(self):
        while True:
            # Mengawasi event exit.
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.menu.exit()
                if event.type == pg.MOUSEMOTION:
                    print(pg.mouse.get_pos())
            
            # Update tampilan game.
            self.__watch_page_change()
            pg.display.update()
            self.clock.tick(FPS)