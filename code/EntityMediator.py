from code.Enemy import Enemy
from code.Entity import Entity



class EntityMediator:
    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy):


    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            test_entity = entity_list[i]
            EntityMediator.__verify_collision_window(test_entity)