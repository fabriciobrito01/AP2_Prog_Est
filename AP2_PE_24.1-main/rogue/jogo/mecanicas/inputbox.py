from ..gui.inputbox import InputBox

import pygame

def ler_texto():
    inputbox = InputBox()

    resposta = ""
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return "Sem nome"

            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_RETURN:
                    return resposta

                if evento.key == pygame.K_BACKSPACE:
                    resposta = resposta[:-1]
                elif len(resposta) < 25:
                    resposta += evento.unicode

        inputbox.renderizar(resposta)
