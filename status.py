from namespace import Namespace
import random

# an abstract status class
class Status:
    def __init__(self, pokemon, user=None):
        self.pokemon = pokemon
        self.user = user
        self.turns = 0
        self.keep = True
    
    # Potentially set keep to false if enough turns have passed or some condition is met, which means the status will end.
    def turn(self):
        pass

class Sleep(Status):
    asleepMove = {
        "id": 0,
        "name": "Asleep",
        "type": "Normal",
        "effectType": "CUSTOM",
        "effect": "None"
    }

    def __init__(self, pokemon):
        from move import Move

        super().__init__(pokemon)
        self.old_moves = self.pokemon.moves
        self.pokemon.moves = [Move(self.asleepMove)]
        print(f"{pokemon.name} fell asleep!")
    
    def turn(self):
        self.turns += 1
        if self.turns >= 3:
            print(f"{self.pokemon.name} woke up!")
            self.keep = False
            self.pokemon.moves = self.old_moves


class Leech_Seed_Target(Status):
    # Leech seed does not end until the target is fainted.
    def __init__(self, pokemon, user):
        super().__init__(pokemon, user)
        print(f"{pokemon.name} was seeded!")
    
    def turn(self):
        dmg = (self.user.power or 1) * 3
        self.pokemon.hurt(dmg, self.user, "grass", "Leech Seed")

class Leech_Seed_User(Status):
    def __init__(self, pokemon, target):
        super().__init__(pokemon)
        self.target = target

    def turn(self):
        dmg = (self.pokemon.power or 1) * 3
        dmg = self.target.calculate_dmg(dmg, self.pokemon, "grass")
        self.pokemon.hp += dmg
        print(f"{self.pokemon.name} leeched {dmg} HP!")

class Burn(Status):
    def __init__(self, pokemon, user):
        super().__init__(pokemon, user)
        print(f"{pokemon.name} was burned!")
    
    def turn(self):
        self.turns += 1
        self.pokemon.hurt(random.randint(1, 4), self.user, "fire", "its burn")
        if self.turns >= 5:
            self.keep = False
            print(f"{self.pokemon.name} is no longer burned!")


# for statuses based on moves, they will be set using "_{moveid}" to prevent confusion about which statuses are builtinn
statuses = {
    "_7_user": Leech_Seed_User,
    "_7_target": Leech_Seed_Target,
    "sleep": Sleep,
    "burn": Burn
}

def setStatus(pokemon, status, *args, **kwargs):
    s = statuses.get(status)
    if s:
        pokemon.statuses.append(s(pokemon, *args, **kwargs))
    else:
        print(f"{status} is not a valid status!")

status = Namespace(set=setStatus)