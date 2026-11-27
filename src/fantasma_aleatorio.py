import random

from fantasma import Fantasma
from utilitario import eh_parede


class FantasmaAleatorio(Fantasma):

    def mover(self, pacman):
        random.shuffle(self._direcoes)

        for direcao_linha, direcao_coluna in self._direcoes:
            nova_linha, nova_coluna = self.linha + direcao_linha, self.coluna + direcao_coluna
            if not eh_parede(nova_linha, nova_coluna):
                self.linha, self.coluna = nova_linha, nova_coluna
                break
