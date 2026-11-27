import pygame

from constantes import ALTURA_TELA, ARQUIVO_RECORDE, COR_PRETO, FRAMES_DO_JOGO, LARGURA_TELA, COR_BRANCO
from jogo import Jogo, SemVidasError

def desenhar(tela, jogo, fonte):
    tela.fill(COR_PRETO)
    jogo.desenhar_labirinto(tela)
    jogo.desenhar_pellets(tela)
    jogo.desenha_super_pellets(tela)
    jogo.desenha_pellets_vida(tela)
    jogo.pacman.desenhar(tela)
    for fantasma in jogo.fantasmas:
        fantasma.desenhar(tela)
    texto = fonte.render(f"Pontos: {jogo.pontuacao:04d} Vidas: {jogo.vidas} Recorde: {jogo.recorde}",True, COR_BRANCO)
    tela.blit(texto, (10, ALTURA_TELA - 32))
    pygame.display.flip()


def main():
    pygame.init()
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption("PACMAN")
    relogio = pygame.time.Clock()
    fonte = pygame.font.SysFont(None, 32)

    jogo = Jogo()
    rodando = True

    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    jogo.pacman.mover("esquerda")
                elif evento.key == pygame.K_RIGHT:
                    jogo.pacman.mover("direita")
                elif evento.key == pygame.K_UP:
                    jogo.pacman.mover("cima")
                elif evento.key == pygame.K_DOWN:
                    jogo.pacman.mover("baixo")

        try:
            jogo.atualizar()
        except SemVidasError:
            print(f"Fim de jogo! Pontuação: {jogo.pontuacao}")
            if jogo.pontuacao > jogo.recorde:
                jogo.salvar_recorde()
                print(f"Novo recorde salvo em {ARQUIVO_RECORDE}")
        desenhar(tela, jogo, fonte)

        if jogo.venceu():
            print(f"Você venceu! Pontuação final {jogo.pontuacao}")
            if jogo.pontuacao > jogo.recorde:
                jogo.salvar_recorde()
                print(f"Novo recorde salvo em {ARQUIVO_RECORDE}")
            rodando = False

        relogio.tick(FRAMES_DO_JOGO)

    pygame.quit()

if __name__ == "__main__":
    main()
