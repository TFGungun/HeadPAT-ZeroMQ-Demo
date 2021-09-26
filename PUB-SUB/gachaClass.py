class character:
    def __init__(self, name: str = "PlaceholderName", rarity: int = 0):
        self.name: str = name
        self.rarity: int = rarity

    def print(self):
        return "" + str(self.name) + " (" + str(self.rarity) + "*)"


class banner:
    def __init__(self, name: str = "NoBannerName"):
        self.name: str = name
        self.characters: list = []
        self.drop_rate: list = []

    def addChar(self, character: character, drop_rate: float):
        self.characters.append(character)
        self.drop_rate.append(drop_rate)

    def printBanner(self):
        print("Banner Name : ", self.name)
        for i in range(len(self.characters)):
            print(self.characters[i].print(),
                  " drop rate : ", self.drop_rate[i])


def defBannersMaker():
    c_smolCat = character(name="Smoll Catto", rarity=1)
    c_mediumCat = character(name="Medium Catto", rarity=2)
    c_bigCat = character(name="Big Catto", rarity=3)
    c_lion = character(name="King Lion", rarity=4)
    c_tora = character(name="Tiger God", rarity=5)

    b_cattos = banner("The Cat Lovers' Banner")
    b_cattos.addChar(c_smolCat, 0.35)
    b_cattos.addChar(c_mediumCat, 0.25)
    b_cattos.addChar(c_bigCat, 0.20)
    b_cattos.addChar(c_lion, 0.15)
    b_cattos.addChar(c_tora, 0.05)

    c_lizerd = character(name="Desert Lizerd", rarity=1)
    c_gila = character(name="Gila Monster", rarity=2)
    c_komodo = character(name="Komodo Drago", rarity=3)
    c_croco = character(name="Crocodile Gator", rarity=4)
    c_goji = character(name="GODZILLA", rarity=5)

    b_lizards = banner("The Lizards of Insanity Banner")
    b_lizards.addChar(c_lizerd, 0.36)
    b_lizards.addChar(c_gila, 0.24)
    b_lizards.addChar(c_komodo, 0.21)
    b_lizards.addChar(c_croco, 0.14)
    b_lizards.addChar(c_goji, 0.05)

    return [b_cattos, b_lizards]
