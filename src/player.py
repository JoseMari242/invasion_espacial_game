import pygame

class Player:
    def __init__(self):
        self.img_jugador = pygame.image.load('C:\\Users\\EQUIPO\\Desktop\\Python\\pythonProject\\Invasion_espacial\\assets\\images\\cohete.png')
        self.x = 368
        self.y = 500
        self.x_cambio = 0

    def mover_izquierda(self):
        self.x_cambio = -1

    def mover_derecha(self):
        self.x_cambio = 1

    def detener(self):
        self.x_cambio = 0

    def actualizar_posicion(self):
        self.x += self.x_cambio

    def mantener_limites(self):
        if self.x <= 0:
            self.x = 0
        elif self.x >= 738:
            self.x = 738

    def mostrar(self, pantalla):
        pantalla.blit(self.img_jugador, (self.x, self.y))
