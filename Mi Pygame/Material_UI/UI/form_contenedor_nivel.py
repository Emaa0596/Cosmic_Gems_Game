import pygame
from Material_UI.UI.GUI_form import *
from Material_UI.UI.GUI_button_image import *

class FormContenedorNivel(Form):
    def __init__(self, pantalla:pygame.Surface, nivel):
        super().__init__(pantalla, 0,0, pantalla.get_width(),pantalla.get_height(),"Green")
        nivel._slave = self._slave
        self.nivel = nivel
        self._btn_home = Button_Image(self._slave, self._x,self._y, self._w -100, self._h -100, 50,50,r"juego segundo parcial\Mi Pygame\Material_UI\Recursos\home.png", self.btn_home_click,"")

        self.lista_widgets.append(self._btn_home)

    def update(self, lista_eventos):
        self.nivel.update(lista_eventos)
        for widget in self.lista_widgets:
            widget.update(lista_eventos)
        self.draw()

    def btn_home_click(self, param):
        self.end_dialog()
