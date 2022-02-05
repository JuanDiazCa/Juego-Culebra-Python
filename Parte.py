''' -----------------------------------------------------------
    |                      Juego Culebra                      |
    |                         V. 1.0                          | 
    |                       Clase Parte                       |      
    |               Autor: Ing. Juan David Díaz               |
    |                          2022                           |
    -----------------------------------------------------------'''
import pygame

class Parte:
    AZUL = (0, 0, 255)
    VERDE = (0, 255, 0)
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
        pygame.draw.rect(pantalla, color, [self.x, self.y, self.tam, self.tam], 0)