from constantes import COLUNAS, LABIRINTO, LINHAS


def eh_parede(linha, coluna):
    if 0 <= linha < LINHAS and 0 <= coluna < COLUNAS:
        return LABIRINTO[linha][coluna] == 1
    return True