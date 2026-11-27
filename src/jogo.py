import json

import pygame
from fantasma_aleatorio import FantasmaAleatorio
from fantasma_perseguidor import FantasmaPerseguidor
from pacman import Pacman
from constantes import ARQUIVO_RECORDE, COR_FANTASMA_PERSEGUIDOR, COR_VERMELHO, LINHAS, COLUNAS, LABIRINTO, TAMANHO_CELULA, COR_AZUL, COR_BRANCO, PONTOS_POR_PELLETS, COR_VERDE, PONTOS_POR_SUPER_PELLETS, VIDAS_INICIAIS, COR_FANTASMA_ALEATORIO
import random

class SemVidasError(Exception):
    """Exceção personalizada lançada quando o jogador perde todas as vidas"""

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
        self.pellets_vida = self.criar_pellets_vida()
        self._pontuacao = 0
        self._vidas = VIDAS_INICIAIS

        self.recorde = self.carregar_recorde()

        self.fantasmas = [
            FantasmaAleatorio(5, 7, COR_FANTASMA_ALEATORIO),
            FantasmaPerseguidor(1, 8, COR_FANTASMA_PERSEGUIDOR)
        ]

        self.contador = 0


    @property
    def pontuacao(self):
        return self._pontuacao

    @property
    def vidas(self):
        return self._vidas

    def atualizar(self):
        posicao_atual = self.pacman.posicao()
        if posicao_atual in self.pellets:
            self.pellets.remove(posicao_atual)
            self._pontuacao += PONTOS_POR_PELLETS
        elif posicao_atual in self.super_pellets:
            self.super_pellets.remove(posicao_atual)
            self._pontuacao += PONTOS_POR_SUPER_PELLETS
        elif posicao_atual in self.pellets_vida:
            self.pellets_vida.remove(posicao_atual)
            if self._vidas != VIDAS_INICIAIS:
                self._vidas += 1

        self.contador += 1
        if self.contador % 15 == 0:
            for fantasma in self.fantasmas:
                fantasma.mover(self.pacman)

        for fantasma in self.fantasmas:
            if fantasma.posicao() == self.pacman.posicao():
                fantasma.linha, fantasma.coluna = 1, 8
                self.perde_vida()

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

    def criar_pellets_vida(self):
        pellets_vida = random.sample(list(self.pellets), 1)
        for pellet in pellets_vida:
            self.pellets.remove(pellet)

        return pellets_vida
        

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

    def desenha_pellets_vida(self, tela):
        for linha, coluna in self.pellets_vida:
            centro_x = coluna * TAMANHO_CELULA + TAMANHO_CELULA // 2
            centro_y = linha * TAMANHO_CELULA + TAMANHO_CELULA // 2
            pygame.draw.circle(tela, COR_VERMELHO, (centro_x, centro_y), TAMANHO_CELULA // 6)

    def perde_vida(self):
        self._vidas -= 1
        self.pacman.linha, self.pacman.coluna = 1, 1
        if self._vidas == 0:
            raise SemVidasError("O jogador perdeu todas as vidas!")

    def salvar_recorde(self):
        with open(ARQUIVO_RECORDE, "w", encoding="utf-8") as arquivo:
            json.dump({"recorde": self._pontuacao}, arquivo)

    def carregar_recorde(self):
        try:
            with open(ARQUIVO_RECORDE, "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
                return(dados.get("recorde", 0))
        except FileNotFoundError:
            return 0

    def venceu(self):
        """
                A função é responsável por desenhar o objeto de pontuação no mapa
                """
        return len(self.pellets) == 0