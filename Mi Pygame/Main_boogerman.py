import pygame, sys
from Configuraciones import renderizar_texto, dic_sonidos_booger,pausar,mostrar_intro,generar_csv
from Boton_pausa import Boton_pausa
from Boton_volumen import Boton_volumen
from Boton_home import Boton_home
from nivel_uno import Nivel_uno
from nivel_dos import Nivel_dos
from nivel_tres import Nivel_tres


ANCHO = 1300
ALTO = 600
TAMAÑO_PANTALLA = (ANCHO,ALTO)
FPS = 20
pygame.init()
pygame.mixer.init()
PANTALLA = pygame.display.set_mode(TAMAÑO_PANTALLA)
pygame.display.set_caption("The Cosmic Gems")

icono = pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\items\picante.png")
pygame.transform.scale(icono,(10,10))
pygame.display.set_icon(icono)

boton_pausa = Boton_pausa(PANTALLA,r"juego segundo parcial\Mi Pygame\Sprites\botones\pausa sf.png",(60,40),(40,0))
boton_volumen = Boton_volumen(PANTALLA,r"juego segundo parcial\Mi Pygame\Sprites\botones\sound_sf.png",(50,40),(80,0),r"juego segundo parcial\Mi Pygame\Sprites\botones\sound off sf.png")
boton_home = Boton_home(PANTALLA,r"juego segundo parcial\Mi Pygame\Sprites\botones\home sf.png",(50,40),(0,0),r"juego segundo parcial\Mi Pygame\Sprites\botones\home sf.png")


nivel_uno_superado = False
nivel_dos_superado = False
nivel_tres_superado = False
lista_niveles_superados = [nivel_uno_superado,nivel_dos_superado,nivel_tres_superado]

flag = mostrar_intro(PANTALLA)
if flag:
    nivel_actual = Nivel_uno(PANTALLA) 
    clock = pygame.time.Clock()
    tiempo_inicial = pygame.time.get_ticks()
    pygame.mixer.music.load(nivel_actual.musica)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)
    tiempo_de_pausado = 0

while flag:

    clock.tick(FPS)

    tiempo_actual = pygame.time.get_ticks() - tiempo_de_pausado

    tiempo_transcurrido = tiempo_actual - tiempo_inicial
    tiempo_reanudacion = 0
    tiempo_transcurrido = tiempo_transcurrido * 0.001
    tiempo = 60 - tiempo_transcurrido
    string_tiempo = f"{tiempo:.00f}"
    tiempo_renderizado = renderizar_texto(string_tiempo,"Impact",(200,0,150),25)
    vidas = f"Vidas: {nivel_actual.mi_personaje.vidas}"
    vidas_renderizado = renderizar_texto(vidas,"Impact",(255,0,150),25)
    gemas = f"Gemas: {nivel_actual.mi_personaje.cantidad_gemas}"
    gemas_render = renderizar_texto(gemas,"Impact",(255,0,150),25)
    score = f"Score: {nivel_actual.mi_personaje.puntaje}"
    score_render = renderizar_texto(score,"Impact",(255,0,150),25)
    
    nivel_actual.tiempo_actual = tiempo_actual

    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == pygame.QUIT:
            flag = False
            pygame.quit()
            sys.exit(0)
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                tiempo_de_pausado = boton_pausa.pausar(tiempo_actual)
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                click_position = evento.pos
                if boton_pausa.rectangulo.collidepoint(click_position):
                    tiempo_de_pausado = boton_pausa.pausar(tiempo_actual)
                elif boton_volumen.rectangulo.collidepoint(click_position):
                    boton_volumen.mutear()
                elif boton_home.rectangulo.collidepoint(click_position):
                    tiempo_de_pausado = boton_home.mostrar_ventana_home(tiempo_actual,lista_niveles_superados)
                    nivel_actual_home = boton_home.nivel_actual
                    if nivel_actual_home == "uno":
                        nivel_actual = Nivel_uno(PANTALLA) 
                        clock = pygame.time.Clock()
                        tiempo_inicial = pygame.time.get_ticks()
                        pygame.mixer.music.load(nivel_actual.musica)
                        pygame.mixer.music.set_volume(0.1)
                        pygame.mixer.music.play(-1)
                        if boton_volumen.mute:
                            pygame.mixer.music.set_volume(0.0)
                            boton_volumen.imagen = boton_volumen.imagen_click
                        else:
                            pygame.mixer.music.set_volume(0.1)
                        tiempo_de_pausado = 0
                    elif nivel_actual_home == "dos":
                        nivel_actual = Nivel_dos(PANTALLA) 
                        clock = pygame.time.Clock()
                        tiempo_inicial = pygame.time.get_ticks()
                        pygame.mixer.music.load(nivel_actual.musica)
                        pygame.mixer.music.set_volume(0.1)
                        pygame.mixer.music.play(-1) 
                        if boton_volumen.mute:
                            pygame.mixer.music.set_volume(0.0)
                            boton_volumen.imagen = boton_volumen.imagen_click
                        else:
                            pygame.mixer.music.set_volume(0.1)
                        tiempo_de_pausado = 0
                    elif nivel_actual_home == "tres":
                        nivel_actual = Nivel_tres(PANTALLA) 
                        clock = pygame.time.Clock()
                        tiempo_inicial = pygame.time.get_ticks()
                        pygame.mixer.music.load(nivel_actual.musica)
                        pygame.mixer.music.play(-1)
                        if boton_volumen.mute:
                            pygame.mixer.music.set_volume(0.0)
                            boton_volumen.imagen = boton_volumen.imagen_click
                        else:
                            pygame.mixer.music.set_volume(0.1)
                        tiempo_de_pausado = 0
 
    nivel_actual.update(eventos)

    PANTALLA.blit(tiempo_renderizado,(ANCHO//2, -2))
    PANTALLA.blit(vidas_renderizado,(ANCHO //2 - 300,0))
    PANTALLA.blit(gemas_render,(ANCHO//2 -500, 0))
    PANTALLA.blit(score_render,(ANCHO -300, 0)) 
    PANTALLA.blit(boton_pausa.imagen,(boton_pausa.pos_x,boton_pausa.pos_y))
    PANTALLA.blit(boton_volumen.imagen,(boton_volumen.pos_x,boton_volumen.pos_y))
    PANTALLA.blit(boton_home.imagen,(boton_home.pos_x,boton_home.pos_y))

    if tiempo < 1 and nivel_actual.mi_personaje.ganador == False or nivel_actual.mi_personaje.vidas == 0:
        mensaje_nivel_finalizado = "Finished level"
        mensaje_lose = "You lose"
        mensaje_fin_render = renderizar_texto(mensaje_nivel_finalizado,"chiller",(255,10,10),80)
        mensaje_lose_render = renderizar_texto(mensaje_lose,"chiller",(255,10,10),80)
        PANTALLA.blit(mensaje_fin_render,(ANCHO//2-200,ALTO//2 -100))
        PANTALLA.blit(mensaje_lose_render,(ANCHO//2 -100,ALTO//2))
        pygame.display.update()
        pygame.time.wait(3000)
        tiempo_de_pausado = 0
        match nivel_actual.nivel_actual:
            case "uno":
                nivel_actual = Nivel_uno(PANTALLA)
                tiempo_inicial = pygame.time.get_ticks()
                if boton_volumen.mute:
                    pygame.mixer.music.set_volume(0.0)
                    boton_volumen.imagen = boton_volumen.imagen_click
                else:
                    pygame.mixer.music.set_volume(0.1)
            case "dos":
                nivel_actual = Nivel_dos(PANTALLA)
                tiempo_inicial = pygame.time.get_ticks()
                if boton_volumen.mute:
                    pygame.mixer.music.set_volume(0.0)
                    boton_volumen.imagen = boton_volumen.imagen_click
                else:
                    pygame.mixer.music.set_volume(0.1)                
            case "tres":
                nivel_actual = Nivel_tres(PANTALLA)
                tiempo_inicial = pygame.time.get_ticks() 
                if boton_volumen.mute:
                    pygame.mixer.music.set_volume(0.0)
                    boton_volumen.imagen = boton_volumen.imagen_click
                else:
                    pygame.mixer.music.set_volume(0.1)                

    elif nivel_actual.mi_personaje.ganador:
        mensaje_win = "Congratulations, you win"
        mensaje_win_render = renderizar_texto(mensaje_win,"candara",(100,255,10),80)
        tiempo_de_pausado = 0
        match nivel_actual.nivel_actual:
            case "uno":
                PANTALLA.blit(mensaje_win_render,(200,ALTO//2))
                generar_csv(str(nivel_actual.mi_personaje.puntaje)+";\n","scores_Cosmic_gems.csv")
                pygame.display.update()
                pygame.time.wait(3000)
                lista_niveles_superados[0] = True
                nivel_actual = Nivel_dos(PANTALLA)
                tiempo_inicial = pygame.time.get_ticks()
                tiempo = 60
                pygame.mixer.music.load(nivel_actual.musica)
                pygame.mixer.music.play(-1)
                if boton_volumen.mute:
                    pygame.mixer.music.set_volume(0.0)
                else:
                    pygame.mixer.music.set_volume(0.1)
            case "dos":
                PANTALLA.blit(mensaje_win_render,(200,ALTO//2))
                generar_csv(str(nivel_actual.mi_personaje.puntaje)+";\n","scores_Cosmic_gems.csv")
                pygame.display.update()
                pygame.time.wait(3000)
                lista_niveles_superados[1] = True
                nivel_dos_superado = True
                nivel_actual = Nivel_tres(PANTALLA)
                tiempo_inicial = pygame.time.get_ticks()
                tiempo = 60
                pygame.mixer.music.load(nivel_actual.musica)
                pygame.mixer.music.play(-1)
                if boton_volumen.mute:
                    pygame.mixer.music.set_volume(0.0)
                else:
                    pygame.mixer.music.set_volume(0.1)
            case "tres":
                pygame.mixer.music.stop()
                #dic_sonidos_booger["gana"].play()
                dic_sonidos_booger["winner"].play()
                pygame.mixer.Sound
                PANTALLA.blit(mensaje_win_render,(200,ALTO//2))
                generar_csv(str(nivel_actual.mi_personaje.puntaje)+";\n","scores_Cosmic_gems.csv")
                pygame.display.update()
                pygame.time.wait(3000)
                lista_niveles_superados[2] = True
                nivel_actual = Nivel_uno(PANTALLA)
                tiempo_inicial = pygame.time.get_ticks()
                tiempo = 60
                pygame.mixer.music.load(nivel_actual.musica)
                pygame.mixer.music.play(-1)
                if boton_volumen.mute:
                    pygame.mixer.music.set_volume(0.0)
                else:
                    pygame.mixer.music.set_volume(0.1)
    
    if tiempo < 16 and tiempo > 13: 
        for plataforma in nivel_actual.plataformas:
            if plataforma.path_premio == r"juego segundo parcial\Mi Pygame\Sprites\plataformas\puerta_abierta.png":
                plataforma.premio_descubierto = True
                plataforma.tiene_premio = False
                plataforma.agregar_item(nivel_actual.lista_items,nivel_actual.nivel_actual,"abrir_puerta")
                nivel_actual.plataformas.remove(plataforma)
                del plataforma
                break

    pygame.display.update()