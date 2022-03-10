# Author: Ing. Juan David Díaz
# Date: 2022
# Version: 1.0
# Proyect: Juego culebra
# Proyect description: Juego retro de culebra en pygame 2.1.2 (SDL 2.0.18, Python 3.10.0)
# Description: Clase Culebra

from Parte import Parte

class Culebra:    
    def __init__(self, x:int, y:int, tam:int) -> None:
        self.tam = tam
        self.comiendo=False
        self.cuerpo = []
        #direccion
        # derecha=1 ; izquierda=2 ; arriba=3 ; abajo=4
        self.direccion = 1
        self.cuerpo.append(Parte(x,y,True, tam))
        self.cuerpo.append(Parte(x-tam,y,False, tam))
        self.cuerpo.append(Parte(x-(2*tam),y,False, tam))

    def dibujar(self, pantalla) -> None:
        for parte in self.cuerpo:
            parte.dibujar(pantalla)
    
    def comer(self, x:int, y:int):#agregar a la ultima posicion
        self.cuerpo.append(Parte(x,y,False, self.tam))
    
    def girar(self, direccion:int):
        self.direccion = direccion

    def mover(self) -> None:
        pasoX = 0
        pasoY = 0
        if(self.direccion == 1):
            pasoX += self.tam
        if(self.direccion == 2):
            pasoX -= self.tam
        if(self.direccion == 3):
            pasoY -= self.tam
        if(self.direccion == 4):
            pasoY += self.tam
        cola = self.cuerpo[-1]
        for i in reversed(range(1,len(self.cuerpo))):
            self.cuerpo[i].x = self.cuerpo[i-1].x      
            self.cuerpo[i].y = self.cuerpo[i-1].y   
        self.cuerpo[0].x = self.cuerpo[0].x + pasoX     
        self.cuerpo[0].y = self.cuerpo[0].y + pasoY
        if(self.comiendo):
            self.comer(cola.x,cola.y)

    def getCabezaCoord(self):
        return self.cuerpo[0].x, self.cuerpo[0].y

    def verificarColision(self, ancho:int, alto:int) -> bool:
        #verificar colision con bordes
        x, y = self.getCabezaCoord()
        if x == 0 or x == ancho - self.tam or y == 0 or y == alto - self.tam:
            return True
        #verificar colision cuerpo
        for i in reversed(range(1,len(self.cuerpo))):
            if self.cuerpo[i].x == x and self.cuerpo[i].y == y:
                return True
        return False