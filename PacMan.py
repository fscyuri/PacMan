import pygame.mixer
from BaseParaJogo import *
import random

CORFUNDOJANELA = (0, 0, 0)
LARGURAJANELA = 800
ALTURAJANELA = 640
ICONE = "Recursos/Imagens/icone.png"
direcao_Elvis = random.choice([K_UP, K_DOWN, K_LEFT, K_RIGHT])
direcao_Mozart = random.choice([K_UP, K_DOWN, K_LEFT, K_RIGHT])
direcao_freddie = random.choice([K_UP, K_DOWN, K_LEFT, K_RIGHT])
direcao_Amy = random.choice([K_UP, K_DOWN, K_LEFT, K_RIGHT])


MAPA = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 2, 2, 2, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 2, 2, 2, 2, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 2, 2, 2, 2, 1],
    [1, 2, 1, 1, 1, 0, 1, 0, 0, 2, 2, 2, 2, 2, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1],
    [1, 2, 0, 2, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 2, 2, 2, 1],
    [1, 2, 1, 2, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1],
    [1, 2, 1, 2, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
    [1, 2, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 2, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 2, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 0, 0, 0, 1, 2, 1, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 2, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 2, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 2, 2, 2, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


def desenhaMapa(parede, pilula, posPacman):
    for l in range(len(MAPA)):
        for c in range(len(MAPA[l])):
            if MAPA[l][c] == 1:
                desenhaImagem(parede, c * 32, l * 32)
            elif MAPA[l][c] == 2:
                desenhaImagem(pilula, c * 32, l * 32)
            elif MAPA[l][c] == 0:  # Nota foi comida
                continue
            elif MAPA[l][c] == 9:  # Posicao do pacman
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


def movimentoAleatorio(x, y, velocidade, direcao):
    if direcao == K_UP:
        if posicaoValida(x, y - velocidade):
            y -= 2
        else:
            direcao = random.choice([K_DOWN, K_LEFT, K_RIGHT])
    elif direcao == K_DOWN:
        if posicaoValida(x, y + velocidade):
            y += 2
        else:
            direcao = random.choice([K_UP, K_LEFT, K_RIGHT])
    elif direcao == K_LEFT:
        if posicaoValida(x - velocidade, y):
            x -= 2
        else:
            direcao = random.choice([K_UP, K_DOWN, K_RIGHT])
    elif direcao == K_RIGHT:
        if posicaoValida(x + velocidade, y):
            x += 2
        else:
            direcao = random.choice([K_UP, K_DOWN, K_LEFT])
    return x, y,direcao

def persegue(x_pacman,y_pacman,x,y,velocidade,nova_direcao):
    if x_pacman < x:
        nova_direcao = K_LEFT
        if posicaoValida(x - velocidade, y):
            x -= velocidade
        else:
            nova_direcao = random.choice([K_UP, K_DOWN, K_LEFT])
    if x_pacman > x:
        nova_direcao = K_RIGHT
        if posicaoValida(x + velocidade, y):
            x += velocidade
        else:
            nova_direcao = random.choice([K_UP, K_DOWN, K_LEFT])
    if y_pacman < y:
        nova_direcao = K_UP
        if posicaoValida(x, y - velocidade):
            y -= velocidade
        else:
            nova_direcao = random.choice([K_DOWN, K_LEFT, K_RIGHT])
    if y_pacman > y:
        nova_direcao = K_DOWN
        if posicaoValida(x, y + velocidade):
            y += velocidade
        else:
            nova_direcao = random.choice([K_UP, K_LEFT, K_RIGHT])
    return x, y, nova_direcao

doremifa = ['C', 'D', 'E', 'F', 'F', 'F', 'C', 'D', 'C', 'D', 'D', 'D',
            'C', 'G', 'F', 'E', 'E', 'E', 'C', 'D', 'E', 'F', 'F', 'F']


twinkle_twinkle = ['C', 'C', 'G', 'G', 'A', 'A', 'G',
                   'F', 'F', 'E', 'E', 'D', 'D', 'C']

happy_birthday = ['C', 'C', 'D', 'C', 'F', 'E', 'C', 'C', 'D',
                  'C', 'G', 'F', 'C', 'C', 'C']

jingle_bells = ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'G', 'C', 'D', 'E', 'F', 'F',
                'F', 'F', 'F', 'E', 'E', 'E', 'E', 'D', 'D', 'E', 'D', 'G']

lista_melodias = doremifa, twinkle_twinkle, happy_birthday, jingle_bells
pygame.mixer.init()
som_A = pygame.mixer.Sound("Recursos/Sons/Notas Musicais/A.mp3")
som_B = pygame.mixer.Sound("Recursos/Sons/Notas Musicais/B.mp3")
som_C = pygame.mixer.Sound("Recursos/Sons/Notas Musicais/C.mp3")
som_D = pygame.mixer.Sound("Recursos/Sons/Notas Musicais/D.mp3")
som_E = pygame.mixer.Sound("Recursos/Sons/Notas Musicais/E.mp3")
som_F = pygame.mixer.Sound("Recursos/Sons/Notas Musicais/F.mp3")
som_G = pygame.mixer.Sound("Recursos/Sons/Notas Musicais/G.mp3")

def selecionaMelodia():
    # Display melody selection menu
    desenhaTexto("ESCOLHA UMA MÚSICA:", LARGURAJANELA // 2, ALTURAJANELA // 2 - 50, 24, pygame.Color("white"))
    desenhaTexto("1. Do Ré Mi Fa", LARGURAJANELA // 2, ALTURAJANELA // 2, 24, pygame.Color("white"))
    desenhaTexto("2. Twinkle, Twinkle", LARGURAJANELA // 2, ALTURAJANELA // 2 + 30, 24, pygame.Color("white"))
    desenhaTexto("3. Happy Birthday", LARGURAJANELA // 2, ALTURAJANELA // 2 + 60, 24, pygame.Color("white"))
    desenhaTexto("4. Jingle Bells", LARGURAJANELA // 2, ALTURAJANELA // 2 + 90, 24, pygame.Color("white"))
    atualizaTelaJogo()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return lista_melodias[0]
                elif event.key == pygame.K_2:
                    return lista_melodias[1]
                elif event.key == pygame.K_3:
                    return lista_melodias[2]
                elif event.key == pygame.K_4:
                    return lista_melodias[3]

def tocaMelodiaAutomaticamente(melodia):
    for nota in melodia:
        if nota == 'A':
            som_A.play()
        elif nota == 'B':
            som_B.play()
        elif nota == 'C':
            som_C.play()
        elif nota == 'D':
            som_D.play()
        elif nota == 'E':
            som_E.play()
        elif nota == 'F':
            som_F.play()
        elif nota == 'G':
            som_G.play()

        # Delay entre notas
        pygame.time.delay(600)


def main():
    criaJanela(LARGURAJANELA, ALTURAJANELA, "Pac-Man", CORFUNDOJANELA, ICONE)

    parede = carregaImagem("Recursos/Imagens/parede.png", (32, 32))
    pacman = carregaImagem("Recursos/Imagens/PacMan Icon/pacman.png", (32, 32))
    mozart = carregaImagem("Recursos/Imagens/Fantasmas/mozart.png", (32, 32))
    elvis = carregaImagem("Recursos/Imagens/Fantasmas/elvis.png", (32, 32))
    freddie = carregaImagem("Recursos/Imagens/Fantasmas/freddie2.png", (32, 32))
    amy = carregaImagem("Recursos/Imagens/Fantasmas/amy2.png", (32, 32))
    nota = carregaImagem("Recursos/Imagens/nota.png", (32, 32))

    total_points = 580

    xPacman = 384
    yPacman = 384
    velocidade_pacman = 2
    velocidade_fantasma = 2

    xMozart = 256
    yMozart = 256

    xElvis = 576
    yElvis = 576

    xFreddie = 256
    yFreddie = 384

    xAmy = 544
    yAmy = 32

    som_morte = pygame.mixer.Sound("Recursos/Sons/pacman_death.wav")
    pygame.mixer.music.load("Recursos/Sons/Musicas/Long Gaze.mp3")
    pygame.mixer.init()
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)  # O argumento -1 faz com que a música seja reproduzida em um loop contínuo

    pontuacao = 0
    melodia_escolhida = selecionaMelodia()
    melodia_index = 0

    while True:
        if teclaPressionada(K_ESCAPE):
            break

        # Limpa a janela
        limpaTela()

        # Verifica se uma das teclas foi pressionada

        if teclaPressionada(K_UP) and posicaoValida(xPacman, yPacman - velocidade_pacman):
            pacman = carregaImagem("Recursos/Imagens/PacMan Icon/pacman_up.png", (32, 32))
            yPacman -= 2
        elif teclaPressionada(K_DOWN) and posicaoValida(xPacman, yPacman + velocidade_pacman):
            pacman = carregaImagem("Recursos/Imagens/PacMan Icon/pacman_down.png", (32, 32))
            yPacman += 2
        elif teclaPressionada(K_LEFT) and posicaoValida(xPacman - velocidade_pacman, yPacman):
            pacman = carregaImagem("Recursos/Imagens/PacMan Icon/pacman.png", (32, 32))
            xPacman -= 2
        elif teclaPressionada(K_RIGHT) and posicaoValida(xPacman + velocidade_pacman, yPacman):
            pacman = carregaImagem("Recursos/Imagens/PacMan Icon/pacman_right.png", (32, 32))
            xPacman += 2

        # Movimento aleatório de Mozart
        global direcao_Mozart
        xMozart, yMozart,direcao_Mozart = movimentoAleatorio(xMozart, yMozart, velocidade_fantasma,direcao_Mozart)

        # Movimento aleatório de Elvis
        global direcao_Elvis
        xElvis, yElvis,direcao_Elvis = movimentoAleatorio(xElvis, yElvis, velocidade_fantasma,direcao_Elvis)

        # Movimento aleatório de Freedie
        global direcao_freddie
        xFreddie, yFreddie,direcao_freddie = persegue(xPacman,yPacman,xFreddie,yFreddie,velocidade_fantasma,direcao_freddie)

        # Movimento aleatório de Amy
        global direcao_Amy
        xAmy, yAmy,direcao_Amy = persegue(xPacman,yPacman,xAmy,yAmy,velocidade_fantasma,direcao_Amy)


        # Verifica se Mozart ou Elvis encontraram o Pacman
        if (xPacman, yPacman) == (xMozart, yMozart) or (xPacman, yPacman) == (xElvis, yElvis) or (xPacman, yPacman) == (xFreddie,yFreddie) or (xPacman, yPacman) == (xAmy,yAmy):
            som_morte.play()
            pygame.time.delay(2000)
            mensagem = "Você perdeu! Os fantasmas te pegaram."
            desenhaTexto(mensagem, LARGURAJANELA // 2, ALTURAJANELA // 2, 40, pygame.Color("red"))
            atualizaTelaJogo()
            pygame.time.delay(3000)
            while True:
                desenhaTexto("Deseja jogar novamente? (Pressione R para jogar novamente, ESC para sair)", LARGURAJANELA // 2, ALTURAJANELA // 2 + 50, 24, pygame.Color("white"))
                atualizaTelaJogo()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_r:
                            # Reinicia o jogo
                            main()
                        elif event.key == pygame.K_ESCAPE:
                            pygame.quit()

        # Verifica se o pacman encontrou uma nota musical
        if MAPA[yPacman // 32][xPacman // 32] == 2:
            pontuacao += 10
            MAPA[yPacman // 32][xPacman // 32] = 0  # Remove a pílula do mapa

            # Toca o som correspondente à nota musical
            melodia_atual = melodia_escolhida
            nota_index = melodia_atual[melodia_index % len(melodia_atual)]

            melodia_index = (melodia_index + 1) % len(melodia_escolhida)

            # Toca o som correspondente à nota musical
            if nota_index == 'A':
                som_A.play()
            elif nota_index == 'B':
                som_B.play()
            elif nota_index == 'C':
                som_C.play()
            elif nota_index == 'D':
                som_D.play()
            elif nota_index == 'E':
                som_E.play()
            elif nota_index == 'F':
                som_F.play()
            elif nota_index == 'G':
                som_G.play()

            if pontuacao == total_points:
                msg = "Você ganhou!"
                desenhaTexto(msg, LARGURAJANELA // 2, ALTURAJANELA // 2, 36, pygame.Color("blue"))
                atualizaTelaJogo()
                tocaMelodiaAutomaticamente(melodia_escolhida)
                pygame.time.delay(1000)
                while True:
                    desenhaTexto("Deseja jogar novamente? (Pressione R para jogar novamente, ESC para sair)", LARGURAJANELA // 2, ALTURAJANELA // 2 + 50, 24, pygame.Color("white"))
                    atualizaTelaJogo()

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_r:
                                # Reinicia o jogo
                                main()
                            elif event.key == pygame.K_ESCAPE:
                                pygame.quit()

        desenhaMapa(parede, nota, (xPacman, yPacman))
        desenhaImagem(pacman, xPacman, yPacman)
        desenhaImagem(mozart, xMozart, yMozart)
        desenhaImagem(elvis, xElvis, yElvis)
        desenhaImagem(freddie,xFreddie,yFreddie)
        desenhaImagem(amy,xAmy,yAmy)

        # Exibe pontuação atual
        msg = f"Points: {pontuacao}"
        desenhaTexto(msg, 50, 15, 24, pygame.Color("white"))

        # Atualiza os objetos na janela
        atualizaTelaJogo()

        pygame.mixer.music.set_volume(0.3)

    pygame.mixer.quit()
    finalizaJogo()


main()
