import random

class Inimigo:
    def __init__(self):
        """
        Inicia um novo monstro, retornando um dicionário com as seguintes chaves
        e valores:

        - forca: Um valor aleatório entre 5 e 25
        - vida: um valor aleatório entre 10 e 100

        Antes de retornar o dicionário, exibe na tela a mensagem "Um novo monstro
        apareceu!".
        """
        self.forca = random.randint(5, 25)
        self.vida = random.randint(10, 100)
        self.nome = "Monstro"
        self.xp = 1

    def atacar(self):
        """
        Retorna o dano do monstro, igual ao seu atributo de força.
        """
        return self.forca

    def defender(self, dano):
        """
        Reduz o dano causado da vida do monstro.
        """
        self.vida -= dano

    def esta_vivo(self):
        """
        Retorna True se a vida do monstro é maior que zero.
        """
        return self.vida > 0
