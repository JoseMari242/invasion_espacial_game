import pygame
import random

class Enemy:
    def __init__(self):
        self.img_enemigo = pygame.image.load('C:\\Users\\EQUIPO\\Desktop\\Python\\pythonProject\\Invasion_espacial\\assets\\images\\enemigo.png')
        self.x = random.randint(0, 736)
        self.y = random.randint(50, 200)
        self.x_cambio = 0.2
        self.y_cambio = 50

    def actualizar_posicion(self):
        self.x += self.x_cambio
        if self.x <= 0:
            self.x_cambio = 0.2
            self.y += self.y_cambio
        elif self.x >= 736:
            self.x_cambio = -0.2
            self.y += self.y_cambio

    def reiniciar(self):
        self.x = random.randint(0, 736)
        self.y = random.randint(50, 200)

    def mostrar(self, pantalla):
        pantalla.blit(self.img_enemigo, (self.x, self.y))
