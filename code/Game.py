import sys

import pygame
from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Instructions import Instructions
from code.Menu import Menu
from code.Level import Level
from code.GameOver import GameOver

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:
                level = Level(self.window, 'Level1', menu_return)
                level_return = level.run()

                if isinstance(level_return, int):
                    game_over = GameOver(self.window)
                    game_over.run(level_return)

            elif menu_return == MENU_OPTION[1]:  # Menu Score
                instruction_screen = Instructions(self.window)
                instruction_screen.show()


            elif menu_return == MENU_OPTION[2]:
                pygame.quit()
                sys.exit()
