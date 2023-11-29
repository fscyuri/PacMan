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

def main():
    criaJanela(LARGURAJANELA, ALTURAJANELA, "Pac-Man", CORFUNDOJANELA, ICONE)

    parede = carregaImagem("Recursos/Imagens/parede.png", (32, 32))
    pilula = carregaImagem("Recursos/Imagens/pilula.png", (32, 32))
    pacman = carregaImagem("Recursos/Imagens/pacman.png", (32, 32))
    xPacman = 384
    yPacman = 384
    while True:      
        
        if teclaPressionada(K_ESCAPE):
            break

        #Limpa a janela
        limpaTela()

        #Verifica se uma das teclas foi precionada
        #Se sim, atualiza a posição do Pacman
        if teclaPressionada(K_UP):
            yPacman -= 2
        elif teclaPressionada(K_DOWN):
            yPacman += 2
        elif teclaPressionada(K_LEFT):
            xPacman -= 2
        elif teclaPressionada(K_RIGHT):
            xPacman += 2

        #Desenha o mapa
        desenhaMapa(parede, pilula)

        #Desenha o Pacman
        desenhaImagem(pacman, xPacman, yPacman)

        #Atualiza os objetos na janela
        atualizaTelaJogo()

    finalizaJogo()

main()

