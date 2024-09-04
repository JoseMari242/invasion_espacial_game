import pygame
from menu import Inicio
from game import Game

# Inicializar Pygame
pygame.init()

# Crear la pantalla
pantalla = pygame.display.set_mode((800, 600))

def main():
    while True:
        # Crear instancia de la clase Inicio
        menu_inicio = Inicio(pantalla)
        nombre_jugador = menu_inicio.mostrar_menu()

        # Crear instancia de la clase Game
        juego = Game(pantalla, nombre_jugador)
        juego.ejecutar()

if __name__ == "__main__":
    main()
