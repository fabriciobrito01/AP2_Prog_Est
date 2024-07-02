import random

from ...gui.cores import CORES

from ..personagem import Personagem

class Aventureiro(Personagem):
    def __init__(self, nome):
        self.forca = random.randint(10, 18)
        self.defesa = random.randint(10, 18)
        self.vida = random.randint(100, 120)
        self.posicao = [0, 0]

        self.chars = ["@", "#", "$"]
        self.cores = [CORES.branco, CORES.vermelho, CORES.verde, CORES.azul]
        self.char = "@"
        self.cor = CORES.branco

        self.nome = nome
        self.status = "Comece a explorar"
        self.rodada = 0

        self.xp = 0
        self.nivel = 1
        self.xp_por_nivel = 5



    def info(self):
        return {
            "classe": self.__class__.__name__,
            "forca": self.forca,
            "defesa": self.defesa,
            "vida": self.vida,
            "vida_max": self.vida_max,
            "posicao": self.posicao,
            "char": self.char,
            "cor": self.cor,
            "nome": self.nome,
            "status": self.status,
            "xp": self.xp,
            "nivel": self.nivel,
            "xp_por_nivel": self.xp_por_nivel,
            "rodada": self.rodada
        }

    def carregar(self, dados):
        self.forca = dados["forca"]
        self.defesa = dados["defesa"]
        self.vida = dados["vida"]
        self.vida_max = dados["vida_max"]
        self.posicao = dados["posicao"]
        self.char = dados["char"]
        self.cor = dados["cor"]
        self.status = dados["status"]
        self.xp = dados["xp"]
        self.nivel = dados["nivel"]
        self.xp_por_nivel = dados["xp_por_nivel"]
        self.rodada = dados["rodada"]

    def ganhar_xp(self, valor):
        self.xp += valor
        if self.xp >= self.xp_por_nivel:
            self.xp -= self.xp_por_nivel
            self.subir_nivel()


    def subir_nivel(self):
        self.nivel += 1
        self.xp_por_nivel += 1
        self.forca += 1
        self.defesa += 1
        self.vida += 20

        nvida = self.vida - self.vida_max
        if self.vida > self.vida_max:
            self.vida_max = self.vida_max + nvida

    def trocar_char(self):
        indice = self.chars.index(self.char) + 1
        if indice >= len(self.chars):
            indice = 0
        self.char = self.chars[indice]

    def trocar_cor(self):
        indice = self.cores.index(self.cor) + 1
        if indice >= len(self.cores):
            indice = 0
        self.cor = self.cores[indice]

    def andar(self, direcao):
        """
        Altera o valor da posição do aventureiro conforme a direção informada pelo
        usuário. Direções válidas:
        - W: cima
        - A: esquerda
        - S: baixo
        - D: direita

        Se o aventureiro estiver nos limites do mapa, não faz nenhum movimento.

        Considerar que o mapa é um sistema cartesiano, com o eixo x aumentando
        da esquerda para a direita, e o eixo y aumentando de cima para baixo.
        Portanto, as coordenadas (0, 0) estão no canto superior esquerdo do mapa,
        enquanto que as coordenadas (9, 9) estão no canto inferior direito.

        Retorna True caso o aventureiro tenha andado, e False caso contrário.
        """
        match direcao:
            case "W":
                if self.posicao[1] > 0:
                    self.posicao[1] -= 1
                    return True
            case "S":
                if self.posicao[1] < 9:
                    self.posicao[1] += 1
                    return True
            case "A":
                if self.posicao[0] > 0:
                    self.posicao[0] -= 1
                    return True
            case "D":
                if self.posicao[0] < 9:
                    self.posicao[0] += 1
                    return True

        return False

    def atacar(self):
        """
        Retorna um inteiro igual à Força do aventureiro, mais um valor aleatório
        entre 1 e 6.
        """
        return self.forca + random.randint(1, 6)

    def defender(self, dano, usar_defesa=True):
        """
        Calcula o dano a ser absorvido pelo aventureiro, igual ao dano causado
        menos o atributo de defesa do aventureiro.

        Se o dano a ser absorvido é menor ou igual a zero, não faz nada. Se for
        maior que zero, reduz esse dano da vida do aventureiro.
        """
        if usar_defesa:
            dano -= self.defesa
        if dano > 0:
            self.vida -= dano

    def esta_vivo(self):
        """
        Retorna True se a vida do aventureiro é maior que zero.
        """
        return self.vida > 0

    def __str__(self):
        return f"""Informações de {self.nome}:
Vida: {self.vida}
Força: {self.forca}
Defesa: {self.defesa}
"""
