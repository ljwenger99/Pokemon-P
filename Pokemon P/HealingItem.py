#Healing item class
class HealingItem:
    def __init__(self,name,plural,cost,amount,healing):
        self.name = name
        self.plural = plural
        self.cost = cost
        self.amount = amount
        self.healing = healing

    def healpokemon(self,pokemon):
        totaldamage = pokemon.maxhealth - pokemon.temphealth
        if self.amount == 0:
            print("You are out of " + self.plural + "!")
        elif totaldamage == 0:
            print(pokemon.name + " is already at full health!")
        elif totaldamage < self.healing:
            pokemon.temphealth = pokemon.maxhealth
            self.amount -= 1
            print(pokemon.name + " was healed " + str(totaldamage) + " hp.")
        else:
            pokemon.temphealth += self.healing
            self.amount -= 1
            print(pokemon.name + " was healed " + str(self.healing) + " hp.")
