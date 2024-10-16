from Material_UI.UI.GUI_form import *
from Material_UI.UI.GUI_button_image import *
from manejador_niveles import Manejador_niveles
from Material_UI.UI.form_contenedor_nivel import FormContenedorNivel



class FormMenuPlay(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border, border_size, active, path_image):
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active)
        self.manejador_niveles = Manejador_niveles(self._master)
        aux_image = pygame.image.load(path_image)
        aux_image = pygame.transform.scale(aux_image,(w,h))
        self._slave = aux_image

        self._btn_nivel_1 = Button_Image(self._slave,100,100,x-200,y+100,75,75,r"juego segundo parcial\Mi Pygame\Sprites\fuentes\1.png",self.entrar_nivel,"nivel_uno")
        self._btn_nivel_2 = Button_Image(self._slave,250,100,x-100,y+100,75,75,r"juego segundo parcial\Mi Pygame\Sprites\fuentes\2.png",self.entrar_nivel,"nivel_dos")
        self._btn_nivel_3 = Button_Image(self._slave,400,100,x,y+100,75,75,r"juego segundo parcial\Mi Pygame\Sprites\fuentes\3.png",self.entrar_nivel,"nivel_tres")
        self._btn_home = Button_Image(self._slave, 400,400, x,y, 50,50, r"juego segundo parcial\Mi Pygame\Material_UI\Recursos\home.png", self.btn_home_click,"")


        self.lista_widgets.append(self._btn_nivel_1)
        self.lista_widgets.append(self._btn_nivel_2)
        self.lista_widgets.append(self._btn_nivel_3)
        self.lista_widgets.append(self._btn_home)
        

    def on(self,parametro):
        print("hola", parametro)

    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            for widget in self.lista_widgets:
                widget.update(lista_eventos)
            self.draw()
        else:
            self.hijo.update(lista_eventos)

    def entrar_nivel(self, nombre_nivel):
        print("deberia entrar al nivel")
        nivel = self.manejador_niveles.get_nivel(nombre_nivel)
        form_contenedor_nivel = FormContenedorNivel(self._master, nivel)
        self.show_dialog(form_contenedor_nivel)

    def btn_home_click(self, param):
        self.end_dialog()