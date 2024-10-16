import pygame,random
#from Class_enemigo import *
from Class_enemigo import *


class Nivel:
    def __init__(self, pantalla , personaje_principal:Personaje, lista_plataformas,lista_enemigos,lista_items, imagen_fondo, musica, nivel_actual:str):
        self.slave = pantalla
        self.mi_personaje = personaje_principal
        self.plataformas = lista_plataformas
        self.enemigos = lista_enemigos
        self.lista_items = lista_items
        self.img_fondo = imagen_fondo
        self.tiempo_actual = 0
        self.tiempo_disparo = 0
        self.debug = False
        self.musica = musica
        self.nivel_actual = nivel_actual
        self.mi_personaje.nivel_actual = self.nivel_actual

    def update(self,lista_eventos):
        for evento in lista_eventos:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_TAB:
                    self.cambiar_modo()   
        
        self.leer_inputs()
        self.actualizar_pantalla()

    def actualizar_pantalla(self):
        self.slave.blit(self.img_fondo,(0,0))

        for plataforma in self.plataformas:
            if plataforma.esta_visible:
                self.slave.blit(plataforma.superficie_plataforma,(plataforma.rectangulo.x,plataforma.rectangulo.y))

        self.mi_personaje.update(self.slave,self.plataformas, self.lista_items, self.enemigos)

        enemigos_a_eliminar = []
        for enemigo in self.enemigos:
            enemigo.update(self.slave,self.plataformas,self.tiempo_actual, self.mi_personaje, self.lista_items)
            if enemigo.esta_muerto:
                enemigos_a_eliminar.append(enemigo)

        for enemigo in enemigos_a_eliminar:
            self.enemigos.remove(enemigo)
            del enemigo
        
        if len(self.lista_items) > 0:
            for item in self.lista_items:
                self.slave.blit(item.animacion, (item.rectangulo.x,item.rectangulo.y))

        if len(self.enemigos) <= 1:
            match self.nivel_actual:
                case "uno":
                    nueva_lista = Enemigo.crear_enemigo(4,(50,70),diccionario_goblin,3,"globin")
                case "dos":
                    nueva_lista = Enemigo.crear_enemigo(4,(50,70),dic_miner_globin,6,"m_globin")
                case "tres":
                    globin = random.choice(["globin","m_globin"])
                    if globin == "globin":
                        nueva_lista = Enemigo.crear_enemigo(4,(50,70),diccionario_goblin,4,"globin")
                    else:
                        nueva_lista = Enemigo.crear_enemigo(4,(50,70),dic_miner_globin,8,"m_globin")
            for e in nueva_lista:
                self.enemigos.append(e)

        self.dibujar_rectangulos()


    def leer_inputs(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.mi_personaje.que_hace = "camina"
            if keys[pygame.K_RIGHT and pygame.K_UP]:
                self.mi_personaje.que_hace = "salta_derecha"

        elif keys[pygame.K_LEFT]:
            self.mi_personaje.que_hace = "camina_izquierda"
            if keys[pygame.K_LEFT and pygame.K_UP]:
                self.mi_personaje.que_hace = "salta_izquierda"
            
        elif keys[pygame.K_DOWN]:
            self.mi_personaje.que_hace = "agachado"
        elif keys[pygame.K_UP]:
            self.mi_personaje.que_hace = "salta"   
        else:
            if not "izquierda" in self.mi_personaje.que_hace:
                self.mi_personaje.que_hace = "quieto"
            else:
                self.mi_personaje.que_hace = "quieto_izquierda"

        if self.mi_personaje.disparo and keys[pygame.K_SPACE]:
            if self.tiempo_actual - self.tiempo_disparo > 700:
                self.tiempo_disparo = self.tiempo_actual
                self.mi_personaje.animar_personaje(self.slave,"tira_poder")
                self.mi_personaje.lanzar_proyectil()


    def cambiar_modo(self):
        self.debug = not self.debug

    def get_modo(self):
        return self.debug  

    def dibujar_rectangulos(self):
        if self.get_modo():
            for lado in self.mi_personaje.lados:
                pygame.draw.rect(self.slave,"Blue", self.mi_personaje.lados[lado], 1)

            for plataforma in self.plataformas:
                pygame.draw.rect(self.slave,"Orange",plataforma.limite_derecho,1)
                pygame.draw.rect(self.slave,"Orange",plataforma.limite_izquierdo,1)
                for lado in plataforma.lados:
                    pygame.draw.rect(self.slave,"Orange",plataforma.lados[lado],1)

            for enemigo in self.enemigos:
                for lado in enemigo.lados:
                    pygame.draw.rect(self.slave,"Red",enemigo.lados[lado],1)