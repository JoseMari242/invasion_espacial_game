import pygame
from player import Player
from enemy import Enemy
from utils import hay_colision
import random

class Game:
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.fondo = pygame.image.load('C:\\Users\\EQUIPO\\Desktop\\Python\\pythonProject\\Invasion_espacial\\assets\\images\\Fondo.jpg')
        self.musica_fondo = pygame.mixer.music.load('C:\\Users\\EQUIPO\\Desktop\\Python\\pythonProject\\Invasion_espacial\\assets\\sounds\\MusicaFondo.mp3')
        pygame.mixer.music.play(-1)

        # Crear el jugador
        self.jugador = Player()

        # Crear los enemigos
        self.cantidad_enemigos = 8
        self.enemigos = [Enemy() for _ in range(self.cantidad_enemigos)]

        # Variables de la bala
        self.img_bala = pygame.image.load('C:/Users/EQUIPO/Desktop/Python/pythonProject/Invasion_espacial/assets/images/bala.png')
        self.bala_x = 0
        self.bala_y = 500
        self.bala_y_cambio = 0.3
        self.bala_visible = False

        # Puntaje
        self.puntaje = 0
        self.fuente = pygame.font.Font('C:\\Users\\EQUIPO\\Desktop\\Python\\pythonProject\\Invasion_espacial\\assets\\fonts\\Simple.otf', 32)
        self.texto_x = 10
        self.texto_y = 10

        # Texto final de juego
        self.fuente_final = pygame.font.Font('C:\\Users\\EQUIPO\\Desktop\\Python\\pythonProject\\Invasion_espacial\\assets\\fonts\\Simple.otf', 40)

    def texto_final(self):
        mi_fuente_final = self.fuente_final.render("GAME OVER", True, (255, 255, 255))
        self.pantalla.blit(mi_fuente_final, (60, 200))

    def mostrar_puntaje(self, x, y):
        texto = self.fuente.render(f"Score: {self.puntaje}", True, (255, 255, 255))
        self.pantalla.blit(texto, (x, y))

    def ejecutar(self):
        se_ejecuta = True
        while se_ejecuta:
            # Imagen de fondo
            self.pantalla.blit(self.fondo, (0, 0))

            # Eventos
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    se_ejecuta = False
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_LEFT:
                        self.jugador.mover_izquierda()
                    if evento.key == pygame.K_RIGHT:
                        self.jugador.mover_derecha()
                    if evento.key == pygame.K_SPACE:
                        sonido_bala = pygame.mixer.Sound('C:\\Users\\EQUIPO\\Desktop\\Python\\pythonProject\\Invasion_espacial\\assets\\sounds\\disparo.mp3')
                        sonido_bala.play()
                        if not self.bala_visible:
                            self.bala_x = self.jugador.x
                            self.disparar_bala(self.bala_x, self.bala_y)
                if evento.type == pygame.KEYUP:
                    if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                        self.jugador.detener()

            # Movimiento del jugador
            self.jugador.actualizar_posicion()

            # Mantener al jugador dentro de los límites
            self.jugador.mantener_limites()

            # Movimiento de los enemigos
            for enemigo in self.enemigos:
                enemigo.actualizar_posicion()
                if enemigo.y > 500:
                    for e in self.enemigos:
                        e.y = 1000
                    self.texto_final()
                    break

                # Colisión
                if hay_colision(enemigo.x, enemigo.y, self.bala_x, self.bala_y):
                    sonido_colision = pygame.mixer.Sound('C:\\Users\\EQUIPO\\Desktop\\Python\\pythonProject\\Invasion_espacial\\assets\\sounds\\Golpe.mp3')
                    sonido_colision.play()
                    self.bala_y = 500
                    self.bala_visible = False
                    self.puntaje += 1
                    enemigo.reiniciar()

                enemigo.mostrar(self.pantalla)

            # Movimiento de la bala
            if self.bala_visible:
                self.disparar_bala(self.bala_x, self.bala_y)
                self.bala_y -= self.bala_y_cambio
                if self.bala_y <= -64:
                    self.bala_y = 500
                    self.bala_visible = False

            self.jugador.mostrar(self.pantalla)
            self.mostrar_puntaje(self.texto_x, self.texto_y)

            pygame.display.update()

    def disparar_bala(self, x, y):
        self.bala_visible = True
        self.pantalla.blit(self.img_bala, (x + 16, y + 10))
