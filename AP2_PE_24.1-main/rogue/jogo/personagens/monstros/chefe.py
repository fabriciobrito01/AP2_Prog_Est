import random

from .inimigo import Inimigo

class Chefe(Inimigo):
    def __init__(self):
        self.vida = random.randint(50, 120)
        self.forca = random.randint(15, 30)
        self.defesa = random.randint(1, 6)
        self.nome = "Chefe"
        self.xp = 5

    def defender(self, dano):
        dano -= self.defesa
        if dano > 0:
            self.vida -= dano
