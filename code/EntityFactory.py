from code.Background import Background
from code.Const import WIN_WIDTH, ENEMY_LIST
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Player0':
                return Player('Player', (50, 270))

            case 'Enemy0' | 'Enemy1' | 'Enemy2' | 'Enemy3':
                return Enemy(entity_name, (WIN_WIDTH + 50, 365))

