import pygame.mixer
from BaseParaJogo import *
import random

CORFUNDOJANELA = (0, 0, 0)
LARGURAJANELA = 800
ALTURAJANELA = 640
ICONE = "Recursos/Imagens/icone.png"

MAPA = [
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],   
[1,0,0,0,1,0,0,0,2,2,2,2,2,2,0,0,0,0,0,0,1,0,0,0,1],
[1,0,1,0,1,0,1,1,1,0,1,1,1,1,1,0,1,1,1,0,1,0,1,0,1],
[1,0,0,2,2,2,0,0,1,0,0,0,1,0,0,0,1,0,2,2,2,2,0,0,1],
[1,1,1,0,1,1,1,0,0,0,1,0,0,0,1,0,0,0,1,1,1,0,1,1,1],
[1,0,0,0,0,0,1,0,1,1,1,1,0,1,1,1,1,0,1,0,2,2,2,2,1],
[1,2,1,1,1,0,1,0,0,2,2,2,2,2,0,0,0,0,1,0,1,1,1,0,1],
[1,2,0,2,0,0,1,1,0,1,1,1,1,1,1,1,0,1,1,0,0,2,2,2,1],
[1,2,1,2,1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,1,0,1,0,1],
[1,2,1,2,1,1,0,1,1,1,1,0,1,0,1,1,1,1,0,1,1,0,1,0,1],
[1,2,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,2,1,0,1],
[1,0,0,0,1,0,1,1,0,1,1,1,1,1,1,1,0,1,1,0,1,2,0,0,1],
[1,0,1,0,1,0,0,0,0,2,2,2,0,0,0,2,2,0,0,0,1,2,1,0,1],
[1,1,1,0,1,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,1,2,1,1,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,0,0,0,2,0,0,1],
[1,0,1,0,1,0,1,1,1,1,0,1,1,1,0,1,1,1,1,0,1,0,1,0,1],
[1,0,0,0,1,0,2,2,2,0,0,0,0,0,2,2,2,2,0,0,1,0,0,0,1],
[1,0,1,0,1,0,1,1,1,0,1,1,1,1,1,0,1,1,1,0,1,0,1,0,1],
[1,0,0,0,1,0,0,0,0,2,2,2,2,0,0,0,0,0,0,0,1,0,0,0,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

def desenhaMapa(parede, pilula, pos_pacman):
    for l in range(len(MAPA)):
        for c in range(len(MAPA[l])):
            if MAPA[l][c] == 1:
                desenhaImagem(parede, c*32, l*32)
            elif MAPA[l][c] == 2:
                desenhaImagem(pilula, c*32, l*32)
            elif MAPA[l][c] == 0: # Nota foi comida
                continue
            elif MAPA[l][c] == 9: # Posicao do pacman
                continue
def posicaoValida(x, y):
    # Converte as coordenadas para índices do mapa
    coluna_esquerda = x // 32
    coluna_direita = (x + 32 - 1) // 32  # Largura do Pacman é 32
    linha_cima = y // 32
    linha_baixo = (y + 32 - 1) // 32  # Altura do Pacman é 32

    # Verifica se todas as posições do retângulo não colidem com as paredes
    for linha in range(linha_cima, linha_baixo + 1):
        for coluna in range(coluna_esquerda, coluna_direita + 1):
            if MAPA[linha][coluna] == 1:
                return False
    return True

def movimentoAleatorio(x, y, velocidade):
    direcao = random.choice([K_UP, K_DOWN, K_LEFT, K_RIGHT])
    if direcao == K_UP and posicaoValida(x, y - velocidade):
        y -= velocidade
    elif direcao == K_DOWN and posicaoValida(x, y + velocidade):
        y += velocidade
    elif direcao == K_LEFT and posicaoValida(x - velocidade, y):
        x -= velocidade
    elif direcao == K_RIGHT and posicaoValida(x + velocidade, y):
        x += velocidade
    return x, y

def main():
    criaJanela(LARGURAJANELA, ALTURAJANELA, "Pac-Man", CORFUNDOJANELA, ICONE)

    parede = carregaImagem("Recursos/Imagens/parede.png", (32, 32))
    pacman = carregaImagem("Recursos/Imagens/PacMan Icon/pacman.png", (32, 32))
    mozart = carregaImagem("Recursos/Imagens/Fantasmas/mozart.png", (32, 32))
    elvis = carregaImagem("Recursos/Imagens/Fantasmas/elvis.png", (32, 32))

    nota = carregaImagem("Recursos/Imagens/nota.png", (32, 32))
    total_points = 580

    xPacman = 384
    yPacman = 384
    velocidade_pacman = 4
    velocidade_fantasma = 2

    xMozart = 256
    yMozart = 256

    xElvis = 576
    yElvis = 576

    som_A = pygame.mixer.Sound("Recursos/Sons/Notas Musicais/A.mp3")
    som_morte = pygame.mixer.Sound("Recursos/Sons/pacman_death.wav")

    pygame.mixer.music.load("Recursos/Sons/Musicas/Long Gaze.mp3")
    pygame.mixer.init()
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)  # O argumento -1 faz com que a música seja reproduzida em um loop contínuo

    pontuacao = 0
    while True:
        if teclaPressionada(K_ESCAPE):
            break

        #Limpa a janela
        limpaTela()

        # Verifica se uma das teclas foi pressionada
        if teclaPressionada(K_UP) and posicaoValida(xPacman, yPacman - velocidade_pacman):
            pacman = carregaImagem("Recursos/Imagens/PacMan Icon/pacman_up.png", (32, 32))
            yPacman -= 4
        elif teclaPressionada(K_DOWN) and posicaoValida(xPacman, yPacman + velocidade_pacman):
            pacman = carregaImagem("Recursos/Imagens/PacMan Icon/pacman_down.png", (32, 32))
            yPacman += 4
        elif teclaPressionada(K_LEFT) and posicaoValida(xPacman - velocidade_pacman, yPacman):
            pacman = carregaImagem("Recursos/Imagens/PacMan Icon/pacman.png", (32, 32))
            xPacman -= 4
        elif teclaPressionada(K_RIGHT) and posicaoValida(xPacman + velocidade_pacman, yPacman):
            pacman = carregaImagem("Recursos/Imagens/PacMan Icon/pacman_right.png", (32, 32))
            xPacman += 4

        # Movimento aleatório de Mozart
        #xMozart, yMozart = movimentoAleatorio(xMozart, yMozart, velocidade_fantasma)

        # Movimento aleatório de Elvis
        #xElvis, yElvis = movimentoAleatorio(xElvis, yElvis, velocidade_fantasma)

        # Verifica se Mozart ou Elvis encontraram o Pacman
        if (xPacman, yPacman) == (xMozart, yMozart) or (xPacman, yPacman) == (xElvis, yElvis):
            som_morte.play()
            pygame.time.delay(2000)
            mensagem = "Você perdeu! Os fantasmas te pegaram."
            desenhaTexto(mensagem, LARGURAJANELA // 2, ALTURAJANELA // 2, 40, pygame.Color("red"))
            atualizaTelaJogo()
            pygame.time.delay(5000)  # Aguarda 5 segundos antes de encerrar o jogo
            break

        # Verifica se o pacman encontrou uma nota musical
        if MAPA[yPacman // 32][xPacman // 32] == 2:
            pontuacao += 10  # Ajuste a pontuação conforme necessário
            MAPA[yPacman // 32][xPacman // 32] = 0  # Remove a pílula do mapa
            som_A.play()
            if pontuacao == total_points:
                msg = "Você ganhou!"
                desenhaTexto(msg, LARGURAJANELA // 2, ALTURAJANELA // 2, 36, pygame.Color("blue"))
                # Toca música final
                pygame.time.delay(30000)
                atualizaTelaJogo()
                break

        #Desenha o mapa
        desenhaMapa(parede, nota, (xPacman, yPacman))

        #Desenha o Pacman
        desenhaImagem(pacman, xPacman, yPacman)

        #Desenha o Mozart
        desenhaImagem(mozart, xMozart, yMozart)

        #Desenha o Elvis
        desenhaImagem(elvis, xElvis, yElvis)

        # Exibe pontuação atual
        msg = f"Points: {pontuacao}"
        desenhaTexto(msg, 50, 15, 24, pygame.Color("white"))

        #Atualiza os objetos na janela
        atualizaTelaJogo()

        pygame.mixer.music.set_volume(0.3)

    pygame.mixer.quit()
    finalizaJogo()


main()

