import pygame, sys
from src.config import *
from src.state import *
from src.Menu import Menu

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

    def run(self):
        while True:
            # Mengawasi event exit.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.menu.exit()

                if event.type == pygame.MOUSEMOTION:
                    print(pygame.mouse.get_pos())

            self.watch_page()

            # Update tampilan game.
            pygame.display.update()
            self.clock.tick(FPS)

    def watch_page(self):
        if PAGE == 'menu':
            self.menu.render()