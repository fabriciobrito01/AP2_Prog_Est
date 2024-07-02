import random

from .aventureiro import Aventureiro

class Guerreiro(Aventureiro):
    def __init__(self, nome):
        super().__init__(nome)
        self.forca = random.randint(15, 30)
        self.chars.append("G")
        self.char = "G"
        self.vida_max = self.vida
