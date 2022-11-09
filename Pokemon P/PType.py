import random

#Pokemon type class
class PType:
    def __init__(self,name,strength,weakness):
        self.name = name
        self.strength = strength
        self.weakness = weakness
        
    def isweakto(self,other):
        if self.weakness == other:
            return True
        else:
            return False
        
    def isstrongagainst(self,other):
        if self.strength == other:
            return True
        else:
            return False

