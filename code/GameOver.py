import pygame, sys
from code.Const import WIN_WIDTH, WIN_HEIGHT, C_RED, C_WHITE, C_BLACK, C_YELLOW


class GameOver:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
        self.surf.fill(C_BLACK)

    def run(self, score):
        pygame.mixer_music.stop()  # Garante que a música da fase pare
        while True:
            self.window.blit(self.surf, (0, 0))

            # Textos na tela final de Game Over
            self.draw_text(60, "GAME OVER", C_RED, (WIN_WIDTH / 2, WIN_HEIGHT / 2 - 50))

            self.draw_text(30, f"PONTUAÇÃO FINAL: {score}", C_YELLOW, (WIN_WIDTH / 2, WIN_HEIGHT / 2))

            self.draw_text(20, "Pressione ENTER para Retornar ao Menu", C_WHITE, (WIN_WIDTH / 2, WIN_HEIGHT / 2 + 50))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return

    def draw_text(self, size, text, color, pos):
        font = pygame.font.SysFont("Lucida Sans Typewriter", size)
        text_surf = font.render(text, True, color)
        text_rect = text_surf.get_rect(center=pos)
        self.window.blit(text_surf, text_rect)