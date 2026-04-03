import pygame

from code.Const import WIN_WIDTH, GRAVITY, PLAYER_JUMP_FORCE
from code.Entity import Entity


class Player(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name + '0',position)
        self.animation_list = []
        # Load Frame Animations
        for i in range(6):
            img = pygame.image.load(f'./asset/Player{i}.png').convert_alpha()
            img = pygame.transform.scale(img, (128,128))
            self.animation_list.append(img)

        self.frame_index = 0
        self.image = self.animation_list[self.frame_index]

        self.vertical_speed = 0
        self.is_jumping = False
        self.ground_y = position[1]  # Guarda a posição inicial como o "chão"

    def update_hitbox(self):
        #ajuste da Hitbox pra ficar no centro do player
        self.hitbox.center = (self.rect.centerx + 50, self.rect.centery)

    def move(self):
        pressed_key = pygame.key.get_pressed()

        # Movimentação Horizontal
        if pressed_key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 2
        if pressed_key[pygame.K_RIGHT] and self.rect.right < WIN_WIDTH:
            self.rect.x += 2

        # Comando do Pulo
        if pressed_key[pygame.K_UP] and not self.is_jumping:
            self.vertical_speed = -PLAYER_JUMP_FORCE
            self.is_jumping = True

        # Gravidade e Chão
        self.vertical_speed += GRAVITY
        self.rect.y += self.vertical_speed

        if self.rect.y >= self.ground_y:
            self.rect.y = self.ground_y
            self.vertical_speed = 0
            self.is_jumping = False

        self.frame_index += 0.1
        if self.frame_index >= len(self.animation_list):
            self.frame_index = 0

        self.surf = self.animation_list[int(self.frame_index)]

        # Ajuste de Hitbox
        self.hitbox = self.rect.inflate(0, 150)
        self.update_hitbox()