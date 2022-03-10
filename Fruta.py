# Author: Ing. Juan David Díaz
# Date: 2022
# Version: 1.0
# Proyect: Juego culebra
# Proyect description: Juego retro de culebra en pygame 2.1.2 (SDL 2.0.18, Python 3.10.0)
# Description: Clase Fruta

import pygame
import random

class Fruta:
    ROJO = (255, 0, 0)
    def __init__(self,x:int,y:int, tam) -> None:
        self.x = x
        self.y = y
        self.tam = tam
 
    def dibujar(self, pantalla) -> None:
        pygame.draw.ellipse(pantalla, self.ROJO, [self.x, self.y, self.tam, self.tam], 0)

    def cambiarCoordenadas(self,culebrita, ancho, alto):
        choca = True
        while choca:
            x = int(random.randint(self.tam, ancho - (self.tam*2))/self.tam)*self.tam
            y = int(random.randint(self.tam, alto - (self.tam*2))/self.tam)*self.tam
            choca = False
            for parte in culebrita.cuerpo:
                if parte.x == x and parte.y == y:
                    choca = True
        self.x = x
        self.y = y
        return x,y

    def getCoord(self):
        return self.x, self.y
