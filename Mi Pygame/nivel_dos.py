import pygame
from nivel import *
from Configuraciones import *


class Nivel_dos(Nivel):
    def __init__(self, pantalla: pygame.Surface):
        #PANTALLA
        W = pantalla.get_width()
        H = pantalla.get_height()
    
       
        fondo = pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Fondos\fondo_nivel_dos.jpeg")
        fondo = pygame.transform.scale(fondo,(W,H))
        mi_personaje = Personaje((70,90),diccionario_personaje,(110,330),10)
        musica = r"juego segundo parcial\Mi Pygame\Sprites\sonidos\2.wav"

        pl_dos_dos = Plataforma((ANCHO,90),(0,510),True,r"juego segundo parcial\Mi Pygame\Sprites\plataformas\hielo.png")
        pl_tres_dos = Plataforma((300,90),(1000,200),True,r"juego segundo parcial\Mi Pygame\Sprites\plataformas\5_2.png")
        pl_cuatro_dos = Plataforma((110,70),(ANCHO//2,ALTO//2 +40),True,r"juego segundo parcial\Mi Pygame\Sprites\plataformas\6.png")
        pl_cinco_dos = Plataforma((110,70),(ANCHO//2 -200,ALTO//2 - 100),True,r"juego segundo parcial\Mi Pygame\Sprites\plataformas\6.png")
        pl_seis_dos = Plataforma((300,90),(0,150),True,r"juego segundo parcial\Mi Pygame\Sprites\plataformas\5_2.png")
        pl_seis_dos.girar_plataforma(True,False)
        pl_siete_dos = Plataforma((55,55),(900,175),True,r"juego segundo parcial\Mi Pygame\Sprites\plataformas\caja_violeta.png",True)
        pl_ocho_dos = Plataforma((150,90),(0,420),True,r"juego segundo parcial\Mi Pygame\Sprites\plataformas\6.png")
        plataforma_puerta_dos = Plataforma((110,120),(-3,314),True,r"juego segundo parcial\Mi Pygame\Sprites\plataformas\puerta.png",True,r"juego segundo parcial\Mi Pygame\Sprites\plataformas\puerta_abierta.png")
        lista_plataformas_dos = [pl_dos_dos,pl_tres_dos,pl_cuatro_dos,pl_cinco_dos,pl_seis_dos,pl_siete_dos,pl_ocho_dos,plataforma_puerta_dos]


        globin_uno_dos = Enemigo((50,70),dic_miner_globin,(lista_plataformas_dos[1].rectangulo.x,lista_plataformas_dos[1].rectangulo.y-71),6,"m_globin")
        globin_dos_dos = Enemigo((50,70),dic_miner_globin,(lista_plataformas_dos[4].rectangulo.x,lista_plataformas_dos[4].rectangulo.y-71),6,"m_globin")
        globin_cinco_dos = Enemigo((50,70),dic_miner_globin,(lista_plataformas_dos[4].rectangulo.x + 180,lista_plataformas_dos[4].rectangulo.y-71),6,"m_globin")
        globin_tres_dos = Enemigo((50,70),dic_miner_globin,(lista_plataformas_dos[0].rectangulo.x + 700,lista_plataformas_dos[0].rectangulo.y-71),10,"m_globin")
        globin_cuatro_dos = Enemigo((50,70),dic_miner_globin,(lista_plataformas_dos[0].rectangulo.x + 1200,lista_plataformas_dos[0].rectangulo.y-71),10,"m_globin")
        lista_enemigos_dos = [globin_uno_dos,globin_dos_dos,globin_tres_dos,globin_cuatro_dos,globin_cinco_dos]
        
        item_uno_dos = Item(r"juego segundo parcial\Mi Pygame\Sprites\items\gema.png",(50,40),(25,25),"gema")
        item_dos_dos = Item(r"juego segundo parcial\Mi Pygame\Sprites\items\gema.png",(80,40),(25,25),"gema")
        item_tres_dos = Item(r"juego segundo parcial\Mi Pygame\Sprites\items\gema.png",(105,40),(25,25),"gema")
        item_cuatro_dos = Item(r"juego segundo parcial\Mi Pygame\Sprites\items\gema.png",(130,40),(25,25),"gema")

        item_cinco_dos = Item(r"juego segundo parcial\Mi Pygame\Sprites\items\gema.png",(1000,80),(25,25),"gema")
        item_seis_dos = Item(r"juego segundo parcial\Mi Pygame\Sprites\items\gema.png",(1030,60),(25,25),"gema")
        item_siete_dos = Item(r"juego segundo parcial\Mi Pygame\Sprites\items\gema.png",(1060,60),(25,25),"gema")
        item_ocho_dos = Item(r"juego segundo parcial\Mi Pygame\Sprites\items\gema.png",(1100,60),(25,25),"gema")
        item_nueve_dos = Item(r"juego segundo parcial\Mi Pygame\Sprites\items\gema.png",(1130,60),(25,25),"gema")
        item_diez_dos = Item(r"juego segundo parcial\Mi Pygame\Sprites\items\gema.png",(1160,80),(25,25),"gema")

        item_once_dos = Item(r"juego segundo parcial\Mi Pygame\Sprites\items\gema.png",(700,300),(25,25),"gema")
        item_doce_dos = Item(r"juego segundo parcial\Mi Pygame\Sprites\items\gema.png",(675,300),(25,25),"gema")
        item_trece_dos = Item(r"juego segundo parcial\Mi Pygame\Sprites\items\gema.png",(475,130),(25,25),"gema")
        item_catorce_dos = Item(r"juego segundo parcial\Mi Pygame\Sprites\items\gema.png",(500,130),(25,25),"gema")


        item_quince_dos = Item(r"juego segundo parcial\Mi Pygame\Sprites\items\vida.png",(1245,40),(25,25),"vida")

        lista_items_dos = [item_uno_dos,item_dos_dos,item_tres_dos,item_cuatro_dos,item_cinco_dos,item_seis_dos,
                        item_siete_dos,item_ocho_dos,item_nueve_dos,item_diez_dos,item_once_dos,item_doce_dos,item_trece_dos,item_catorce_dos,
                        item_quince_dos]


        super().__init__(pantalla, mi_personaje,lista_plataformas_dos,lista_enemigos_dos,lista_items_dos,fondo, musica, nivel_actual="dos")