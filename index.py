import readline
import random
from pokemon import Pokemon, pokemonDb

class Player:
    def __init__(self, name, pokemon):
        self.name = name
        self.pokemon = pokemon

        print(f"{self.name} chose {self.pokemon.name}!")
    
    chose_move = lambda self: None # returns a Move

    def __str__(self):
        return self.name

class UserPlayer(Player):
    def __init__(self):
        name = input("What is your name? ")
        #pokemon = Pokemon(random.choice(pokemonDb))
        # Using the charmander for testing
        pokemon = Pokemon(pokemonDb[1])
        super().__init__(name, pokemon)

    def choose_move(self):
        move_names = [move.name.lower() for move in self.pokemon.moves]
        move_name = input(f"What move should {self.pokemon.name} use?\nChoose one of: {', '.join(map(lambda x:x.upper(), move_names))}? ").lower()
        if move_name in move_names:
            return self.pokemon.moves[move_names.index(move_name)]
        else:
            print("Invalid move")
            return self.choose_move()

class Computer(Player):
    def __init__(self):
        pokemon = Pokemon(random.choice(pokemonDb))
        super().__init__("Computer", pokemon)
    
    def choose_move(self):
        return random.choice(self.pokemon.moves)

class Game:
    def __init__(self):
        self.player = UserPlayer()
        self.computer = Computer()
        self.turn = 0
        self.winner = None
    
    def play_turn(self):
        self.turn += 1
        print("---")
        print(f"Turn {self.turn}")
        self.player_turn(self.player)
        if not self.computer.pokemon.is_alive():
            return
        self.player_turn(self.computer)
    
    def player_turn(self, player):
        opponent = self.computer if player == self.player else self.player
        player.pokemon.use_move(player.choose_move(), opponent.pokemon)
        if not opponent.pokemon.is_alive():
            self.winner = player
            return
        player.pokemon.turn()
    
    def summery(self):
        print(f"{self.player.name}'s {self.player.pokemon.name} has {self.player.pokemon.hp} HP left.")
        print(f"{self.computer.name}'s {self.computer.pokemon.name} has {self.computer.pokemon.hp} HP left.")
    
    def play(self):
        while self.winner == None:
            self.summery()
            self.play_turn()
        print(f"{self.winner.name} wins!")

if __name__ == "__main__":
    game = Game()
    try:
        game.play()
    except KeyboardInterrupt:
        print("\nGot away safely!")
