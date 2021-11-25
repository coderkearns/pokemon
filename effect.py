import random
from namespace import Namespace
from status import status


rand = Namespace({
    "int": random.randint
})

# Effects follow the pattern: lambda *, target=None, user=None, move=None, status=None, r=None, db=None: ...
class Effect:
    def __init__(self, move, effect):
        self.move = move
        self.effect = effect

    def use(self, target, user):
        if self.effect == None:
            return
        self.effect(target=target, user=user, move=self.move, status=status, r=rand, db=Namespace())
    
    @staticmethod
    def create_effect(move, effect_string):
        return Effect(move, eval(f"lambda *, target=None, user=None, move=None, status=None, r=None, db=None: ({effect_string})"))
