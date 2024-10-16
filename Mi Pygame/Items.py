import pygame

class Item:
    def __init__(self, path_imagen, posicion:tuple, tamaño:tuple, que_item:str = ""):
        self.animacion = pygame.image.load(path_imagen)
        self.animacion = pygame.transform.scale(self.animacion,(tamaño[0],tamaño[1]))
        self.rectangulo = self.animacion.get_rect()
        self.rectangulo.x = posicion[0]
        self.rectangulo.y = posicion[1]
        self.que_item = que_item
    