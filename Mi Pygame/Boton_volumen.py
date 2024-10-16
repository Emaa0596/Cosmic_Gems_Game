import pygame, sys
from Boton import Boton

class Boton_volumen(Boton):
    def __init__(self, pantalla, path_imagen: str, tamaño: tuple, posicion: tuple, path_imagen_click=""):
        super().__init__(pantalla, path_imagen, tamaño, posicion, path_imagen_click)
        self.mute = False
        self.superficie = self.imagen

    def mutear(self):
        self.mute = not self.mute
        pygame.mixer.init()
        if self.mute:
            pygame.mixer.music.set_volume(0)
            self.imagen = self.imagen_click
        else:
            pygame.mixer.music.set_volume(0.2)
            self.imagen = self.superficie