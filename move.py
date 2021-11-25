import yaml
from effect import Effect
from move_types import supereffective, weak, immune

# get moves data
with open("moves.yaml") as f:
    movesDb = yaml.load(f, Loader=yaml.FullLoader)


class Move:
    SUPEREFFECTIVE_MULTIPLIER = 2
    NOT_VERY_EFFECTIVE_MULTIPLIER = 0.5
    TYPE_MULTIPLIER = 1.5

    def __init__(self, move_dict):
        self.id = move_dict['id']
        self.name = move_dict['name']
        self.type = move_dict['type']

        self.effect_type = move_dict['effectType']
        self.effect = self.create_effect(move_dict['effect'])
    
    def create_effect(self, effect_json):
        if self.effect_type == "RANDINT":
            return Effect.create_effect(self, f"target.hurt(r.int({effect_json[0]}, {effect_json[1]}), user, move.type)")
        elif self.effect_type == "CUSTOM":
            return Effect.create_effect(self, effect_json)
        else:
            raise Exception(f"Unknown effect type: {self.effect_type}")

    def use(self, target, user):
        self.effect.use(target, user)
    
    @staticmethod
    def calculate_dmg(dmg, user, target, type):
        base_dmg = dmg + user.power - target.defense

        if supereffective(type, target.type):
            print("It's super effective!")
            base_dmg *= Move.SUPEREFFECTIVE_MULTIPLIER

        if weak(type, target.type):
            print("It's not very effective...")
            base_dmg *= Move.NOT_VERY_EFFECTIVE_MULTIPLIER

        if type == user.type:
            print("It's a type bonus!")
            base_dmg *= Move.TYPE_MULTIPLIER
        
        if immune(type, target.type):
            print("It isn't affected by that move...")
            base_dmg = 0
        
        return round(base_dmg)

    
    def __str__(self):
        return f"{self.name}"
