import math

import pygame

LARGURA_TELA = 700
ALTURA_TELA = 600

RAIO_PACMAN = 15
VELOCIDADE_PACMAN = 1

COR_VERMELHO = (255, 0, 0)
COR_VERDE = (0, 255, 0)
COR_AZUL = (0, 0, 255)
COR_AMARELO = (255, 255, 0)
COR_PRETO = (0, 0, 0)

FRAMES_DO_JOGO = 60

# 1 = PAREDE e 0 = ESPAÇO LIVRE
# LABIRINTO = [
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
#     [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
#     [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
#     [1, 0, 0, 1, 1, 1, 0, 0, 0, 1],
#     [1, 1, 0, 0, 0, 1, 1, 0, 1, 1],
#     [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
#     [1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
#     [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
# ]
# LABIRINTO = [
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
#     [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
#     [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
#     [1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
# ]
# LABIRINTO = [
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
#     [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
#     [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
#     [1, 0, 1, 1, 0, 0, 1, 1, 0, 1],
#     [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
#     [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
#     [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
# ]

# LABIRINTO = [
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
#     [1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1],
#     [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
#     [1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
#     [1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1],
#     [1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
#     [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1],
#     [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
#     [1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1],
#     [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#     [1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#     [1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
# ]
LABIRINTO = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
LINHAS = len(LABIRINTO)
COLUNAS = len(LABIRINTO[0])

LARGURA_CELULA = LARGURA_TELA / COLUNAS
ALTURA_CELULA = ALTURA_TELA / LINHAS

TAMANHO_CELULA = min(LARGURA_CELULA, ALTURA_CELULA)

def eh_parede(linha, coluna):
    if 0 <= linha < LINHAS and 0 <= coluna < COLUNAS:
        return LABIRINTO[linha][coluna] == 1
    return True

def desenhar_labirinto(tela):
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

def criar_pacman():
    return {
        "linha": 1,
        "coluna": 1,
    }


def mover_pacman(pacman, direcao):
    delta = {
        "cima": (0, -1),
        "baixo": (0, 1),
        "esquerda": (-1, 0),
        "direita": (1, 0)
    }

    d_coluna, d_linha = delta[direcao]
    nova_linha = pacman["linha"] + d_linha
    nova_coluna = pacman["coluna"] + d_coluna

    if not eh_parede(nova_linha, nova_coluna):
        pacman["linha"] = nova_linha
        pacman["coluna"] = nova_coluna    

def desenhar_pacman(tela, pacman):
    centro_x = pacman["coluna"] * TAMANHO_CELULA + TAMANHO_CELULA // 2
    centro_y = pacman["linha"] * TAMANHO_CELULA + TAMANHO_CELULA // 2

    pygame.draw.circle(tela, COR_AMARELO, (centro_x, centro_y), TAMANHO_CELULA // 4)

def desenhar(tela, pacman):
    tela.fill(COR_PRETO)
    desenhar_labirinto(tela)
    desenhar_pacman(tela, pacman)
    pygame.display.flip()


def main():
    pygame.init()
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption("PACMAN")
    relogio = pygame.time.Clock()

    pacman = criar_pacman()
    rodando = True

    for linha in range(LINHAS):
        for coluna in range(COLUNAS):
            print(LABIRINTO[linha][coluna], end=" ")
        print()

    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    mover_pacman(pacman, "esquerda")
                elif evento.key == pygame.K_RIGHT:
                    mover_pacman(pacman, "direita")
                elif evento.key == pygame.K_UP:
                    mover_pacman(pacman, "cima")
                elif evento.key == pygame.K_DOWN:
                    mover_pacman(pacman, "baixo")

        desenhar(tela, pacman)
    


        relogio.tick(FRAMES_DO_JOGO)


if __name__ == "__main__":
    main()
