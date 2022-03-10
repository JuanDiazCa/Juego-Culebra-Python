# Author: Ing. Juan David Díaz
# Date: 2022
# Version: 1.0
# Proyect: Juego culebra
# Proyect description: Juego retro de culebra en pygame 2.1.2 (SDL 2.0.18, Python 3.10.0)
# Description: Clase Parte

import pygame

class Parte:
    AZUL = (0, 0, 255)
    VERDE = (0, 255, 0)
    GRIS = (155, 155, 155)
    def __init__(self, x:int, y:int, esCabeza:bool, tam) -> None:
        self.x = x
        self.y = y 
        self.tam = tam
        self.esCabeza = esCabeza

    def dibujar(self, pantalla) -> None:
        if(self.esCabeza):
            color = self.AZUL
        else:
            color = self.VERDE
        pygame.draw.rect(pantalla, color, [self.x, self.y, self.tam, self.tam], 0, int(self.tam/10))
        pygame.draw.rect(pantalla, self.GRIS, [self.x, self.y, self.tam, self.tam], 1, int(self.tam/10))