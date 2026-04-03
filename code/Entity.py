from abc import ABC, abstractmethod

import pygame.image
import pygame.transform

from code.Const import WIN_WIDTH, WIN_HEIGHT


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./asset/' + name + '.png').convert_alpha()

        if 'Bg' in name:
            self.surf = pygame.transform.scale(self.surf, (WIN_WIDTH, WIN_HEIGHT))

        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0

        self.hitbox = self.rect.inflate(0, 0)
        self.update_hitbox()

    @abstractmethod
    def move(self):
        self.rect.centerx -= 1
        pass

    def update_hitbox(self):
        self.hitbox.center = self.rect.center # Ajuste de hitbox
