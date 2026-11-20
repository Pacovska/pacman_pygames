import math

import pygame

LARGURA_TELA = 1600
ALTURA_TELA = 800
LARGURA_OBSTACULO = 400
ALTURA_OBSTACULO = 200

OBSTACULO = pygame.Rect(
    (LARGURA_TELA // 2) - (LARGURA_OBSTACULO // 2),
    (ALTURA_TELA // 2) - (ALTURA_OBSTACULO // 2),
    LARGURA_OBSTACULO,
    ALTURA_OBSTACULO
)

RAIO_PACMAN = 30
VELOCIDADE_PACMAN = 5

COR_VERMELHO = (255, 0, 0)
COR_VERDE = (0, 255, 0)
COR_AZUL = (0, 0, 255)
COR_AMARELO = (255, 255, 0)

FRAMES_DO_JOGO = 60


def criar_pacman():
    return {
        "x": 100,
        "y": 100,
        "olhando_x": 1,
        "olhando_y": 0
    }


def mover_pacman(pacman, teclas):
    x_inicial = pacman["x"]
    y_inicial = pacman["y"]

    if teclas[pygame.K_LEFT]:
        pacman["x"] -= VELOCIDADE_PACMAN
        pacman["olhando_x"], pacman["olhando_y"] = -1, 0
    if teclas[pygame.K_RIGHT]:
        pacman["x"] += VELOCIDADE_PACMAN
        pacman["olhando_x"], pacman["olhando_y"] = 1, 0
    if teclas[pygame.K_DOWN]:
        pacman["y"] += VELOCIDADE_PACMAN
        pacman["olhando_x"], pacman["olhando_y"] = 0, 1
    if teclas[pygame.K_UP]:
        pacman["y"] -= VELOCIDADE_PACMAN
        pacman["olhando_x"], pacman["olhando_y"] = 0, -1

    caixa = pygame.Rect(pacman["x"] - RAIO_PACMAN, pacman["y"] - RAIO_PACMAN, RAIO_PACMAN * 2, RAIO_PACMAN * 2)
    if caixa.colliderect(OBSTACULO):
        pacman["x"] = x_inicial
        pacman["y"] = y_inicial

    pacman["x"] = max(RAIO_PACMAN, min(LARGURA_TELA - RAIO_PACMAN, pacman["x"]))
    pacman["y"] = max(RAIO_PACMAN, min(ALTURA_TELA - RAIO_PACMAN, pacman["y"]))


def desenhar_pacman(tela, pacman):
    centro_x = int(pacman["x"])
    centro_y = int(pacman["y"])
    
    angulo_base = math.atan2(pacman["olhando_y"], pacman["olhando_x"])
    abertura = math.radians(22.5)
    
    angulo_inicio = angulo_base + abertura
    angulo_fim = angulo_base + (2 * math.pi - abertura)
    
    pontos = [(centro_x, centro_y)]
    passos = 20
    for i in range(passos + 1):
        angulo = angulo_inicio + (angulo_fim - angulo_inicio) * (i / passos)
        x = centro_x + int(RAIO_PACMAN * math.cos(angulo))
        y = centro_y + int(RAIO_PACMAN * math.sin(angulo))
        pontos.append((x, y))

    pygame.draw.polygon(tela, COR_VERDE, pontos)

def desenhar(tela, pacman):
    tela.fill((0, 0, 0))
    pygame.draw.rect(tela, COR_AZUL, OBSTACULO)
    desenhar_pacman(tela, pacman)
    pygame.display.flip()


def main():
    pygame.init()
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption("PACMAN")
    relogio = pygame.time.Clock()

    pacman = criar_pacman()
    rodando = True

    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        teclas = pygame.key.get_pressed()
        mover_pacman(pacman, teclas)
        desenhar(tela, pacman)

        relogio.tick(FRAMES_DO_JOGO)


if __name__ == "__main__":
    main()
