from .cores import CORES

import pygame

L = 450
M = 10
AT = 20
LR = L - 2 * M
AR = AT + 2 * M
A = AR + 3 * M + AT

class InputBox:
    def __init__(self) -> None:
        self.display = pygame.display.set_mode((L, A))
        pygame.display.set_caption("Rogue")
        self.fonte = pygame.font.SysFont("Courier New", AT)

    def renderizar(self, resposta):
        self.display.fill(CORES.preto)

        texto = self.fonte.render("Informe o seu nome:", True, CORES.branco)
        self.display.blit(texto, [M, M])

        texto = self.fonte.render(resposta, True, CORES.branco)
        self.display.blit(texto, [2 * M, 3 * M + AT])

        rect = pygame.Rect(M, 2 * M + AT, LR, AR)
        pygame.draw.rect(self.display, CORES.branco, rect, 3)

        pygame.display.update()
