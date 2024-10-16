import pygame
from Configuraciones import obtener_rectangulos
from Items import *
import random
#from Class_personaje import personaje_principal

ANCHO = 1300
ALTO = 600

class Plataforma:
    def __init__(self,tamaño:tuple, posicion_inicial:tuple,esta_visible:bool,path_plataforma:str="",tiene_premio = False, path_premio = ""):
        self.esta_visible = esta_visible
        self.ancho = tamaño[0]
        self.alto = tamaño[1]

        if self.esta_visible:
            superficie_plataforma = pygame.image.load(path_plataforma)
            self.superficie_plataforma = pygame.transform.scale(superficie_plataforma,(self.ancho,self.alto))
            self.rectangulo = self.superficie_plataforma.get_rect()
            self.rectangulo.x = posicion_inicial[0]
            self.rectangulo.y = posicion_inicial[1]       
        else:
            self.rectangulo = pygame.Rect(posicion_inicial[0],posicion_inicial[1],self.ancho,self.alto)
            self.limites_boss = {}
            self.limites_boss["uno"] = pygame.Rect(self.rectangulo.left + 325, self.rectangulo.top -8, 8, 8)
            self.limites_boss["dos"] = pygame.Rect(self.rectangulo.left + 650, self.rectangulo.top -8, 8, 8)
            self.limites_boss["tres"] = pygame.Rect(self.rectangulo.left + 975, self.rectangulo.top -8, 8, 8)
            self.limites_boss["cuatro"] = pygame.Rect(self.rectangulo.left + 1225, self.rectangulo.top -8, 8, 8)

            
        self.lados = obtener_rectangulos(self.rectangulo)
        self.limite_derecho = pygame.Rect(self.rectangulo.right - 8, self.rectangulo.top -8, 8, 8)
        self.limite_izquierdo = pygame.Rect(self.rectangulo.left, self.rectangulo.top -8, 8, 8)

        self.tiene_premio = tiene_premio
        self.premio_descubierto = False
        self.path_premio = path_premio

    def cambiar_plataforma(self,nivel_actual:str):
        if self.premio_descubierto:
            match nivel_actual:
                case "uno":
                    superficie = pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\plataformas\madera.png")
                case "dos":
                    superficie = pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\plataformas\gris.png")
                case "tres":
                    superficie = pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\plataformas\verde.png")
            self.superficie_plataforma = pygame.transform.scale(superficie,(self.ancho,self.alto))

    def girar_plataforma(self, flip_x:bool, flip_y:bool):
        self.superficie_plataforma = pygame.transform.flip(self.superficie_plataforma,flip_x,flip_y)

    def agregar_item(self, lista_items_actual:list,nivel_actual:str, que_item = ""):
        lista = ["picante","gema","vida"]
        if que_item == "":
            que_item = random.choice(lista)
        match que_item:
            case "picante":
                premio = Item(r"juego segundo parcial\Mi Pygame\Sprites\items\picante.png",(self.rectangulo.x + 5,self.rectangulo.y -49),(45,45),"picante")
            case "gema":
                premio = Item(r"juego segundo parcial\Mi Pygame\Sprites\items\gema.png",(self.rectangulo.x + 16,self.rectangulo.y -25),(25,25),"gema")
            case "vida":
                premio = Item(r"juego segundo parcial\Mi Pygame\Sprites\items\vida.png",(self.rectangulo.x + 16,self.rectangulo.y -25),(25,25),"vida")
            case "abrir_puerta":
                premio = Item(r"juego segundo parcial\Mi Pygame\Sprites\plataformas\puerta_abierta.png",(self.rectangulo.x,self.rectangulo.y -8),(self.ancho,self.alto),"puerta")
        self.cambiar_plataforma(nivel_actual)
        lista_items_actual.append(premio)
