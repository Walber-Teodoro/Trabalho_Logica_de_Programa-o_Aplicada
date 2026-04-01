import sys

import pygame

from code.Const import C_YELLOW, WIN_WIDTH, C_WHITE, C_RED


class Instructions:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/InstructionsBg.png').convert_alpha()

        # tamanho da janela
        self.width = 720
        self.height = 480

        # transformar a imagem do menu Score para a resolução desejada do projeto
        self.surf = pygame.transform.scale(self.surf, (self.width, self.height))
        self.rect = self.surf.get_rect(left=0, top=0)
        pass

    def show(self):
        pygame.mixer_music.load("./asset/Instructions.ogg")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)

            self.draw_text(35, "COMO JOGAR", C_RED, (WIN_WIDTH / 2, 50))

            instructions_text = [
                "Villager Run é um jogo de corrida lateral.",
                "Objetivo: Evitar os vegetais na tela.",
                "O jogo termina se colidir ou o tempo acabar.",
                "",
                "COMANDOS:",
                "SETAS DIREITA/ESQUERDA: Movimentar",
                "SETA PARA CIMA: Pular",
                "",
                "Pressione ESC para voltar ao Menu"
            ]

            for i, line in enumerate(instructions_text):
                self.draw_text(18, line, C_YELLOW, (WIN_WIDTH / 2, 120 + (i * 35)))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
            pygame.display.flip()

    def draw_text(self, size, text, color, pos):
        font = pygame.font.SysFont("Lucida Sans Typewriter", size)
        text_surf = font.render(text, True, color)
        text_rect = text_surf.get_rect(center=pos)
        self.window.blit(text_surf, text_rect)