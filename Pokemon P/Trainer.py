import random

#Trainer class
class Trainer:
    def __init__(self,name,pokemon,healingitems,reward):
        self.name = name
        self.pokemon = pokemon
        self.healingitems = healingitems
        self.reward = reward

    def trainerturn(self,player):
        if self.pokemon.temphealth < .33*self.pokemon.maxhealth:
            for i in self.healingitems:
                if i.amount > 0:
                    print(self.name + " used a " + i.name + "!")
                    i.healpokemon(self.pokemon)
                    return
        movenum = random.randint(0,len(self.pokemon.moves)-1)
        self.pokemon.moves[movenum].damagepokemon(self.pokemon,player.active_pokemon)
