import pygame.image
import pygame.transform
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, C_WHITE, MENU_OPTION, C_YELLOW, C_RED


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/Bg.png').convert_alpha()

        # tamanho da janela
        self.width = 720
        self.height = 480

        # transformar a imagem do menu principal para a resolução desejada do projeto
        self.surf = pygame.transform.scale(self.surf, (self.width, self.height))
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        # initial position cursor
        menu_option = 0
        # play music in menu
        pygame.mixer_music.load("./asset/Menu.ogg")
        # music in loop
        pygame.mixer_music.play(-1)
        while True:
            #Draw Images
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(60, "Villager", C_WHITE, (WIN_WIDTH / 2, 60))
            self.menu_text(55, "Run", C_WHITE, (WIN_WIDTH / 2, 100))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(30, MENU_OPTION[i], C_RED, ((WIN_WIDTH / 2), 390 + 35 * i))
                else:
                    self.menu_text(30, MENU_OPTION[i], C_YELLOW, ((WIN_WIDTH / 2), 390 + 35 * i))

            # Check all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # close window
                    quit()  # end pygame

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0

                    if event.key == pygame.K_UP:
                            if menu_option > 0:
                                menu_option -= 1
                            else:
                                menu_option = len(MENU_OPTION) - 1

                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]

            pygame.display.flip()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
