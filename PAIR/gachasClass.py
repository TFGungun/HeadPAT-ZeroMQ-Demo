class character:
    def __init__(self, name: str = "PlaceholderName", rarity: int = 0):
        self.name: str = name
        self.rarity: int = rarity

    def print(self):
        return "" + str(self.name) + " (" + str(self.rarity) + "*)"


def defMaker():
    c_smolCat = character(name="Smoll Catto", rarity=1)
    c_mediumCat = character(name="Medium Catto", rarity=2)
    c_bigCat = character(name="Big Catto", rarity=3)
    c_lion = character(name="King Lion", rarity=4)
    c_tora = character(name="Tiger God", rarity=5)

    c_lizerd = character(name="Desert Lizerd", rarity=1)
    c_gila = character(name="Gila Monster", rarity=2)
    c_komodo = character(name="Komodo Drago", rarity=3)
    c_croco = character(name="Crocodile Gator", rarity=4)
    c_goji = character(name="GODZILLA", rarity=5)

    return [c_smolCat, c_mediumCat, c_bigCat, c_lion, c_tora, c_lizerd, c_gila, c_komodo, c_croco, c_goji]
