import yaml
from move import Move, movesDb

# get pokemon data
with open('pokemon.yaml') as f:
    pokemonDb = yaml.load(f, Loader=yaml.FullLoader)

class Pokemon:
    def __init__(self, pokemon_dict):
        self.id = pokemon_dict['id']
        self.name = pokemon_dict['name']
        self.type = pokemon_dict['type']

        self.moves = []
        for move in pokemon_dict['moves']:
            self.load_move(move)

        self.max_hp = pokemon_dict['stats']['hp']
        self.hp = pokemon_dict['stats']["hp"]
        self.power = pokemon_dict['stats']["power"]
        self.defense = pokemon_dict['stats']["defense"]

        self.statuses = []
    
    def load_move(self, move_id):
        self.moves.append(Move(movesDb[str(move_id)]))
    
    def set(self, key, value):
        setattr(self, key, value)
    
    def is_alive(self):
        return self.hp > 0
    
    def use_move(self, move, target):
        print(f"{self.name} used {move.name}")
        move.use(target, self)
    
    def hurt(self, dmg, user, type, reason=None):
        dmg = Move.calculate_dmg(dmg, user, self, type)
        self.hp = self.hp - dmg
        if reason:
            return print(f"{self.name} took {dmg} damage from {reason}!")
        print(f"{self.name} took {dmg} damage!")
    
    def calculate_dmg(self, dmg, user, type):
        return Move.calculate_dmg(dmg, user, self, type)
    
    def turn(self):
        for status in self.statuses:
            status.turn()
            if not status.keep:
                self.statuses.remove(status)
