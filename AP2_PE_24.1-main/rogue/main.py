from jogo.mecanicas.mecanicas import loop

import pygame

def iniciar_jogo():
    pygame.init()

def encerrar_jogo():
    print("Saindo do jogo!")
    pygame.quit()

def main():
    iniciar_jogo()
    loop()
    encerrar_jogo()

if __name__ == "__main__":
    main()
