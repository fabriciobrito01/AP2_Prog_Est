from .cores import CORES

import pygame

M = 10
LB = 150
AT = 20
AB = AT + 2 * M
A = AB + AT + 3 * M
L = 2 * LB + 3 * M

class MenuClasse:
    def __init__(self):
        self.display = pygame.display.set_mode((L, A))
        pygame.display.set_caption("Rogue")
        self.fonte = pygame.font.SysFont("Courier New", AT)

    @staticmethod
    def mapear_clique(pos):
        x, y = pos

        if M <= x <= M + LB and 2 * M + AT <= y <= 2 * M + AT + AB:
            return "Guerreiro"

        if 2 * M + LB <= x <= 2 * M + 2 * LB and 2 * M + AT <= y <= 2 * M + AT + AB:
            return "Paladino"

        return ""

    def renderizar(self):
        self.display.fill(CORES.preto)

        texto = self.fonte.render("Agora, escolha sua classe:", True, CORES.branco)
        self.display.blit(texto, [M, M])

        rect = pygame.Rect(M, 2 * M + AT, LB, AB)
        pygame.draw.rect(self.display, CORES.branco, rect)

        texto = self.fonte.render("Guerreiro", True, CORES.preto)
        self.display.blit(texto, [M + (LB - texto.get_width()) // 2, 3 * M + AT])

        rect = pygame.Rect(2 * M + LB, 2 * M + AT, LB, AB)
        pygame.draw.rect(self.display, CORES.branco, rect)

        texto = self.fonte.render("Paladino", True, CORES.preto)
        self.display.blit(texto, [2 * M + LB + (LB - texto.get_width()) // 2, 3 * M + AT])

        pygame.display.update()
