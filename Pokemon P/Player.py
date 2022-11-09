class Player:
    def __init__(self):
        self.active_pokemon = ''
        self.pokemon_list = []
        self.money = 0
        self.healing_items = []
        self.pokeball_bag = []
        
    def playerturn(self,enemy):
        action = ''
        print("\nWhat would you like to do?\n")
        print("1. Fight")
        print("2. Use Item")
        while action not in ['1','2']:
            action = input("\nEnter a number.\n")
        if action == '1':
            action = ''
            while action not in range(1,len(self.active_pokemon.moves)+2):
                for i in self.active_pokemon.moves:
                    print(str(self.active_pokemon.moves.index(i)+1) + ". " + i.name)
                print(str(self.active_pokemon.moves.index(i)+2) + ". " + "Return")
                while True:
                    try:
                        action = int(input("Which move would you like to use? Enter a number.\n"))
                        break
                    except ValueError:
                        continue
                if action in range(1,len(self.active_pokemon.moves)+1):
                    self.active_pokemon.moves[action-1].damagepokemon(self.active_pokemon,enemy)
                elif action == len(self.active_pokemon.moves)+1:
                    self.playerturn(enemy)
        elif action == '2':
            action = ''
            while action not in range(1,len(self.healing_items)+2):
                for i in self.healing_items:
                    print(str(self.healing_items.index(i)+1) + ". " + i.name + " -- x" + str(i.amount))
                print(str(self.healing_items.index(i)+2) + ". " + "Return")
                while True:
                    try:
                        action = int(input("Which healing item would you like to use? Enter a number.\n"))
                        break
                    except ValueError:
                        continue
                if action in range(1,len(self.healing_items)+1):
                    self.healing_items[action-1].healpokemon(self.active_pokemon)
                    if self.healing_items[action-1].amount == 0 or self.active_pokemon.temphealth == self.active_pokemon.maxhealth:
                        self.playerturn(enemy)
                elif action == len(self.healing_items)+1:
                    self.playerturn(enemy)

