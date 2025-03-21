import pygame
from pygame.locals import *

from Material_UI.UI.GUI_button_image import *
from Material_UI.UI.GUI_form import *
from Material_UI.UI.GUI_label import *

        
class FormMenuScore(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border, active, path_image, scoreboard, margen_y,margen_x, espacio):
        super().__init__(screen, x,y,w,h,color_background,color_border,active)
        aux_image = pygame.image.load(path_image)
        aux_image = pygame.transform.scale(aux_image,(w,h))
        self._slave = aux_image
        self._score = scoreboard
        self.lista_widgets = []

        self._margen_y = margen_y
        #Creo 2 labels y los agrego a la lista de widgets
        self.lista_widgets.append(
            Label(screen=self._slave, x=margen_x+10,y=20,w=w/2-margen_x-10,h=50,text = "Jugador", font="Verdana",font_size=30,font_color=(255,255,255),path_image=r"juego segundo parcial\Mi Pygame\Material_UI\Recursos\bar.png"))
        self.lista_widgets.append(
            Label(screen=self._slave,
                 x=margen_x+10+w/2-margen_x-10,
                 y=20,w=w/2-margen_x-10,
                 h=50,text = "Puntaje",
                font="Verdana",
                font_size=30,
                font_color=(255,255,255),
                path_image=r"juego segundo parcial\Mi Pygame\Material_UI\Recursos\bar.png"))
        
        pos_inicial_y = margen_y
        
        #Encapsular esta logica en un metodo. Esto nos permite dibujar la tabla en pantalla
        
        
        for j in self._score:
            pos_inicial_x = margen_x
            for n,s in j.items():
                cadena = "" 
                cadena = f"{s}"
                pos = Label(screen=self._slave, x=pos_inicial_x,y=pos_inicial_y,
                            w=w/2-margen_x,h=100,text = cadena, font="Verdana",font_size=30,
                            font_color=(255,255,255),path_image=r"juego segundo parcial\Mi Pygame\Material_UI\Recursos\Table.png")
                self.lista_widgets.append(pos)
                pos_inicial_x += w/2-margen_x
                
            pos_inicial_y+=100 + espacio
                
        
        
        #Crear boton home

        # self.boton_home = Button_Image(self._slave, 
        #                                 w-70, h-70,
        #                                 x, y,
        #                                 50, 50, "Recursos\home.png", 
        #                                 self.btn_home_click, "", "", "Verdana", 15,
        #                                 (0, 255, 0), (0, 255, 0), (255, 255, 255), 2)
        
        self.boton_home = Button_Image(screen = self._slave, x = w - 70, y = h - 70, master_x = x, master_y = y,
                                       w = 50, h = 50, color_background = (255, 0, 0),
                                       color_border = (255, 0, 255),
                                       onclick = self.btn_home_click,
                                       onclick_param = "",
                                       text = "",
                                       font = "Verdana",
                                       font_size = 15,
                                       font_color = (0, 255, 0),
                                       path_image = r"juego segundo parcial\Mi Pygame\Material_UI\Recursos\home.png")
        

        self.lista_widgets.append(self.boton_home)
        
    def btn_home_click(self,parametro):
        self.end_dialog()
    
    def update(self, lista_eventos):
        if self.active:
            for widget in self.lista_widgets:
                widget.update(lista_eventos)
            self.draw()
            