import pygame
import random

class Enemy:
    def __init__(self, tipo='grande'):
        self.tipo = tipo
        if self.tipo == 'grande':
            self.img_enemigo = pygame.image.load('C:\\Users\\EQUIPO\\Desktop\\Python\\pythonProject\\Invasion_espacial\\assets\\images\\grande.png')
            self.x_cambio = 0.2
            self.y_cambio = 50
        elif self.tipo == 'pequeño':
            self.img_enemigo = pygame.image.load('C:\\Users\\EQUIPO\\Desktop\\Python\\pythonProject\\Invasion_espacial\\assets\\images\\enemigo.png')
            self.x_cambio = 0.2  # Ajusta la velocidad para que no sea tan rápida
            self.y_cambio = 40

        self.x = random.randint(0, 736)
        self.y = random.randint(50, 200)

    def actualizar_posicion(self):
        self.x += self.x_cambio
        if self.x <= 0:
            self.x_cambio = abs(self.x_cambio)
            self.y += self.y_cambio
        elif self.x >= 736:
            self.x_cambio = -abs(self.x_cambio)
            self.y += self.y_cambio

    def dividir(self):
        if self.tipo == 'grande':
            return [Enemy(tipo='pequeño') for _ in range(4)]  # Aumentar el número de enemigos pequeños
        return []

    def reiniciar(self):
        self.x = random.randint(0, 736)
        self.y = random.randint(50, 200)

    def mostrar(self, pantalla):
        pantalla.blit(self.img_enemigo, (self.x, self.y))