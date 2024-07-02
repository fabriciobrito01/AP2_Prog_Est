import random

from .aventureiro import Aventureiro

class Paladino(Aventureiro):
    def __init__(self, nome):
        super().__init__(nome)
        self.defesa = random.randint(15, 25)
        self.vida = random.randint(120, 150)
        self.chars.append("P")
        self.char = "P"
        self.vida_max = self.vida
