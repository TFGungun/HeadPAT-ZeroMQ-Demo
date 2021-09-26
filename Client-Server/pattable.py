class pattable:
    def __init__(self, name: str = "PlaceholderName"):
        self.name: str = name
        self.pattable_parts: list = []

    def addPattablePart(self, pattablePart: str):
        self.pattable_parts.append(pattablePart)


def makeDefpattables():
    parts = ["head", "tail", "paw", "muzzle",
             "wings", "horns", "spikes", "nose"]

    pattables = {}

    nergigante = pattable("Nergigante")
    nerg_pat_idx = [0, 1, 2, 3, 4, 5, 6]
    for idx in nerg_pat_idx:
        nergigante.addPattablePart(parts[idx])
    pattables[nergigante.name] = nergigante

    taiga = pattable("Tiger")
    taiga_pat_idx = [0, 1, 2, 3, 7]
    for idx in taiga_pat_idx:
        taiga.addPattablePart(parts[idx])
    pattables[taiga.name] = taiga

    catto = pattable("Cat")
    cat_pat_idx = [0, 1, 2, 3, 7]
    for idx in cat_pat_idx:
        catto.addPattablePart(parts[idx])
    pattables[catto.name] = catto

    slime = pattable("Elemental Slime")
    sli_pat_idx = [0]
    for idx in sli_pat_idx:
        slime.addPattablePart(parts[idx])
    pattables[slime.name] = slime

    return pattables
