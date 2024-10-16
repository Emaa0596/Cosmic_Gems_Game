import pygame
from nivel import *
from Configuraciones import *


class Nivel_uno(Nivel):
    def __init__(self, pantalla: pygame.Surface):
        #PANTALLA
        W = pantalla.get_width()
        H = pantalla.get_height()
        
        
        fondo = pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Fondos\5_sin_marca.jpg")
        fondo = pygame.transform.scale(fondo,(W,H))
        mi_personaje = Personaje((70,90),diccionario_personaje,(100,400),10)
        musica = r"juego segundo parcial\Mi Pygame\Sprites\sonidos\1.wav"
        
        plataforma_piso = Plataforma((ANCHO,20),(0,400),False)
        plataforma_piso.rectangulo.top = mi_personaje.lados["main"].bottom
        plataforma_piso.lados = obtener_rectangulos(plataforma_piso.rectangulo)
        plataforma_dos = Plataforma((300,90),(ANCHO-298,308),True, r"juego segundo parcial\Mi Pygame\Sprites\plataformas\plataforma_toki.png") #298
        plataforma_dos.girar_plataforma(True,False)
        plataforma_tres = Plataforma((80,50),(ANCHO//2 -20,ALTO//2 +80),True, r"juego segundo parcial\Mi Pygame\Sprites\plataformas\0.png")
        plataforma_cuatro = Plataforma((80,50),(ANCHO-100,111),True, r"juego segundo parcial\Mi Pygame\Sprites\plataformas\0.png")
        plataforma_cinco = Plataforma((300,90),(-1,308),True, r"juego segundo parcial\Mi Pygame\Sprites\plataformas\plataforma_toki.png")
        plataforma_seis = Plataforma((60,60),(100,90),True,r"juego segundo parcial\Mi Pygame\Sprites\plataformas\caja.png",True,r"juego segundo parcial\Mi Pygame\Sprites\plataformas\picante.png")
        plataforma_siete = Plataforma((450,80),(450,115),True, r"juego segundo parcial\Mi Pygame\Sprites\plataformas\lava1.png")
        plataforma_puerta = Plataforma((110,120),(25,350),True,r"juego segundo parcial\Mi Pygame\Sprites\plataformas\puerta.png",True,r"juego segundo parcial\Mi Pygame\Sprites\plataformas\puerta_abierta.png")
        lista_plataformas = [plataforma_piso,plataforma_dos,plataforma_tres,plataforma_cuatro,plataforma_cinco,plataforma_seis,plataforma_siete,plataforma_puerta]

        item_uno = Item(r"juego segundo parcial\Mi Pygame\Sprites\items\gema.png",(1200,40),(25,25),"gema")
        item_dos = Item(r"juego segundo parcial\Mi Pygame\Sprites\items\gema.png",(1225,40),(25,25),"gema")
        item_tres = Item(r"juego segundo parcial\Mi Pygame\Sprites\items\gema.png",(1250,40),(25,25),"gema")
        item_cuatro = Item(r"juego segundo parcial\Mi Pygame\Sprites\items\gema.png",(1275,50),(25,25),"gema")
        item_cinco = Item(r"juego segundo parcial\Mi Pygame\Sprites\items\gema.png",(1175,50),(25,25),"gema")

        item_seis = Item(r"juego segundo parcial\Mi Pygame\Sprites\items\gema.png",(525,70),(25,25),"gema")
        item_siete = Item(r"juego segundo parcial\Mi Pygame\Sprites\items\gema.png",(575,70),(25,25),"gema")
        item_ocho = Item(r"juego segundo parcial\Mi Pygame\Sprites\items\gema.png",(625,70),(25,25),"gema")
        item_nueve = Item(r"juego segundo parcial\Mi Pygame\Sprites\items\gema.png",(675,70),(25,25),"gema")
        item_diez = Item(r"juego segundo parcial\Mi Pygame\Sprites\items\gema.png",(725,70),(25,25),"gema")
        item_once = Item(r"juego segundo parcial\Mi Pygame\Sprites\items\gema.png",(775,70),(25,25),"gema")

        item_vida = Item(r"juego segundo parcial\Mi Pygame\Sprites\items\vida.png",(1250,10),(25,25),"vida")

        lista_items = [item_uno, item_dos, item_tres,item_cuatro,item_cinco, item_vida,
                    item_seis,item_siete,item_ocho,item_nueve,item_diez,item_once]

        globin_uno = Enemigo((50,70),diccionario_goblin,(plataforma_dos.rectangulo.x,plataforma_dos.rectangulo.y -71),3,"globin")
        globin_dos = Enemigo((50,70),diccionario_goblin,(plataforma_cinco.rectangulo.x,plataforma_cinco.rectangulo.y -71),3,"globin")
        globin_tres = Enemigo((50,70),diccionario_goblin,(plataforma_piso.rectangulo.x + 1000,plataforma_piso.rectangulo.y -71),3,"globin")
        globin_cuatro = Enemigo((50,70),diccionario_goblin,(plataforma_siete.rectangulo.x,plataforma_siete.rectangulo.y -71),3,"globin")
        globin_cinco = Enemigo((50,70),diccionario_goblin,(plataforma_siete.rectangulo.x + 300,plataforma_siete.rectangulo.y -71),3,"globin")
        lista_enemigos = [globin_uno,globin_dos,globin_tres,globin_cuatro,globin_cinco]



        super().__init__(pantalla, mi_personaje,lista_plataformas,lista_enemigos,lista_items,fondo, musica,nivel_actual="uno")