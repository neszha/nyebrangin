import pygame
from src.config import *
import src.state as state 
from src.Menu import Menu
from src.Level import Level

class Main:

    def __init__(self, game_name):
        self.game_name = game_name
        self.levels = []
        self.index_level = 0
        self.total_point = 0

        # Menyiapkan game.
        pygame.init()
        pygame.display.set_caption(self.game_name)
        self.clock = pygame.time.Clock()

        # Daftar halaman game.
        self.menu = Menu()
        self.level = Level()

    def __watch_page_change(self):
        if state.PAGE == 'menu':
            self.menu.render()
        elif state.PAGE == 'game-run':
            print('game run')

    def run(self):
        while True:
            # Mengawasi event exit.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.menu.exit()
                if event.type == pygame.MOUSEMOTION:
                    print(pygame.mouse.get_pos())
            
            # Update tampilan game.
            self.__watch_page_change()
            pygame.display.update()
            self.clock.tick(FPS)