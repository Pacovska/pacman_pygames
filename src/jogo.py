import pygame
from pacman import Pacman
from constantes import LINHAS, COLUNAS, LABIRINTO, TAMANHO_CELULA, COR_AZUL, COR_BRANCO, PONTOS_POR_PELLETS, COR_VERDE, PONTOS_POR_SUPER_PELLETS
import random

class Jogo:
    """
      A função é responsável por desenhar o objeto de pontuação no 
    Controla o estado geral da partida: pontuação, pellets restantes. 
    A pontuação é "privado" (self._pontuacao) e só pode ser lido de fora através
    da propriedade "pontuacao".
    """

    def __init__(self):
        self.pacman = Pacman(1,1)
        self.pellets = self.criar_pellets()
        self.super_pellets = self.criar_super_pellets()
        self._pontuacao = 0

    @property
    def pontuacao(self):
        return self._pontuacao

    def atualizar(self):
        posicao_atual = self.pacman.posicao()
        if posicao_atual in self.pellets:
            self.pellets.remove(posicao_atual)
            self._pontuacao += PONTOS_POR_PELLETS
        elif posicao_atual in self.super_pellets:
            self.super_pellets.remove(posicao_atual)
            self._pontuacao += PONTOS_POR_SUPER_PELLETS

    def desenhar_labirinto(self, tela):
        """
                A função é responsável por desenhar o objeto de pontuação no mapa
                """
        for linha in range(LINHAS):
            for coluna in range(COLUNAS):
                if LABIRINTO[linha][coluna] == 1:
                    retangulo = pygame.Rect(
                        coluna * TAMANHO_CELULA,
                        linha * TAMANHO_CELULA,
                        TAMANHO_CELULA,
                        TAMANHO_CELULA
                    )
                    pygame.draw.rect(tela, COR_AZUL, retangulo)

    def criar_pellets(self):
        pellets = {
            (linha, coluna)
            for linha in range(LINHAS)
            for coluna in range(COLUNAS)
            if LABIRINTO[linha][coluna] == 0
        }

        pellets.remove(self.pacman.posicao())

        return pellets

    def criar_super_pellets(self):
        super_pellets = random.sample(list(self.pellets), 4)
        for pellet in super_pellets:
            self.pellets.remove(pellet)

        return super_pellets
        

    def desenhar_pellets(self, tela):
        """
        A função é responsável por desenhar o objeto de pontuação no mapa
        """
        for linha, coluna in self.pellets:
            centro_x = coluna * TAMANHO_CELULA + TAMANHO_CELULA // 2
            centro_y = linha * TAMANHO_CELULA + TAMANHO_CELULA // 2
            pygame.draw.circle(tela, COR_BRANCO, (centro_x, centro_y), TAMANHO_CELULA // 10)

    def desenha_super_pellets(self, tela):
        for linha, coluna in self.super_pellets:
            centro_x = coluna * TAMANHO_CELULA + TAMANHO_CELULA // 2
            centro_y = linha * TAMANHO_CELULA + TAMANHO_CELULA // 2
            pygame.draw.circle(tela, COR_VERDE, (centro_x, centro_y), TAMANHO_CELULA // 6)
        

    def venceu(self):
        """
                A função é responsável por desenhar o objeto de pontuação no mapa
                """
        return len(self.pellets) == 0