import pygame
from Configuraciones import *
from Items import *
from Class_disparo import Disparo

class Personaje:
    def __init__(self, tamaño:tuple, animaciones:dict , posicion_inicial:tuple, velocidad:int):
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        self.vidas = 3
        self.puntaje = 0
        self.cantidad_gemas = 0
        #animaciones
        self.animaciones = animaciones
        self.animaciones = reescalar_imagenes(self.animaciones,*tamaño)
        self.que_hace = "quieto"
        self.contador_pasos = 0 
        #gravedad y salto
        self.gravedad = 1
        self.potencia_salto = -18
        self.limite_velocidad_caida = 18
        self.esta_saltando = False
        self.desplazamiento_y = 0

        self.velocidad = velocidad
        self.rectangulo_principal = animaciones["quieto"][0].get_rect()
        self.rectangulo_principal.x = posicion_inicial[0]
        self.rectangulo_principal.y = posicion_inicial[1]
        #hitbox
        self.lados = obtener_rectangulos(self.rectangulo_principal)

        #PODERES
        self.tiempo_habilidad = 10000
        self.tiempo_anterior = 0
        self.vuela = False
        self.disparo = False
        self.lista_proyectiles = []

        self.ganador = False
        self.nivel_actual = ""
        #self.ultimo_movimiento = ""
     

    def update(self,pantalla:pygame.Surface,lista_plataformas, lista_items, lista_enemigos):
        if self.cantidad_gemas > 0:
            self.disparo = True
        else:
            self.disparo = False

        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual > self.tiempo_habilidad + self.tiempo_anterior:
            self.vuela = False

        match self.que_hace:       
            case "camina":
                if not self.esta_saltando:
                    self.animar_personaje(pantalla,"camina")
                self.mover(self.velocidad, pantalla, lista_plataformas,lista_items)  

            case "camina_izquierda":
                if not self.esta_saltando:
                    self.animar_personaje(pantalla,"camina_izquierda")
                self.mover(self.velocidad *-1, pantalla, lista_plataformas,lista_items)

            case "agachado": 
                if not self.esta_saltando:
                    self.animar_personaje(pantalla,"agachado")

            case "quieto":
                if not self.esta_saltando:
                    self.animar_personaje(pantalla,"quieto")

            case "quieto_izquierda":
                if not self.esta_saltando:
                    self.animar_personaje(pantalla,"quieto_izquierda")

            case "salta":
                if not self.esta_saltando or self.vuela:
                    self.esta_saltando = True
                    if not self.vuela:
                        dic_sonidos_booger["salta"].play()
                        self.potencia_salto = -18
                        self.vuela = False
                    else:
                        self.vuela = True
                        self.potencia_salto = -5
                    self.desplazamiento_y = self.potencia_salto

            case "salta_derecha":
                if not self.esta_saltando or self.vuela:
                    self.esta_saltando = True
                    if not self.vuela:
                        dic_sonidos_booger["salta"].play()
                        self.animar_personaje(pantalla,"salta")

                        self.potencia_salto = -18
                        self.vuela = False
                    else:
                        self.vuela = True
                        self.potencia_salto = -5
                    self.desplazamiento_y = self.potencia_salto
                self.mover(self.velocidad, pantalla, lista_plataformas,lista_items)

            case "salta_izquierda":
                if not self.esta_saltando or self.vuela:
                    self.esta_saltando = True
                    if not self.vuela:
                        dic_sonidos_booger["salta"].play()
                        self.vuela = False
                        self.animar_personaje(pantalla,"salta_izquierda")
                        self.potencia_salto = -18
                    else:
                        self.vuela = True
                        self.potencia_salto = -5

                    self.desplazamiento_y = self.potencia_salto
                self.mover(self.velocidad *-1, pantalla, lista_plataformas,lista_items)
        
        # if self.que_hace != "quieto" and self.que_hace != "quieto_izquierda":
        #     self.ultimo_movimiento = self.que_hace
        self.aplicar_gravedad(pantalla,self.que_hace)
        self.detectar_colisiones(lista_plataformas, lista_items)
        self.detectar_colisiones_items(lista_items)
        Disparo.actualizar_proyectil(pantalla,self.lista_proyectiles,lista_enemigos,lista_plataformas, lista_items)
        
    def animar_personaje(self,pantalla:pygame.Surface, que_animacion:str):
        animacion = self.animaciones[que_animacion]
        largo = len(self.animaciones[que_animacion])
        if self.contador_pasos >= largo:
            self.contador_pasos = 0   
        pantalla.blit(animacion[self.contador_pasos], self.lados["main"])
        self.contador_pasos += 1

    def mover(self,velocidad, pantalla:pygame.Surface , lista_plataformas:list,lista_items):
        
        nueva_posicion = self.rectangulo_principal.x + velocidad
        if nueva_posicion >= 0 and nueva_posicion <= (pantalla.get_width() - self.rectangulo_principal.width):
            for lado in self.lados:
                self.lados[lado].x += velocidad
                
        self.detectar_colisiones(lista_plataformas, lista_items)
        

    def aplicar_gravedad(self,pantalla:pygame.Surface,que_hace:str):
        if self.esta_saltando and not self.vuela:
            if que_hace == "camina_izquierda" or que_hace == "quieto_izquierda":
                self.animar_personaje(pantalla,"salta_izquierda")
            elif que_hace != "camina_izquierda" and que_hace != "salta_izquierda" and que_hace != "quieto_izquierda":
                self.animar_personaje(pantalla,"salta")
            elif que_hace == "salta_izquierda":
                self.animar_personaje(pantalla,"salta_izquierda")

        if self.vuela and self.esta_saltando:
            if que_hace == "camina_izquierda":

                dic_sonidos_booger["vuela"].play()
                self.animar_personaje(pantalla,"vuela_izquierda")
            elif que_hace != "camina_izquierda" and que_hace != "salta_izquierda":
                dic_sonidos_booger["vuela"].set_volume(0.2)
                dic_sonidos_booger["vuela"].play()
                self.animar_personaje(pantalla,"vuela")
            elif que_hace == "salta_izquierda":
                dic_sonidos_booger["vuela"].set_volume(0.2)
                dic_sonidos_booger["vuela"].play()
                self.animar_personaje(pantalla,"vuela_izquierda")

        for lado in self.lados:
            self.lados[lado].y += self.desplazamiento_y
    
        if self.desplazamiento_y + self.gravedad < self.limite_velocidad_caida:
            self.desplazamiento_y += self.gravedad


    def detectar_colisiones(self,lista_plataformas:list, lista_items):

        for plataforma in lista_plataformas:
            if self.lados["bottom"].colliderect(plataforma.lados["top"]):
                self.rectangulo_principal.bottom = plataforma.lados["top"].top 
                self.lados = obtener_rectangulos(self.rectangulo_principal)
                self.esta_saltando = False

            elif self.lados["right"].colliderect(plataforma.lados["left"]):
                self.rectangulo_principal.right = plataforma.lados["left"].left
                self.lados = obtener_rectangulos(self.rectangulo_principal)

            elif self.lados["left"].colliderect(plataforma.lados["right"]):
                self.rectangulo_principal.left = plataforma.lados["right"].right
                self.lados = obtener_rectangulos(self.rectangulo_principal)

            elif self.lados["top"].colliderect(plataforma.lados["bottom"]):
                self.desplazamiento_y = self.limite_velocidad_caida

                self.lados = obtener_rectangulos(self.rectangulo_principal)
                
                if plataforma.tiene_premio:
                    plataforma.premio_descubierto = True
                    plataforma.tiene_premio = False
                    plataforma.agregar_item(lista_items,self.nivel_actual)
       

    def lanzar_proyectil(self):
        x = None
        margen = 47
        y = self.rectangulo_principal.centery - 5
        if self.que_hace == "camina" or self.que_hace == "quieto" or self.que_hace == "salta" or self.que_hace == "salta_derecha":
            x = self.rectangulo_principal.right - margen
        elif self.que_hace == "camina_izquierda" or self.que_hace == "salta_izquierda" or self.que_hace == "quieto_izquierda":
            x = self.rectangulo_principal.left - 100 + margen
        
        if x != None:
            dic_sonidos_booger["dispara"].play()
            self.lista_proyectiles.append(Disparo(x,y,self.que_hace))

    def detectar_colisiones_items(self, lista_items:list):
        if len(lista_items) > 0:
            for item in lista_items:
                if self.rectangulo_principal.colliderect(item.rectangulo):
                    match item.que_item:
                        case "gema":
                            self.puntaje += 10
                            self.cantidad_gemas += 1
                            lista_items.remove(item)
                            del item
                        case "vida":
                            self.vidas +=1
                            self.puntaje += 50
                            lista_items.remove(item)
                            del item
                        case "picante":
                            self.puntaje += 50
                            self.tiempo_anterior = pygame.time.get_ticks()
                            self.vuela = True
                            lista_items.remove(item)
                            del item 
                        case "puerta":
                            if self.cantidad_gemas > 4:
                                self.ganador = True    
                        case "esmeralda":
                            if self.cantidad_gemas > 4:
                                dic_sonidos_booger["gana"].play()
                                self.puntaje += 100
                                self.ganador = True  

