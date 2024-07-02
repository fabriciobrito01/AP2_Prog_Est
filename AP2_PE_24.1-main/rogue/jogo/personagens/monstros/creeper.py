import random

from .inimigo import Inimigo

class Creeper(Inimigo):
    def __init__(self):
        self.forca = random.randint(15, 25)
        self.vida = random.randint(10, 50)
        self.nome = "Creeper"
        self.xp = 3
