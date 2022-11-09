#Pokemon class
class Pokemon:
    def __init__(self,name,level,ptype,health,movelist,escapechance):
        self.name = name
        self.level = level
        self.type = ptype
        self.maxhealth = health
        self.temphealth = health
        self.moves = movelist
        self.escapechance = escapechance
        
