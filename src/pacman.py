import pygame
from constantes import TAMANHO_CELULA, COR_AMARELO, LINHAS, COLUNAS, LABIRINTO
from utilitario import eh_parede

class Pacman:
    """Representa o jogador. Guarda a posição e sabe se mover no labirinto"""
    def __init__(self, linha, coluna):
        self.linha = linha
        self.coluna = coluna

    def posicao(self):
        return (self.linha, self.coluna)

    def desenhar(self, tela):
        centro_x = self.coluna * TAMANHO_CELULA + TAMANHO_CELULA // 2
        centro_y = self.linha * TAMANHO_CELULA + TAMANHO_CELULA // 2
        pygame.draw.circle(tela, COR_AMARELO, (centro_x, centro_y), TAMANHO_CELULA // 4)


    def mover(self, direcao):
        delta = {
            "cima": (0, -1),
            "baixo": (0, 1),
            "esquerda": (-1, 0),
            "direita": (1, 0)
        }

        d_coluna, d_linha = delta[direcao]
        nova_linha = self.linha + d_linha
        nova_coluna = self.coluna + d_coluna

        if not eh_parede(nova_linha, nova_coluna):
            self.linha = nova_linha
            self.coluna = nova_coluna 

    