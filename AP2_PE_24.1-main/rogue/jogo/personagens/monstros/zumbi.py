import random

from .inimigo import Inimigo

class Zumbi(Inimigo):
    def __init__(self):
        self.forca = random.randint(5, 15)
        self.vida = random.randint(10, 50)
        self.nome = "Zumbi"
        self.xp = 1
