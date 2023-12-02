######################################################
# Introdução a Programação (2023/2)
# EP2 - PacMan
# Integrante 1:
# Integrante 2:
# Integrante 3: 
# Integrante 4: 
######################################################


#ATENÇÃO: você não pode importar o módulo PyGame neste arquivo. 
#Consequentemente, você não pode usar o métodos do módulo.
#Você pode, se precisar, importar o módulo math e/ou random.
from BaseParaJogo import *

CORFUNDOJANELA = (0, 0, 0)
LARGURAJANELA = 800
ALTURAJANELA = 640
ICONE = "Recursos/Imagens/icone.png"

MAPA = [
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],   
[1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1],
[1,0,1,0,1,0,1,1,1,0,1,1,1,1,1,0,1,1,1,0,1,0,1,0,1],
[1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,1],
[1,1,1,0,1,1,1,0,0,0,1,0,0,0,1,0,0,0,1,1,1,0,1,1,1],
[1,0,0,0,0,0,1,0,1,1,1,1,0,1,1,1,1,0,1,0,0,0,0,0,1],
[1,0,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,1,0,1],
[1,0,0,0,0,0,1,1,0,1,1,1,1,1,1,1,0,1,1,0,0,0,0,0,1],
[1,0,1,0,1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,1,0,1,0,1],
[1,0,1,0,1,1,0,1,1,1,1,0,1,0,1,1,1,1,0,1,1,0,1,0,1],
[1,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,1],
[1,0,0,0,1,0,1,1,0,1,1,1,1,1,1,1,0,1,1,0,1,0,0,0,1],
[1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1],
[1,1,1,0,1,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,1,0,1,1,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,1,0,1,0,1,1,1,1,0,1,1,1,0,1,1,1,1,0,1,0,1,0,1],
[1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1],
[1,0,1,0,1,0,1,1,1,0,1,1,1,1,1,0,1,1,1,0,1,0,1,0,1],
[1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

def desenhaMapa(parede, pilula):
    for l in range(len(MAPA)):
        for c in range(len(MAPA[l])):
            if MAPA[l][c] == 1:
                desenhaImagem(parede, c*32, l*32)
            elif MAPA[l][c] == 2:
                desenhaImagem(pilula, c*32, l*32)

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




def main():
    criaJanela(LARGURAJANELA, ALTURAJANELA, "Pac-Man", CORFUNDOJANELA, ICONE)

    parede = carregaImagem("Recursos/Imagens/parede.png", (32, 32))
    pilula = carregaImagem("Recursos/Imagens/pilula.png", (32, 32))
    pacman = carregaImagem("Recursos/Imagens/pacman.png", (32, 32))
    mozart = carregaImagem("Recursos/Imagens/mozart.png", (32, 32))
    elvis = carregaImagem("Recursos/Imagens/elvis.png", (32, 32))

    xPacman = 384
    yPacman = 384

    xMozart = 704
    yMozart = 574

    xElvis = 28
    yElivs = 158
    background_song = carregaMusica("Recursos/Sons/Musicas/Long Gaze.mp3")

    while True:

        if teclaPressionada(K_ESCAPE):
            break

        #Limpa a janela
        limpaTela()

        # Verifica se uma das teclas foi pressionada
        # Se sim, atualiza a posição do Pacman
        if teclaPressionada(K_UP) and posicaoValida(xPacman, yPacman - 2):
            yPacman -= 2
        elif teclaPressionada(K_DOWN) and posicaoValida(xPacman, yPacman + 2):
            yPacman += 2
        elif teclaPressionada(K_LEFT) and posicaoValida(xPacman - 2, yPacman):
            xPacman -= 2
        elif teclaPressionada(K_RIGHT) and posicaoValida(xPacman + 2, yPacman):
            xPacman += 2


        #Desenha o mapa
        desenhaMapa(parede, pilula)

        #Desenha o Pacman
        desenhaImagem(pacman, xPacman, yPacman)

        #Desenha o Mozar
        desenhaImagem(mozart, xMozart, yMozart)

        #Desenha o Elvis
        desenhaImagem(elvis, xElvis, yElivs)

        #Atualiza os objetos na janela
        atualizaTelaJogo()


    finalizaJogo()


main()

