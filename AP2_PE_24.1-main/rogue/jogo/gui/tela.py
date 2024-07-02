from .cores import CORES

import pygame

GRID = 40
LARGURA = 10 * GRID + 350
ALTURA = 10 * GRID + 100
MARGEM = 10
FONTE = "Courier New"

def centralizar_grid(texto, posicao_inicial):
    x = (LARGURA - 10 * GRID) // 2 + posicao_inicial[0] + (GRID - texto.get_width()) // 2
    y = (ALTURA - 10 * GRID) // 2 + posicao_inicial[1] + (GRID - texto.get_height()) // 2
    return [x, y]

class Tela:
    def __init__(self):
        self.display = pygame.display.set_mode((LARGURA, ALTURA))
        pygame.display.set_caption("Rogue")
        self.fonte_grid = pygame.font.SysFont(FONTE, GRID)
        self.fonte_msg = pygame.font.SysFont(FONTE, GRID // 2)
        self.fonte_rodada = pygame.font.SysFont(FONTE, GRID // 2)

    def renderizar(self, aventureiro, tesouro, pocao):
        self.display.fill(CORES.preto)
        self.personagem(aventureiro, aventureiro.cor)
        self.personagem(tesouro, tesouro.cor)
        self.personagem(pocao, pocao.cor)
        self.atributos(aventureiro)
        self.status(aventureiro.status)
        self.rodadas(aventureiro.rodada)
        self.mapa(aventureiro, tesouro, pocao)

        pygame.display.update()

    def status(self, mensagem):
        texto = self.fonte_msg.render(mensagem, True, CORES.branco)
        self.display.blit(texto, [MARGEM, MARGEM])

    def rodadas(self, rodada):
        texto = self.fonte_rodada.render(str(rodada), True, CORES.branco)
        self.display.blit(texto, [LARGURA-MARGEM - texto.get_width() , 0])


    def atributos(self, aventureiro):
        mensagem = f"{aventureiro.nome} nv {aventureiro.nivel}: XP({aventureiro.xp}/{aventureiro.xp_por_nivel}) - " \
            f"Vida {aventureiro.vida}/{aventureiro.vida_max} - Força {aventureiro.forca} - Defesa {aventureiro.defesa}"
        texto = self.fonte_msg.render(mensagem, True, CORES.branco)
        text_rect = texto.get_rect()
        text_rect.centerx = self.display.get_rect().centerx
        text_rect.bottom = self.display.get_rect().bottom - MARGEM
        self.display.blit(texto, text_rect)

    def mapa(self, aventureiro, tesouro, pocao):
        texto = self.fonte_grid.render("·", True, CORES.branco)
        for linha in range(10):
            for coluna in range(10):
                if [linha, coluna] not in [aventureiro.posicao, tesouro.posicao, pocao.posicao]:
                    self.display.blit(texto, centralizar_grid(texto, [linha * GRID, coluna * GRID]))
    
    def personagem(self, personagem, cor=CORES.branco):
        # renderização do texto
        texto = self.fonte_grid.render(personagem.char, True, cor)
        # inserir o render na tela
        x = personagem.posicao[0] * GRID
        y = personagem.posicao[1] * GRID
        self.display.blit(texto, centralizar_grid(texto, [x, y]))
