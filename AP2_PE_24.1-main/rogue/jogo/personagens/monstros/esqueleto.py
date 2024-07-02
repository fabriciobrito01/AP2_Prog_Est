import random

from .inimigo import Inimigo

class Esqueleto(Inimigo):
    def __init__(self):
        self.forca = random.randint(10, 15)
        self.vida = random.randint(30, 100)
        self.nome = "Esqueleto"
        self.xp = 2
