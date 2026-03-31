from code.Enemy import Enemy
from code.Entity import Entity
from code.Player import Player


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        # Esta parte serve para impedir que entidades saiam da janela
        # Você já faz algo similar no move() ou no Level.py
        pass

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            ent1 = entity_list[i]

            # Comparamos ent1 com todas as outras entidades à frente na lista
            for j in range(i + 1, len(entity_list)):
                ent2 = entity_list[j]

                # Regra: Se um for Player e o outro for Enemy (ou vice-versa)
                if (isinstance(ent1, Player) and isinstance(ent2, Enemy)) or \
                        (isinstance(ent2, Player) and isinstance(ent1, Enemy)):

                    if ent1.hitbox.colliderect(ent2.hitbox):
                        print(f"COLISÃO DETECTADA entre {ent1.name} e {ent2.name}!")
                        return True
                    return False