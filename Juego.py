# Author: Ing. Juan David Díaz
# Date: 2022
# Version: 1.0
# Proyect: Juego culebra
# Proyect description: Juego retro de culebra en pygame 2.1.2 (SDL 2.0.18, Python 3.10.0)
# Description: Clase Juego

import sys
import pygame
from Culebra import Culebra
from Fruta import Fruta

class Juego:
    def __init__(self, ANCHO_VENTANA:int, ALTO_VENTANA:int, 
    ALTO_INFO:int, COLOR_BORDE:tuple, COLOR_TABLERO:tuple, 
    TAM:int, VEL:int) -> None:
        self.ANCHO_VENTANA = ANCHO_VENTANA
        self.ALTO_VENTANA = ALTO_VENTANA
        self.ALTO_INFO = ALTO_INFO
        self.COLOR_BORDE = COLOR_BORDE
        self.COLOR_TABLERO = COLOR_TABLERO
        self.TAM = TAM
        self.VEL = VEL


    def loopJuego(self):
        pygame.init()
        pygame.display.set_caption("Culebrita")
        pantalla = pygame.display.set_mode((self.ANCHO_VENTANA,self.ALTO_VENTANA + self.ALTO_INFO))
        reloj = pygame.time.Clock()
        jugando = True
        gameOver = False
        completado = False
        puntaje = 0
        culebra = Culebra(int((self.ANCHO_VENTANA/2)/self.TAM)*self.TAM, int((self.ALTO_VENTANA/2)/self.TAM)*self.TAM, self.TAM)
        fruta = Fruta(0,0, self.TAM)
        fruta.cambiarCoordenadas(culebra, self.ANCHO_VENTANA, self.ALTO_VENTANA)
        # main loop
        while jugando:
            # main loop
            while not gameOver and not completado:
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
                self.dibujarTablero(pantalla)
                self.mostrarInfo(pantalla, puntaje)
                culebra.mover()
                culebra.dibujar(pantalla)
                fruta.dibujar(pantalla)
                if fruta.getCoord() == culebra.getCabezaCoord():
                    puntaje += 10
                    celdasX = int(self.ANCHO_VENTANA/self.TAM)
                    celdasY = int(self.ALTO_VENTANA/self.TAM)
                    if len(culebra.cuerpo) == (celdasX*celdasY)-1:
                        completado = True
                        self.dibujarTablero(pantalla)
                        self.mostrarInfo(pantalla, puntaje)
                    else:
                        culebra.comiendo = True
                        fruta.cambiarCoordenadas(culebra, self.ANCHO_VENTANA, self.ALTO_VENTANA)
                else:
                    culebra.comiendo = False
                gameOver = culebra.verificarColision(self.ANCHO_VENTANA, self.ALTO_VENTANA) 
                reloj.tick(self.VEL)
            if gameOver and not completado:
                self.msgGameOver(pantalla)
            else:
                self.msgCompletado(pantalla)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameOver = False
                        completado = False
                        puntaje = 0
                        culebra = Culebra(int((self.ANCHO_VENTANA/2)/self.TAM)*self.TAM, int((self.ALTO_VENTANA/2)/self.TAM)*self.TAM, self.TAM)
                        fruta = Fruta(0,0, self.TAM)
                        fruta.cambiarCoordenadas(culebra, self.ANCHO_VENTANA, self.ALTO_VENTANA)
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
        pygame.quit()
        sys.exit()
    
    def msgCompletado(self, pantalla):
        fuente = pygame.font.match_font('consolas')
        tipo_letra1 = pygame.font.Font(fuente,40)
        tipo_letra2 = pygame.font.Font(fuente,20)
        superficie1 = tipo_letra1.render("FELICITACIONES JUEGO TERMINADO",True, (0,255,0))
        rectangulo1 = superficie1.get_rect()
        rectangulo1.center = (int(self.ANCHO_VENTANA/2), int((self.ALTO_VENTANA)/2))
        pantalla.blit(superficie1,rectangulo1)
        superficie2 = tipo_letra1.render("JUEGO TERMINADO",True, (0,255,0))
        rectangulo2 = superficie1.get_rect()
        rectangulo2.center = (int(self.ANCHO_VENTANA/2), int((self.ALTO_VENTANA)/2)+50)
        pantalla.blit(superficie2,rectangulo2)
        superficie3 = tipo_letra2.render("Presiona enter para empezar de nuevo",True, (0,255,0))
        rectangulo3 = superficie2.get_rect()
        rectangulo3.center = (int(self.ANCHO_VENTANA/2), int((self.ALTO_VENTANA)/2) + 100)
        pantalla.blit(superficie3,rectangulo3)

    def msgGameOver(self, pantalla):
        fuente = pygame.font.match_font('consolas')
        tipo_letra1 = pygame.font.Font(fuente,40)
        tipo_letra2 = pygame.font.Font(fuente,20)
        superficie1 = tipo_letra1.render("GAME OVER",True, (255,0,0))
        rectangulo1 = superficie1.get_rect()
        rectangulo1.center = (int(self.ANCHO_VENTANA/2), int((self.ALTO_VENTANA)/2))
        pantalla.blit(superficie1,rectangulo1)
        superficie2 = tipo_letra2.render("Presiona enter para empezar de nuevo",True, (255,0,0))
        rectangulo2 = superficie2.get_rect()
        rectangulo2.center = (int(self.ANCHO_VENTANA/2), int((self.ALTO_VENTANA)/2) + 50)
        pantalla.blit(superficie2,rectangulo2)

    def mostrarInfo(self, pantalla, puntaje):
        fuente = pygame.font.match_font('consolas')
        tipo_letra = pygame.font.Font(fuente,20)
        superficie = tipo_letra.render("Puntaje: "+ str(puntaje),True, (233,234,237))
        rectangulo = superficie.get_rect()
        rectangulo.center = (int(self.ANCHO_VENTANA/2), int(self.ALTO_VENTANA + self.ALTO_INFO/2))
        pantalla.blit(superficie,rectangulo)

    def dibujarTablero(self, pantalla):
        pantalla.fill(self.COLOR_BORDE)
        pygame.draw.rect(pantalla, self.COLOR_TABLERO, [self.TAM, self.TAM, self.ANCHO_VENTANA-(2*self.TAM), self.ALTO_VENTANA-(2*self.TAM)], 0)