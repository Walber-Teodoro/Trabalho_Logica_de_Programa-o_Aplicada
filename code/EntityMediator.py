from code.Enemy import Enemy
from code.Entity import Entity
from code.Player import Player


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        pass

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            ent1 = entity_list[i]

            for j in range(i + 1, len(entity_list)):
                ent2 = entity_list[j]

                if (isinstance(ent1, Player) and isinstance(ent2, Enemy)) or \
                        (isinstance(ent2, Player) and isinstance(ent1, Enemy)):

                    if ent1.hitbox.colliderect(ent2.hitbox):
                        return True
                    return False