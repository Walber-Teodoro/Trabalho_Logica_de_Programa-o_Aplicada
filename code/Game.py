import pygame
from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Menu import Menu
from code.Level import Level
from code.GameOver import GameOver  # 1. Importe a nova classe


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:  # Se escolheu NEW GAME
                level = Level(self.window, 'Level1', menu_return)
                level_return = level.run()

                # 2. Verifique o retorno do Level
                if level_return == 'GAME_OVER':
                    game_over = GameOver(self.window)
                    game_over.run()  # Executa a tela de Game Over
                    # Após o game_over.run() terminar (ao apertar Enter),
                    # o loop recomeça e volta naturalmente para o Menu.

            elif menu_return == MENU_OPTION[2]:  # Se escolheu EXIT
                pygame.quit()
                quit()