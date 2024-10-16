import pygame, sys
from Configuraciones import renderizar_texto
from Boton import Boton 

class Boton_pausa(Boton):
    def __init__(self, pantalla: pygame.Surface, path_imagen: str, tamaño: tuple, posicion:tuple, path_imagen_click=""):
        super().__init__(pantalla, path_imagen, tamaño, posicion, path_imagen_click)
        self.pausa = False

    def pausar(self, tiempo_al_pausar):
        mensaje_pausa = renderizar_texto("Juego pausado","Arial",(100,255,10),50)
        self.pausa = True
        pygame.mixer.init()
        pygame.mixer.music.pause()
        while self.pausa:
            self.pantalla_master.blit(mensaje_pausa,(470,300))
            pygame.display.update()
            eventos = pygame.event.get()
            for evento in eventos:
                if evento.type == pygame.QUIT:
                    self.pausa = not self.pausa
                    pygame.quit()
                    sys.exit(0)
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    if evento.button == 1:
                        click_position = evento.pos
                        if self.rectangulo.collidepoint(click_position):
                            pygame.mixer.music.unpause()
                            self.pausa = not self.pausa
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        pygame.mixer.music.unpause()               
                        self.pausa = not self.pausa
        tiempo_de_pausado = pygame.time.get_ticks() - tiempo_al_pausar
        return tiempo_de_pausado
