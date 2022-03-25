import random;

class Character:
    characterStrength = 0
    characterSpeed = 0
    characterIntelligence = 0
    characterLife = 0

    def getStrength(self):
        return self.characterStrength
    
    def getSpeed(self):
        return self.characterSpeed

    def getIntelligence(self):
        return self.characterIntelligence

    def getLife(self):
        return self.characterLife

    def setLife(self, life):
        self.characterLife = life

class Hero(Character):
    heroClass = ""
    heroName = ""

    def __init__(self, heroClass):
        self.heroClass = heroClass
        
        if heroClass == "Warrior":
            self.characterStrength = random.randrange(8,15,1)
            self.characterSpeed = random.randrange(3,8,1)
            self.characterIntelligence = random.randrange(0,4,1)
            self.characterLife = self.characterStrength*2+1
        if heroClass == "Rogue":
            self.characterStrength = random.randrange(3,8,1)
            self.characterSpeed = random.randrange(8,13,1)
            self.characterIntelligence = random.randrange(3,8,1)
            self.characterLife = self.characterStrength*2+1
        if heroClass == "Mage":
            self.characterStrength = random.randrange(0,4,1)
            self.characterSpeed = random.randrange(3,8,1)
            self.characterIntelligence = random.randrange(8,13,1)
            self.characterLife = self.characterStrength*2+1