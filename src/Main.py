import pygame, sys
from src.config import *

class Main:

    def __init__(self, game_name):
        self.game_name = game_name
        self.levels = []
        self.index_level = 0
        self.total_point = 0

        # Menyiapkan game.
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        pygame.display.set_caption(self.game_name)
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            # Mengawasi event exit.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit()

            # Update tampilan game.
            self.screen.fill('black')
            pygame.display.update()
            print("asfd")
            self.clock.tick(FPS)

    def start_level(self):
        pass
 
    def exit(self): 
        pygame.quit()
        sys.exit()