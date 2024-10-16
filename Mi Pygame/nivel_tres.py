import pygame
from nivel import *
from Configuraciones import *


class Nivel_tres(Nivel):
    def __init__(self, pantalla: pygame.Surface):
        #PANTALLA
        W = pantalla.get_width()
        H = pantalla.get_height()
       
        fondo = pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Fondos\4.jpg")
        fondo = pygame.transform.scale(fondo,(W,H))
        mi_personaje = Personaje((70,90),diccionario_personaje,(110,490),10)
        musica = r"juego segundo parcial\Mi Pygame\Sprites\sonidos\4.wav"

        pl_final_piso = Plataforma((ANCHO,20),(0,580),False)
        pl_final_uno = Plataforma((55,55),(800,250),True,r"juego segundo parcial\Mi Pygame\Sprites\plataformas\caja_celeste.png",True)
        pl_final_once = Plataforma((55,55),(900,250),True,r"juego segundo parcial\Mi Pygame\Sprites\plataformas\caja_celeste.png",True)
        pl_final_doce = Plataforma((55,55),(1000,250),True,r"juego segundo parcial\Mi Pygame\Sprites\plataformas\caja_celeste.png",True)
        pl_final_trece = Plataforma((55,55),(1100,250),True,r"juego segundo parcial\Mi Pygame\Sprites\plataformas\caja_celeste.png",True)
        pl_final_catorce = Plataforma((55,55),(1200,250),True,r"juego segundo parcial\Mi Pygame\Sprites\plataformas\caja_celeste.png",True)

        pl_final_dos = Plataforma((55,55),(0,250),True,r"juego segundo parcial\Mi Pygame\Sprites\plataformas\caja_celeste.png",True)
        pl_final_ocho = Plataforma((55,55),(100,250),True,r"juego segundo parcial\Mi Pygame\Sprites\plataformas\caja_celeste.png",True)
        pl_final_tres = Plataforma((55,55),(200,250),True,r"juego segundo parcial\Mi Pygame\Sprites\plataformas\caja_celeste.png",True)
        pl_final_cuatro = Plataforma((55,55),(300,250),True,r"juego segundo parcial\Mi Pygame\Sprites\plataformas\caja_celeste.png",True)
        pl_final_cinco = Plataforma((55,55),(400,250),True,r"juego segundo parcial\Mi Pygame\Sprites\plataformas\caja_celeste.png",True)

        pl_final_nueve = Plataforma((80,50),(650,400),True, r"juego segundo parcial\Mi Pygame\Sprites\plataformas\0.png")
        pl_final_diez = Plataforma((80,50),(470,220),True, r"juego segundo parcial\Mi Pygame\Sprites\plataformas\0.png")

        divisor_uno = Plataforma((45,8),(55,250),True, r"juego segundo parcial\Mi Pygame\Sprites\plataformas\divisor.png")
        divisor_dos = Plataforma((45,8),(155,250),True, r"juego segundo parcial\Mi Pygame\Sprites\plataformas\divisor.png")
        divisor_tres = Plataforma((45,8),(255,250),True, r"juego segundo parcial\Mi Pygame\Sprites\plataformas\divisor.png")
        divisor_cuatro = Plataforma((45,8),(355,250),True, r"juego segundo parcial\Mi Pygame\Sprites\plataformas\divisor.png")

        divisor_cinco = Plataforma((45,8),(855,250),True, r"juego segundo parcial\Mi Pygame\Sprites\plataformas\divisor.png")
        divisor_seis = Plataforma((45,8),(1255,250),True, r"juego segundo parcial\Mi Pygame\Sprites\plataformas\divisor.png")
        divisor_siete = Plataforma((45,8),(955,250),True, r"juego segundo parcial\Mi Pygame\Sprites\plataformas\divisor.png")
        divisor_ocho = Plataforma((45,8),(1055,250),True, r"juego segundo parcial\Mi Pygame\Sprites\plataformas\divisor.png")
        divisor_nueve = Plataforma((45,8),(1155,250),True, r"juego segundo parcial\Mi Pygame\Sprites\plataformas\divisor.png")

        plataformas_final = [pl_final_piso,pl_final_uno,pl_final_dos,pl_final_tres,pl_final_cuatro,pl_final_cinco,pl_final_ocho,
                            pl_final_nueve,pl_final_diez,pl_final_once,pl_final_doce,pl_final_trece,pl_final_catorce,divisor_uno,
                            divisor_dos,divisor_tres,divisor_cuatro , divisor_cinco,divisor_seis,divisor_siete,divisor_ocho,divisor_nueve]

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


        globin_uno_dos = Enemigo((50,70),dic_miner_globin,(200,-100),6,"m_globin")
        globin_dos_dos = Enemigo((50,70),dic_miner_globin,(500,-100),6,"m_globin")
        globin_cinco_dos = Enemigo((50,70),dic_miner_globin,(800,-100),6,"m_globin")
        globin_tres_dos = Enemigo((50,70),dic_miner_globin,(1000,-100),10,"m_globin")
        globin_cuatro_dos = Enemigo((50,70),dic_miner_globin,(1200,-100),10,"m_globin")
        lista_enemigos_dos = [globin_uno_dos,globin_dos_dos,globin_tres_dos,globin_cuatro_dos,globin_cinco_dos]

        boss = Boss((100,120),dic_boss,(pl_final_piso.rectangulo.x + 1000, pl_final_piso.rectangulo.y -120),4,"boss")
        lista_enemigos_dos.append(boss)

        super().__init__(pantalla, mi_personaje,plataformas_final,lista_enemigos_dos,lista_items_dos,fondo, musica, nivel_actual="tres")