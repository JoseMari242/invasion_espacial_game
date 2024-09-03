import pygame
from game import Game
from menu import Inicio

# Inicializar Pygame
pygame.init()

# Crear la pantalla
pantalla = pygame.display.set_mode((800, 600))

# Iniciar el juego
def main():
    # Crear instancia de la clase Inicio
    menu_inicio = Inicio(pantalla)
    menu_inicio.mostrar_menu()

    # Crear instancia de la clase Game
    juego = Game(pantalla)
    juego.ejecutar()

if __name__ == "__main__":
    main()
