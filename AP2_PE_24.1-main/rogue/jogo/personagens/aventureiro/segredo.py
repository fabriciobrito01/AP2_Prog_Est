from .aventureiro import Aventureiro

class Segredo(Aventureiro):
    def __init__(self, nome):
        super().__init__(nome)
        self.forca = 30
        self.defesa = 30
        self.vida = 200
        self.chars.append("S")
        self.char = "S"
        self.vida_max = self.vida
