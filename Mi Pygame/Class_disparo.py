import pygame
from Configuraciones import dic_sonidos_enemigos

class Disparo():
    def __init__(self, x, y, direccion:str) -> None:
        self.superficie = pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Poder_moco\5.png")
        self.superficie = pygame.transform.scale(self.superficie,(10,10))
        self.rectangulo = self.superficie.get_rect()
        self.rectangulo.x = x
        self.rectangulo.centery = y
        self.direccion = direccion


    def actualizar(self, pantalla):
        if self.direccion == "camina" or self.direccion == "quieto" or self.direccion == "salta" or self.direccion == "salta_derecha":
            self.rectangulo.x += 30
        elif self.direccion == "camina_izquierda" or self.direccion == "salta_izquierda" or self.direccion == "quieto_izquierda":
            self.rectangulo.x -= 30

        pantalla.blit(self.superficie, self.rectangulo)


    @staticmethod
    def actualizar_proyectil(pantalla:pygame.Surface, lista_proyectiles:list, lista_enemigos:list, lista_plataformas:list, lista_items_actual):
        i = 0
        while i < len(lista_proyectiles):
            proyectil = lista_proyectiles[i]
            proyectil.actualizar(pantalla)
            if proyectil.rectangulo.centerx < 0 or proyectil.rectangulo.centerx > pantalla.get_width():
                try:
                    lista_proyectiles.pop(i)
                except IndexError:
                    break

            for enemigo in lista_enemigos:
                if proyectil.rectangulo.colliderect(enemigo.rectangulo_principal) and enemigo.tipo_enemigo != "boss":
                    dic_sonidos_enemigos["muere_globin"].play()
                    enemigo.animar_personaje(pantalla,"muere")
                    enemigo.esta_muerto = True
                    try:
                        lista_proyectiles.pop(i)
                    except IndexError:
                        break
                elif proyectil.rectangulo.colliderect(enemigo.rectangulo_principal) and enemigo.tipo_enemigo == "boss":
                    if enemigo.vidas > 5:
                        enemigo.vidas -= 5
                    else:
                        enemigo.esta_muerto = True
                        enemigo.animar_personaje(pantalla,"muere")
                        enemigo.mostrar_premio_enemigo(lista_items_actual)

                    try:
                        lista_proyectiles.pop(i)
                    except IndexError:
                        break


            for plataforma in lista_plataformas:
                if proyectil.rectangulo.colliderect(plataforma.rectangulo):
                    try:
                        lista_proyectiles.pop(i)
                    except IndexError:
                        break
            i += 1
