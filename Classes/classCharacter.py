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

class Monster(Character):
    monsterType = ""

    def __init__(self, monsterType):
        self.monsterType = monsterType
        if monsterType == "Orc":
            self.characterStrength = random.randrange(5,10,1)
            self.characterSpeed = random.randrange(4,9,1)
            self.characterIntelligence = random.randrange(1,6,1)
            self.characterLife = self.characterStrength*2+1
        if monsterType == "Oger":
            self.characterStrength = random.randrange(12,17,1)
            self.characterSpeed = random.randrange(2,7,1)
            self.characterIntelligence = random.randrange(0,3,1)
            self.characterLife = self.characterStrength*2+1
        if monsterType == "Goblin":
            self.characterStrength = random.randrange(1,5,1)
            self.characterSpeed = random.randrange(8,13,1)
            self.characterIntelligence = random.randrange(4,9,1)
            self.characterLife = self.characterStrength*2+1

    def getType(self):
        return self.monsterType
        
