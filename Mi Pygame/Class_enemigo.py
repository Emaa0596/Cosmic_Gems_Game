import pygame
from Configuraciones import *
import random
from Class_personaje import Personaje,Disparo
from Class_plataforma import *

class Enemigo(Personaje):
    def __init__(self, tamaño: tuple, animaciones: dict, posicion_inicial: tuple, velocidad: int, que_enemigo:str):
        super().__init__(tamaño, animaciones, posicion_inicial, velocidad)
        self.tipo_enemigo = que_enemigo
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        self.animaciones = animaciones
        self.animaciones = reescalar_imagenes(self.animaciones,*tamaño)
        self.contador_pasos = 0
        self.que_hace = "camina"

        self.velocidad = velocidad
        self.rectangulo_principal = animaciones["camina"][0].get_rect()
        self.rectangulo_principal.x = posicion_inicial[0]
        self.rectangulo_principal.y = posicion_inicial[1]
        self.lados = obtener_rectangulos(self.rectangulo_principal)

        self.gravedad = 1
        self.potencia_salto = -19
        self.limite_velocidad_caida = 19
        self.esta_saltando = False
        self.desplazamiento_y = 0

        self.esta_muerto = False
        self.tiempo_ataque = 0

        self.disparo = True
        self.lista_proyectiles = []

    def update(self, pantalla: pygame.Surface, lista_plataformas, tiempo_actual, personaje_principal:Personaje, lista_items):
        match self.que_hace:
            case "camina":
                if not self.esta_saltando:
                    self.animar_personaje(pantalla,"camina")
                self.mover(self.velocidad, pantalla, lista_plataformas)  
            case "camina_izquierda":
                if not self.esta_saltando:
                    self.animar_personaje(pantalla,"camina_izquierda")
                self.mover(self.velocidad *-1, pantalla, lista_plataformas)
            case "salta":
                if not self.esta_saltando:
                    self.esta_saltando = True
                    self.desplazamiento_y = self.potencia_salto
            case "muere":
                self.animar_personaje(pantalla,"muere")
        
        self.aplicar_gravedad(pantalla,self.que_hace)
        self.detectar_colisiones(lista_plataformas, pantalla, tiempo_actual, personaje_principal, lista_items)
    
    # def lanzar_proyectil(self):
    #     x = None
    #     margen = 47
    #     y = self.rectangulo_principal.centery - 5
    #     if self.que_hace == "camina":
    #         x = self.rectangulo_principal.right - margen
    #     elif self.que_hace == "camina_izquierda":
    #         x = self.rectangulo_principal.left - 100 + margen
    #     if x != None:
    #         self.lista_proyectiles.append(Disparo(x,y,self.que_hace))


    def mover(self, velocidad, pantalla: pygame.Surface, lista_plataformas: list):
        nueva_posicion = self.rectangulo_principal.x + velocidad
        if nueva_posicion >= 0 and nueva_posicion <= (pantalla.get_width() - self.rectangulo_principal.width):
            for lado in self.lados:
                self.lados[lado].x += velocidad

        if nueva_posicion >= (pantalla.get_width() - self.rectangulo_principal.width):  
            self.que_hace = "camina_izquierda"
        elif nueva_posicion <= 0:
            self.que_hace = "camina"
        
        for plataforma in lista_plataformas:
            if self.rectangulo_principal.bottom == plataforma.lados["top"].top and plataforma.ancho > 80:
                if self.lados["right"].colliderect(plataforma.limite_derecho):
                    self.que_hace = "camina_izquierda"
                elif self.lados["left"].colliderect(plataforma.limite_izquierdo):
                    self.que_hace = "camina"                  

    def aplicar_gravedad(self, pantalla: pygame.Surface, que_hace: str):
        super().aplicar_gravedad(pantalla, que_hace)

    @staticmethod
    def crear_enemigo(cantidad:int, tamaño:tuple,diccionario_enemigo:dict, velocidad:int, que_enemigo:str): #ver como pametrizar los limites
        lista = []
        for i in range(cantidad):
            x = random.randrange(0,1240,300) #de que rango a que rango y cada cuandos intervalos (60)
            y = random.randrange(-1000,0,50)
            nuevo_enemigo = Enemigo((50,70),diccionario_enemigo,(x,y),velocidad,que_enemigo)
            lista.append(nuevo_enemigo)
        return lista

    def mostrar_premio_enemigo(self,lista_items_actual:list):
        if self.tipo_enemigo == "boss":
            premio = Item(r"juego segundo parcial\Mi Pygame\Sprites\items\esmeralda.png",(self.rectangulo_principal.x,self.rectangulo_principal.y),(50,50),"esmeralda")
        else:
            premio = Item(r"juego segundo parcial\Mi Pygame\Sprites\items\gema.png",(self.rectangulo_principal.x,self.rectangulo_principal.y),(25,25),"gema")
        lista_items_actual.append(premio)    

    def reciclar_enemigo(self, pantalla):
        self.rectangulo_principal.x = random.randrange(70,1250,60)
        self.rectangulo_principal.y = random.randrange(-1000,-80,50) 
        self.lados = obtener_rectangulos(self.rectangulo_principal)
        self.aplicar_gravedad(pantalla,self.que_hace)
        self.que_hace = "camina"

    def detectar_colisiones(self, lista_plataformas: list,pantalla, tiempo_actual, personaje_principal:Personaje, lista_items_actual):
        if self.lados["top"].colliderect(personaje_principal.lados["bottom"]):
            personaje_principal.esta_saltando = False
            dic_sonidos_enemigos["muere_globin"].play()
            personaje_principal.puntaje += 20
            self.animar_personaje(pantalla,"muere")
            self.mostrar_premio_enemigo(lista_items_actual)
            self.esta_muerto = True

        elif self.lados["left"].colliderect(personaje_principal.lados["right"]):
            if tiempo_actual - self.tiempo_ataque > 1500:
                dic_sonidos_booger["herido"].play()
                personaje_principal.animar_personaje(pantalla,"herido")
                if personaje_principal.vidas > 0:
                    personaje_principal.vidas -= 1
                if personaje_principal.cantidad_gemas > 0 and personaje_principal.cantidad_gemas < 6:
                    personaje_principal.cantidad_gemas = 0
                elif personaje_principal.cantidad_gemas > 5:
                    personaje_principal.cantidad_gemas -= 5
                self.tiempo_ataque = tiempo_actual

        elif self.lados["right"].colliderect(personaje_principal.lados["left"]):
            if tiempo_actual - self.tiempo_ataque > 1500:
                dic_sonidos_booger["herido"].play()
                personaje_principal.animar_personaje(pantalla,"herido")
                if personaje_principal.vidas > 0:
                    personaje_principal.vidas -= 1
                if personaje_principal.cantidad_gemas > 0 and personaje_principal.cantidad_gemas < 6:
                    personaje_principal.cantidad_gemas = 0
                elif personaje_principal.cantidad_gemas > 5:
                    personaje_principal.cantidad_gemas -= 5
                self.tiempo_ataque = tiempo_actual

        for plataforma in lista_plataformas:
            if self.lados["bottom"].colliderect(plataforma.lados["top"]):
                self.rectangulo_principal.bottom = plataforma.lados["top"].top 
                self.lados = obtener_rectangulos(self.rectangulo_principal)
                self.esta_saltando = False

            elif self.lados["right"].colliderect(plataforma.lados["left"]):
                self.rectangulo_principal.right = plataforma.lados["left"].left
                self.que_hace = "camina_izquierda"
                self.lados = obtener_rectangulos(self.rectangulo_principal)
                break

            elif self.lados["left"].colliderect(plataforma.lados["right"]):
                self.rectangulo_principal.left = plataforma.lados["right"].right
                self.que_hace = "camina"
                self.lados = obtener_rectangulos(self.rectangulo_principal)
                break



class Boss(Enemigo):
    def __init__(self, tamaño: tuple, animaciones: dict, posicion_inicial: tuple, velocidad: int, que_enemigo: str):
        super().__init__(tamaño, animaciones, posicion_inicial, velocidad, que_enemigo)
        self.esta_muerto = False
        self.tiempo_ataque = 0
        self.vidas = 100

    def mover(self, velocidad, pantalla: pygame.Surface, lista_plataformas: list):
        super().mover(velocidad,pantalla,lista_plataformas)



    def update(self, pantalla: pygame.Surface, lista_plataformas, tiempo_actual, personaje_principal:Personaje, lista_items_actual):
        match self.que_hace:
            case "camina":
                self.animar_personaje(pantalla,"camina")
                self.mover(self.velocidad, pantalla, lista_plataformas)  
            case "camina_izquierda":
                self.animar_personaje(pantalla,"camina_izquierda")
                self.mover(self.velocidad *-1, pantalla, lista_plataformas)
            
        self.detectar_colisiones(lista_plataformas,pantalla,tiempo_actual,personaje_principal,lista_items_actual)

    def detectar_colisiones(self, lista_plataformas: list, pantalla, tiempo_actual, personaje_principal: Personaje, lista_items_actual):
        
        for plataforma in lista_plataformas:
            if self.lados["bottom"].colliderect(plataforma.lados["top"]):
                self.rectangulo_principal.bottom = plataforma.lados["top"].top 
                self.lados = obtener_rectangulos(self.rectangulo_principal)
                self.esta_saltando = False
            if not plataforma.esta_visible:
                for limite in plataforma.limites_boss:
                    if self.que_hace == "camina" and self.lados["right"].colliderect(plataforma.limites_boss[limite]):
                        self.atacar(pantalla,lista_plataformas,personaje_principal, tiempo_actual)
                    elif self.que_hace == "camina_izquierda" and self.lados["left"].colliderect(plataforma.limites_boss[limite]):
                        self.atacar(pantalla,lista_plataformas,personaje_principal, tiempo_actual)

        if self.lados["top"].colliderect(personaje_principal.lados["bottom"]):
            personaje_principal.esta_saltando = False
            if self.vidas > 10:
                self.vidas -= 10
            else:
                self.esta_muerto = True
                self.animar_personaje(pantalla,"muere")
                self.mostrar_premio_enemigo(lista_items_actual)
            #dic_sonidos_enemigos["muere_globin"].play()
            #self.mostrar_premio_enemigo(lista_items_actual)
            #self.esta_muerto = True

        elif self.lados["left"].colliderect(personaje_principal.lados["right"]):
            if tiempo_actual - self.tiempo_ataque > 1500:
                dic_sonidos_booger["herido"].play()
                personaje_principal.animar_personaje(pantalla,"herido")
                if personaje_principal.vidas > 0:
                    personaje_principal.vidas -= 1
                if personaje_principal.cantidad_gemas > 0 and personaje_principal.cantidad_gemas < 6:
                    personaje_principal.cantidad_gemas = 0
                elif personaje_principal.cantidad_gemas > 5:
                    personaje_principal.cantidad_gemas -= 5
                self.tiempo_ataque = tiempo_actual

        elif self.lados["right"].colliderect(personaje_principal.lados["left"]):
            if tiempo_actual - self.tiempo_ataque > 1500:
                dic_sonidos_booger["herido"].play()
                personaje_principal.animar_personaje(pantalla,"herido")
                if personaje_principal.vidas > 0:
                    personaje_principal.vidas -= 1
                if personaje_principal.cantidad_gemas > 0 and personaje_principal.cantidad_gemas < 6:
                    personaje_principal.cantidad_gemas = 0
                elif personaje_principal.cantidad_gemas > 5:
                    personaje_principal.cantidad_gemas -= 5
                self.tiempo_ataque = tiempo_actual

    def atacar(self, pantalla, lista_plataformas:list, personaje_principal:Personaje, tiempo_actual):
        velocidad_anterior = self.velocidad
        self.velocidad = 0
        if tiempo_actual - self.tiempo_ataque > 1500:
            if self.que_hace == "camina":
                self.animar_personaje(pantalla,"ataca")
            else:
                self.animar_personaje(pantalla,"ataca_izquierda")
            if personaje_principal.rectangulo_principal.bottom == lista_plataformas[0].lados["top"].top:
                if personaje_principal.vidas > 0:
                    dic_sonidos_booger["herido"].play()
                    personaje_principal.vidas -= 1
        self.tiempo_ataque = tiempo_actual
        self.velocidad = velocidad_anterior


        
    