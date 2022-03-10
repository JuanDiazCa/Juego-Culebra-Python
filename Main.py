# Author: Ing. Juan David Díaz
# Date: 2022
# Version: 1.1
# Proyect: Juego culebra
# Proyect description: Juego retro de culebra en pygame 2.1.2 (SDL 2.0.18, Python 3.10.0)
# Description: Main.py (Main)

from Juego import Juego

ANCHO_VENTANA = 500
ALTO_VENTANA = 500
ALTO_INFO = 50
COLOR_BORDE = (11, 20, 82)
COLOR_TABLERO = (0,0,0)
TAM = 20
VEL = 10

if __name__=="__main__":
    Juego(ANCHO_VENTANA, ALTO_VENTANA, ALTO_INFO, COLOR_BORDE, COLOR_TABLERO, TAM, VEL).loopJuego()