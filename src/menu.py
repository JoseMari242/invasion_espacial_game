import pygame
import os

class Inicio:
    def __init__(self, pantalla):
        self.pantalla = pantalla
        base_dir = os.path.dirname(__file__)
        self.fondo = pygame.image.load(os.path.join(base_dir, '../assets/images/Menu.jpg'))
        self.fondo_rect = self.fondo.get_rect()

        self.fuente_titulo = pygame.font.Font(os.path.join(base_dir, '../assets/fonts/Simple.otf'), 80)
        self.fuente_boton = pygame.font.Font(os.path.join(base_dir, '../assets/fonts/Simple.otf'), 40)
        self.color_titulo = (255, 215, 0)  # Dorado
        self.color_boton = (255, 190, 0)  # Rojo brillante
        self.boton_rect_start = pygame.Rect(280, 400, 250, 50)  # Posición y tamaño del botón Start
        self.boton_rect_instrucciones = pygame.Rect(280, 470, 250, 50)  # Posición y tamaño del botón Instrucciones

    def mostrar_menu(self):
        ejecutando = True
        mostrar_instrucciones = False

        while ejecutando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    ejecutando = False

                # Manejar clic del ratón
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.boton_rect_start.collidepoint(mouse_pos):
                        ejecutando = False  # Salir del menú para iniciar el juego
                    if self.boton_rect_instrucciones.collidepoint(mouse_pos):
                        mostrar_instrucciones = True

            if mostrar_instrucciones:
                self.mostrar_instrucciones()
                mostrar_instrucciones = False
                continue

            # Dibuja el fondo
            self.pantalla.blit(self.fondo, self.fondo_rect)

            # Mostrar título
            titulo = self.fuente_titulo.render("Invasión Espacial", True, self.color_titulo)
            self.pantalla.blit(titulo, (100, 100))

            # Mostrar botón Start
            pygame.draw.rect(self.pantalla, self.color_boton, self.boton_rect_start)
            boton_texto_start = self.fuente_boton.render("Iniciar Juego", True, (255, 255, 255))
            self.pantalla.blit(boton_texto_start, (self.boton_rect_start.x + 10, self.boton_rect_start.y + 10))

            # Mostrar botón Instrucciones
            pygame.draw.rect(self.pantalla, self.color_boton, self.boton_rect_instrucciones)
            boton_texto_instrucciones = self.fuente_boton.render("Instrucciones", True, (255, 255, 255))
            self.pantalla.blit(boton_texto_instrucciones,
                               (self.boton_rect_instrucciones.x + 10, self.boton_rect_instrucciones.y + 10))

            pygame.display.update()

    def mostrar_instrucciones(self):
        ejecutando = True
        while ejecutando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    ejecutando = False
                if evento.type == pygame.KEYDOWN or evento.type == pygame.MOUSEBUTTONDOWN:
                    ejecutando = False

            self.pantalla.fill((0, 0, 0))
            instrucciones = self.fuente_boton.render("Instrucciones del juego", True, (255, 255, 255))
            self.pantalla.blit(instrucciones, (100, 250))
            pygame.display.update()
