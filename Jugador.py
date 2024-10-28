class Jugador:
    def __init__(self,nombre):
        self.nombre = nombre
        self.puntos = 0
    
    def setPuntos(self,puntos):
        self.puntos = puntos

    def setNombre(self, nombre):
        self.nombre = nombre
    
    def getPuntos(self):
        return self.puntos
    
    def getNombre(self):
        return self.nombre