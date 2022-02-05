''' -----------------------------------------------------------
    |                      Juego Culebra                      |
    |                         V. 1.0                          | 
    |                          Main                           |      
    |               Autor: Ing. Juan David Díaz               |
    |                          2022                           |
    -----------------------------------------------------------'''
import sys
import pygame

from Culebra import Culebra
from Fruta import Fruta

ANCHO_VENTANA = 500
ALTO_VENTANA = 500
ALTO_INFO = 50
COLOR_BORDE = (11, 20, 82)
COLOR_TABLERO = (0,0,0)
TAM = 10
VEL = 10

def juego():
    pygame.init()
    pygame.display.set_caption("Culebrita")
    pantalla = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA + ALTO_INFO))
    reloj = pygame.time.Clock()
    jugando = True
    gameOver = False
    puntaje = 0
    culebra = Culebra(250, 250, TAM)
    fruta = Fruta(0,0, TAM)
    fruta.cambiarCoordenadas(culebra, ANCHO_VENTANA, ALTO_VENTANA)
    # main loop
    while jugando:
        # main loop
        while not gameOver:
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT and culebra.direccion != 2:
                        culebra.direccion = 1
                        break
                    if event.key == pygame.K_LEFT and culebra.direccion != 1:
                        culebra.direccion = 2
                        break
                    if event.key == pygame.K_UP and culebra.direccion != 4:
                        culebra.direccion = 3
                        break
                    if event.key == pygame.K_DOWN and culebra.direccion != 3:
                        culebra.direccion = 4
                        break
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            dibujarTablero(pantalla)
            mostrarInfo(pantalla, puntaje)
            culebra.mover()
            culebra.dibujar(pantalla)
            fruta.dibujar(pantalla)
            if fruta.getCoord() == culebra.getCabezaCoord():
                puntaje += 10
                culebra.comiendo = True
                fruta.cambiarCoordenadas(culebra, ANCHO_VENTANA, ALTO_VENTANA)
            else:
                culebra.comiendo = False
            gameOver = culebra.verificarColision(ANCHO_VENTANA, ALTO_VENTANA) 
            reloj.tick(VEL)
        if gameOver:
            msgGameOver(pantalla)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    gameOver = False
                    puntaje = 0
                    culebra = Culebra(250, 250, TAM)
                    fruta = Fruta(0,0, TAM)
                    fruta.cambiarCoordenadas(culebra, ANCHO_VENTANA, ALTO_VENTANA)
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
    pygame.quit()
    sys.exit()

def msgGameOver(pantalla):
    fuente = pygame.font.match_font('consolas')
    tipo_letra1 = pygame.font.Font(fuente,40)
    tipo_letra2 = pygame.font.Font(fuente,20)
    superficie1 = tipo_letra1.render("GAME OVER",True, (255,0,0))
    rectangulo1 = superficie1.get_rect()
    rectangulo1.center = (int(ANCHO_VENTANA/2), int((ALTO_VENTANA)/2))
    pantalla.blit(superficie1,rectangulo1)
    superficie2 = tipo_letra2.render("Presiona enter para empezar de nuevo",True, (255,0,0))
    rectangulo2 = superficie2.get_rect()
    rectangulo2.center = (int(ANCHO_VENTANA/2), int((ALTO_VENTANA)/2) + 50)
    pantalla.blit(superficie2,rectangulo2)

def mostrarInfo(pantalla, puntaje):
    fuente = pygame.font.match_font('consolas')
    tipo_letra = pygame.font.Font(fuente,20)
    superficie = tipo_letra.render("Puntaje: "+ str(puntaje),True, (233,234,237))
    rectangulo = superficie.get_rect()
    rectangulo.center = (int(ANCHO_VENTANA/2), int(ALTO_VENTANA + ALTO_INFO/2))
    pantalla.blit(superficie,rectangulo)

def dibujarTablero(pantalla):
    pantalla.fill(COLOR_BORDE)
    pygame.draw.rect(pantalla, COLOR_TABLERO, [TAM, TAM, ANCHO_VENTANA-(2*TAM), ALTO_VENTANA-(2*TAM)], 0)

if __name__=="__main__":
    juego()