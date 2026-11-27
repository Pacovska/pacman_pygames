from fantasma import Fantasma
from utilitario import eh_parede


class FantasmaPerseguidor(Fantasma):

    def mover(self, pacman):
        melhor_direcao = None
        menor_distancia = None
        for direcao_linha, direcao_coluna in self._direcoes:
            nova_linha, nova_coluna = self.linha + direcao_linha, self.coluna + direcao_coluna
            if eh_parede(nova_linha, nova_coluna):
                continue
            distancia = abs(nova_linha - pacman.linha) + abs(nova_coluna - pacman.coluna)
            if menor_distancia is None or distancia < menor_distancia:
                menor_distancia = distancia
                melhor_direcao = (nova_linha, nova_coluna)
        if melhor_direcao:
            self.linha, self.coluna = melhor_direcao