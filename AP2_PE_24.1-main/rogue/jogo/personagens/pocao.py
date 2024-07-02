import random

from ..gui.cores import CORES

from .personagem import Personagem


class Pocao(Personagem):
    def __init__(self, tesouro):
        while True:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            if not (x == y == 0):
                break
            if not (self.posicao == tesouro.posicao):
                break

        self.posicao = [x, y]
        self.char = "%"
        self.cor = CORES.verde
        self.cont = 0

    def alterar_posicao(self, nova_pos):
        self.posicao = nova_pos

    def carregar(self, dados):
        self.posicao = dados["posicao"]

    def info(self):
        return {"posicao": self.posicao}
    
    def resultado(self, aventureiro):
        impacto = random.choices(["Dobrar a vida", "Aumentar a força", "Aumenta a defesa"], [0.2, 0.4, 0.4])[0]
        if impacto == "Dobrar a vida":
            aventureiro.status = "Tomou uma poção que dobrou sua vida!"
            aventureiro.vida *= 2
            aventureiro.vida_max *= 2

        elif impacto == "Aumentar a força":
            aventureiro.status = "Tomou uma poção que aumentou em 15 sua força!"
            aventureiro.forca += 15

        elif impacto == "Aumentar a defesa":
            aventureiro.status = "Tomou uma poção que aumentou em 10 a sua defesa!"
            aventureiro.defesa += 10
        self.char = "·"
        impacto = []
        self.cor = CORES.branco
        self.cont += 1
