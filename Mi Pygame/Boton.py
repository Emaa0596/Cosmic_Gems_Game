import pygame

class Boton():
    def __init__(self,pantalla:pygame.Surface,path_imagen:str, tamaño:tuple, posicion:tuple , path_imagen_click = ""):
        self.pantalla_master = pantalla
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        self.pos_x = posicion[0]
        self.pos_y = posicion[1]
        self.imagen = pygame.image.load(path_imagen)
        self.imagen = pygame.transform.scale(self.imagen,(self.ancho,self.alto))
        if path_imagen_click != "":
            self.imagen_click = pygame.image.load(path_imagen_click)
            self.imagen_click = pygame.transform.scale(self.imagen_click,(self.ancho,self.alto))

        self.rectangulo = self.imagen.get_rect()
        self.rectangulo.x = self.pos_x
        self.rectangulo.y = self.pos_y
    