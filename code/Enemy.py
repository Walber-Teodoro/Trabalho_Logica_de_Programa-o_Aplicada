
from code.Const import ENTITY_SPEED, WIN_WIDTH
from code.Entity import Entity

class Enemy(Entity):
    def __init__(self, name: str, position: tuple):

        super().__init__(name,position)
        self.speed = ENTITY_SPEED[self.name]

    def move(self):
        self.rect.x -= self.speed
        #if self.rect.right <= 0:
        #    self.rect.left = WIN_WIDTH
        #pass