import pygame

class Inicio:
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.fondo = pygame.image.load('C:\\Users\\EQUIPO\\Desktop\\Python\\pythonProject\\Invasion_espacial\\assets\\images\\Fondo.jpg')
        self.fuente = pygame.font.Font('C:\\Users\\EQUIPO\\Desktop\\Python\\pythonProject\\Invasion_espacial\\assets\\fonts\\Simple.otf', 40)

    def mostrar_menu(self):
        # Aquí puedes dibujar el menú de inicio
        ejecutando = True
        while ejecutando:
            self.pantalla.blit(self.fondo, (0, 0))
            mensaje = self.fuente.render("Presiona Enter para empezar", True, (255, 255, 255))
            self.pantalla.blit(mensaje, (100, 250))

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    ejecutando = False
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_RETURN:
                        ejecutando = False

            pygame.display.update()
