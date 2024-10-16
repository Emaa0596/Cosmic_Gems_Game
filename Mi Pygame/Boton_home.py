import pygame,sys
from Boton import Boton
from Configuraciones import renderizar_texto

class Boton_home(Boton):
    def __init__(self, pantalla: pygame.Surface, path_imagen: str, tamaño: tuple, posicion: tuple, path_imagen_click=""):
        super().__init__(pantalla, path_imagen, tamaño, posicion, path_imagen_click)
        self.active = False
        self.ventana = pygame.image.load(r"juego segundo parcial\Mi Pygame\Material_UI\Recursos\Window.png")
        self.ventana = pygame.transform.scale(self.ventana,(800,500))
        self.rectangulo_ventana = self.ventana.get_rect()
        self.rectangulo_ventana.x = 250
        self.rectangulo_ventana.y = 50
        self.icono_uno = pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\botones\1.png")
        self.icono_dos = pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\botones\2.png")
        self.icono_tres = pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\botones\3.png")
        self.icono_uno = pygame.transform.scale(self.icono_uno,(50,50))
        self.icono_dos = pygame.transform.scale(self.icono_dos,(50,50))
        self.icono_tres = pygame.transform.scale(self.icono_tres,(50,50))
        self.rectangulo_icono_uno = self.icono_uno.get_rect()
        self.rectangulo_icono_uno.x = 526
        self.rectangulo_icono_uno.y = 87 +50
        self.rectangulo_icono_dos = self.icono_uno.get_rect()
        self.rectangulo_icono_dos.x = 576
        self.rectangulo_icono_dos.y = 140 +50

        self.rectangulo_icono_tres = self.icono_uno.get_rect()
        self.rectangulo_icono_tres.x = 635
        self.rectangulo_icono_tres.y = 200 +50

        self.rectangulo_imagen_click = self.imagen_click.get_rect()
        self.rectangulo_imagen_click.x = 305
        self.rectangulo_imagen_click.y = 412 + 50
        self.nivel_actual = ""


    def mostrar_ventana_home(self, tiempo_al_entrar, lista_niveles_superados):
        self.active = True
        mensaje_niveles = renderizar_texto("Nivel bloqueado","candara",(100,255,10),50)
        pygame.mixer.init()
        pygame.mixer.music.pause()
        while self.active:
            self.pantalla_master.blit(self.ventana,(self.rectangulo_ventana.x,self.rectangulo_ventana.y))
            self.pantalla_master.blit(self.icono_uno,(self.rectangulo_icono_uno.x,self.rectangulo_icono_uno.y))
            self.pantalla_master.blit(self.icono_dos,(self.rectangulo_icono_dos.x,self.rectangulo_icono_dos.y))
            self.pantalla_master.blit(self.icono_tres,(self.rectangulo_icono_tres.x,self.rectangulo_icono_tres.y))
            self.pantalla_master.blit(self.imagen_click,(self.rectangulo_imagen_click.x,self.rectangulo_imagen_click.y))
            eventos = pygame.event.get()
            pygame.display.update()
            for evento in eventos:
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        pygame.mixer.music.unpause()
                        self.active = not self.active
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    if evento.button == 1:
                        click_position = evento.pos
                        if self.rectangulo_icono_uno.collidepoint(click_position):
                            self.nivel_actual = "uno"
                            tiempo = pygame.time.get_ticks()
                            pygame.mixer.music.unpause()
                            return tiempo
                        elif self.rectangulo_icono_dos.collidepoint(click_position):
                            if lista_niveles_superados[1] == True:
                                self.nivel_actual = "dos"
                                tiempo = pygame.time.get_ticks()
                                return tiempo
                            else:
                                self.ventana.blit(mensaje_niveles,(300,400))
                        
                        elif self.rectangulo_icono_tres.collidepoint(click_position):
                            if lista_niveles_superados[2] == True:
                                self.nivel_actual = "tres"
                                tiempo = pygame.time.get_ticks()
                                return tiempo
                            else:
                                self.ventana.blit(mensaje_niveles,(300,400))

                        elif self.rectangulo_imagen_click.collidepoint(click_position):
                            pygame.mixer.music.unpause()
                            self.active = False
                    
        pygame.mixer.music.unpause()
        tiempo_de_pausado = pygame.time.get_ticks() - tiempo_al_entrar
        return tiempo_de_pausado
