import pygame

from constantes import TAMANHO_CELULA


class Fantasma:
    def __init__(self, linha, coluna, cor):
        self.linha = linha
        self.coluna = coluna
        self.cor = cor
        self._direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]


    def posicao(self):
        return(self.linha, self.coluna)

    def mover(self, pacman):
        raise NotImplementedError("Subclasse deve implementar mover()")

    def desenhar(self, tela):
        centro_x = self.coluna * TAMANHO_CELULA + TAMANHO_CELULA //2 
        centro_y = self.linha * TAMANHO_CELULA + TAMANHO_CELULA //2 
        pygame.draw.circle(tela, self.cor, (centro_x, centro_y), TAMANHO_CELULA // 4)