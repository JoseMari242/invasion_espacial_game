import pygame
from player import Player
from enemy import Enemy
from utils import hay_colision
import os

class Game:
    def __init__(self, pantalla, nombre_jugador):
        self.pantalla = pantalla
        self.nombre_jugador = nombre_jugador
        base_dir = os.path.dirname(__file__)
        self.fondo = pygame.image.load(os.path.join(base_dir, '../assets/images/Fondo.jpg'))
        pygame.mixer.music.load(os.path.join(base_dir, '../assets/sounds/MusicaFondo.mp3'))
        pygame.mixer.music.play(-1)

        # Crear el jugador
        self.jugador = Player()

        # Crear los enemigos
        self.cantidad_enemigos = 8
        self.enemigos = [Enemy() for _ in range(self.cantidad_enemigos)]

        # Variables de la bala
        self.img_bala = pygame.image.load(os.path.join(base_dir, '../assets/images/bala.png'))
        self.bala_x = 0
        self.bala_y = 500
        self.bala_y_cambio = 0.3
        self.bala_visible = False

        # Puntaje
        self.puntaje = 0
        self.fuente = pygame.font.Font(os.path.join(base_dir, '../assets/fonts/Simple.otf'), 32)
        self.texto_x = 10
        self.texto_y = 10

        # Texto final de juego
        self.fuente_final = pygame.font.Font(os.path.join(base_dir, '../assets/fonts/Simple.otf'), 40)

    def mostrar_pantalla_final(self):
        ejecutando = True
        boton_volver_inicio = pygame.Rect(150, 400, 250, 50)
        boton_salir = pygame.Rect(400, 400, 250, 50)

        while ejecutando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    return

                # Manejar clic del ratón
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if boton_volver_inicio.collidepoint(mouse_pos):
                        ejecutando = False
                        return "volver_inicio"
                    if boton_salir.collidepoint(mouse_pos):
                        pygame.quit()
                        return

            self.pantalla.fill((0, 0, 0))
            game_over_texto = self.fuente_final.render("GAME OVER", True, (255, 0, 0))
            self.pantalla.blit(game_over_texto, (250, 150))

            puntuacion_texto = self.fuente_final.render(
                f"{self.nombre_jugador}, tu puntuación ha sido: {self.puntaje}", True, (255, 255, 255))
            self.pantalla.blit(puntuacion_texto, (150, 250))

            pygame.draw.rect(self.pantalla, (255, 190, 0), boton_volver_inicio)
            boton_texto_volver = self.fuente.render("Volver al Inicio", True, (255, 255, 255))
            self.pantalla.blit(boton_texto_volver, (boton_volver_inicio.x + 10, boton_volver_inicio.y + 10))

            pygame.draw.rect(self.pantalla, (255, 0, 0), boton_salir)
            boton_texto_salir = self.fuente.render("Salir del Juego", True, (255, 255, 255))
            self.pantalla.blit(boton_texto_salir, (boton_salir.x + 10, boton_salir.y + 10))

            pygame.display.update()

    def mostrar_puntaje(self, x, y):
        texto = self.fuente.render(f"Score: {self.puntaje}", True, (255, 255, 255))
        self.pantalla.blit(texto, (x, y))

    def ejecutar(self):
        se_ejecuta = True
        while se_ejecuta:
            self.pantalla.blit(self.fondo, (0, 0))

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    se_ejecuta = False
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_LEFT:
                        self.jugador.mover_izquierda()
                    if evento.key == pygame.K_RIGHT:
                        self.jugador.mover_derecha()
                    if evento.key == pygame.K_SPACE:
                        sonido_bala = pygame.mixer.Sound(
                            os.path.join(os.path.dirname(__file__), '../assets/sounds/disparo.mp3'))
                        sonido_bala.play()
                        if not self.bala_visible:
                            self.bala_x = self.jugador.x
                            self.disparar_bala(self.bala_x, self.bala_y)
                if evento.type == pygame.KEYUP:
                    if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                        self.jugador.detener()

            self.jugador.actualizar_posicion()
            self.jugador.mantener_limites()

            for enemigo in self.enemigos:
                enemigo.actualizar_posicion()

                if hay_colision(enemigo.x, enemigo.y, self.jugador.x, self.jugador.y):
                    resultado = self.mostrar_pantalla_final()
                    if resultado == "volver_inicio":
                        return
                    else:
                        se_ejecuta = False
                        break

                if enemigo.y > 500:
                    for e in self.enemigos:
                        e.y = 1000
                    resultado = self.mostrar_pantalla_final()
                    if resultado == "volver_inicio":
                        return
                    else:
                        se_ejecuta = False
                        break

                if hay_colision(enemigo.x, enemigo.y, self.bala_x, self.bala_y):
                    sonido_colision = pygame.mixer.Sound(
                        os.path.join(os.path.dirname(__file__), '../assets/sounds/Golpe.mp3'))
                    sonido_colision.play()
                    self.bala_y = 500
                    self.bala_visible = False
                    self.puntaje += 1
                    enemigo.reiniciar()

                enemigo.mostrar(self.pantalla)

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
