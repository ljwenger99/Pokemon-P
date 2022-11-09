import random

#Pokemon move class
class Move:
    def __init__(self,name,ptype,damage,hitchance):
        self.name = name
        self.type = ptype
        self.damage = damage
        self.hitchance = hitchance
        
    def damagepokemon(self,attacker,defender):
        print(attacker.name + " used " + self.name)
        tempdamage = self.damage
        hitcheck = random.randint(0,100)
        if self.hitchance >= hitcheck: #hits
            if self.type == attacker.type: #STAB (Same-Type-Attack-Bonus)
                tempdamage = tempdamage * 1.2
            if defender.type.isweakto(self.type): #type advantage
                tempdamage = tempdamage * 1.2
                print("It's super effective!")
            if defender.type.isstrongagainst(self.type): #type disadvantage
                tempdamage = tempdamage * 0.8
                print("It's not very effective...")
            critchance = random.randint(0,100)
            if critchance >= 95: #critical hit
                tempdamage = tempdamage*1.5
                print("Critical hit!!!")
            tempdamage = int(round(tempdamage,0))
            defender.temphealth -= tempdamage
            print(defender.name + " took " + str(tempdamage) + " damage.")
        else: #doesn't hit
            print("The attack missed!")
