import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

import random

from code.Const import C_WHITE, WIN_HEIGHT, SPAWN_DELAY, ENEMY_LIST, WIN_WIDTH, C_YELLOW, C_RED
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator


class Level:

    def __init__(self, window, name, menu_option):
        self.score = 0
        self.spawn_timer = None
        self.timeout = 60000
        self.window = window
        self.name = name
        self.menu_option = menu_option
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.player = EntityFactory.get_entity('Player0')
        self.entity_list.append(self.player)


    def run(self):
        pygame.mixer.music.load(f'./asset/{self.name}.ogg')
        pygame.mixer.music.play(-1)
        clock = pygame.time.Clock()
        start_time = pygame.time.get_ticks()
        total_time = 60000
        self.spawn_timer = 0

        while True:
            clock.tick(60)

            tempo_passado = pygame.time.get_ticks() - start_time
            self.timeout = total_time - tempo_passado #passagem do tempo da fase

            if self.timeout <= 0:
                pygame.mixer.music.stop() #condição de timeout do jogo
                return 'GAME_OVER'

            self.spawn_timer += 1
            if self.spawn_timer >= SPAWN_DELAY: #geração de inimigos

                inimigo_aleatorio = random.choice(ENEMY_LIST)

                novo_inimigo = EntityFactory.get_entity(inimigo_aleatorio)

                self.entity_list.append(novo_inimigo)

                self.spawn_timer = 0

            for ent in self.entity_list[:]:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

                # Teste de hitbox (retirar o # da função abaixo pra ativar)
                # pygame.draw.rect(self.window, (255, 0, 0), ent.hitbox, 2)

                if ent.name in ENEMY_LIST and ent.rect.right < 0:
                    self.entity_list.remove(ent)
                    self.score += 10
                    print(f"Pontuação: {self.score}")

            from code.EntityMediator import EntityMediator
            if  EntityMediator.verify_collision(entity_list=self.entity_list):
                pygame.mixer_music.stop()
                return self.score   #retorna a pontuação final ao encerrar o jogo

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.mixer.music.stop()  # Função para retornar ao menu apertando o ESC
                        return 'MENU'

            self.level_text(14, f'{self.name} - Timeout:{self.timeout / 1000 :.1f}s', C_WHITE, (10, 5))
            self.level_text(14, f'fps: {clock.get_fps():.0f}', C_WHITE,(10, WIN_HEIGHT - 35))
            self.level_text(20, f'Score: {self.score}', C_RED, (WIN_WIDTH - 150, 10))
            pygame.display.flip()
            pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
