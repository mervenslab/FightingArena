import random;

class Item:
    itemType = "";
    itemCharacteristics = {};

    def __init__(self, itemType):
        self.itemType = itemType;

        if self.itemType == "LifePotion":
            self.itemCharacteristics["LifeRegen"] = 15;