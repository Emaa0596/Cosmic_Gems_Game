import pygame
pygame.init()
pygame.font.init()


def renderizar_texto(texto:str, estilo_letra:str, color, tamaño:int):
    fuente = pygame.font.SysFont(estilo_letra,tamaño) 
    texto_renderizado = fuente.render(texto,False, color, None)
    return texto_renderizado

def reescalar_imagenes(diccionario_personaje:dict, ancho,alto):
    for clave in diccionario_personaje:
            for i in range(len(diccionario_personaje[clave])):
                imagen = diccionario_personaje[clave][i]
                diccionario_personaje[clave][i] = pygame.transform.scale(imagen,(ancho,alto))
    return diccionario_personaje

def girar_imagenes(lista:list,flip_x,flip_y):
    lista_girada = []
    for imagen in lista:
        lista_girada.append(pygame.transform.flip(imagen,flip_x,flip_y))
    return lista_girada

def obtener_rectangulos(principal:pygame.Rect)-> dict:
    diccionario = {}
    diccionario["main"] = principal
    diccionario["bottom"] = pygame.Rect(principal.left, principal.bottom -10, principal.width, 10)
    diccionario["right"] = pygame.Rect(principal.right -8, principal.top, 8, principal.height)
    diccionario["left"] = pygame.Rect(principal.left, principal.top, 8, principal.height)
    diccionario["top"] = pygame.Rect(principal.left, principal.top, principal.width, 10)
    return diccionario

def pausar(tiempo_al_pausar, pantalla:pygame.Surface):
    mensaje_pausa = renderizar_texto("Juego pausado","Arial",(100,255,10),50)
    pausa = True
    pygame.mixer.init()
    pygame.mixer.music.pause()
    while pausa:
        pantalla.blit(mensaje_pausa,(300,300))
        pygame.display.update()
        eventos = pygame.event.get()
        for evento in eventos:
            if evento.type == pygame.QUIT:
                pygame.quit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    pygame.mixer.music.unpause()
                    pausa = False
    tiempo_de_pausado = pygame.time.get_ticks() - tiempo_al_pausar
    return tiempo_de_pausado
            
def mostrar_intro(pantalla:pygame.Surface):
    ancho = pantalla.get_width()
    alto = pantalla.get_height()
    mensaje_intro = renderizar_texto("Presione cualquier tecla para comenzar","Arial",(243, 156, 18),35)
    fondo_intro = pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Fondos\Portada_intro.png")
    fondo_intro = pygame.transform.scale(fondo_intro,(ancho,alto))
    pygame.init()
    pygame.mixer.init()
    intro = True
    pygame.mixer.music.load(r"juego segundo parcial\Mi Pygame\Sprites\sonidos\INTRO.wav")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.3)
    while intro:
        pantalla.blit(fondo_intro,(0,0))
        pantalla.blit(mensaje_intro,(425,alto/2 + 80))
        pygame.display.update()
        eventos = pygame.event.get()
        for evento in eventos:
            if evento.type == pygame.QUIT:
                pygame.quit()
                intro = False
                return intro
            elif evento.type == pygame.KEYDOWN:
                intro = False
                pygame.mixer.music.stop()
                return True
            
def generar_csv(score:str,path:str):
    with open(path,"a") as archivo:
        archivo.write(score)
    return True

personaje_camina = [ pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Caminando\1.png"),
                     pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Caminando\2.png"),
                     pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Caminando\3.png"),
                     pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Caminando\4.png"),
                     pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Caminando\5.png"),
                     pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Caminando\6.png"),
                     pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Caminando\7.png"),
                     pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Caminando\8.png"),
                     pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Caminando\9.png"),
                     pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Caminando\10.png"),
                     pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Caminando\11.png"),
                     pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Caminando\12.png"),
                     pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Caminando\13.png"),
                     pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Caminando\14.png"),
                     pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Caminando\15.png"),
                     pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Caminando\16.png"),
                     pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Caminando\17.png"),
                     pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Caminando\18.png"),
                     pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Caminando\19.png"),
                     pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Caminando\20.png")]

personaje_camina_izquierda = girar_imagenes(personaje_camina, True, False)

personaje_quieto = [pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Animado\2.png")]

personaje_salta = [pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Saltando\4.png")]

personaje_salta_izquierda = girar_imagenes(personaje_salta,True,False)

personaje_agachado =[pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Agachado\2.png")]

personaje_vuela = [pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\vuela\vuela.png")]

personaje_vuela_izquierda = girar_imagenes(personaje_vuela,True,False)

personaje_vuela_arriba = [pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\vuela\vuela_arriba.png")]

personaje_tira_poder = [pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Tira_poder\0.png"),
                        pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Tira_poder\0.png"),
                        pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Tira_poder\0.png"),
                        pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Tira_poder\0.png"),
                        pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Tira_poder\1.png"),
                        pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Tira_poder\1.png"),
                        pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Tira_poder\1.png"),
                        pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Tira_poder\2.png"),
                        pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Tira_poder\2.png"),
                        pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Tira_poder\2.png"),
                        pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Tira_poder\2.png"),
                        pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Tira_poder\2.png"),
                        pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Tira_poder\2.png"),
                        pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Tira_poder\2.png"),
                        pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Tira_poder\2.png"),
                        pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Tira_poder\2.png"),
                        pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Tira_poder\2.png"),
                        pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Tira_poder\3.png"),
                        pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Tira_poder\3.png"),
                        pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Tira_poder\3.png"),
                        pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Tira_poder\3.png"),
                        pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Tira_poder\3.png"),
                        pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Tira_poder\4.png"),
                        pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Tira_poder\4.png"),
                        pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Tira_poder\4.png"),
                        pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Tira_poder\4.png")]

personaje_herido = [pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Muriendo\1.png"),
                    pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Muriendo\0.png"),
                    pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Muriendo\0.png"),
                    pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Muriendo\0.png"),
                    pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Muriendo\0.png"),
                    pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Muriendo\0.png"),
                    pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Muriendo\0.png"),
                    pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Muriendo\0.png"),
                    pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Muriendo\0.png"),
                    pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Muriendo\0.png"),
                    pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Muriendo\0.png"),
                    pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Muriendo\0.png"),
                    pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Muriendo\0.png"),
                    pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Muriendo\0.png"),
                    pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Muriendo\0.png"),
                    pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Muriendo\0.png"),
                    pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Muriendo\0.png"),
                    pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Muriendo\0.png")]

personaje_gana = [pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\gana\gana.png")]

personaje_quieto_izquierda = girar_imagenes(personaje_quieto,True,False)

diccionario_personaje = {}
diccionario_personaje["quieto"] = personaje_quieto
diccionario_personaje["quieto_izquierda"] = personaje_quieto_izquierda
diccionario_personaje["camina"] = personaje_camina
diccionario_personaje["camina_izquierda"] = personaje_camina_izquierda
diccionario_personaje["salta"] = personaje_salta
diccionario_personaje["salta_izquierda"] = personaje_salta_izquierda
diccionario_personaje["agachado"] = personaje_agachado
diccionario_personaje["vuela"] = personaje_vuela
diccionario_personaje["vuela_izquierda"] = personaje_vuela_izquierda
diccionario_personaje["vuela_arriba"] = personaje_vuela_arriba
diccionario_personaje["tira_poder"] = personaje_tira_poder
diccionario_personaje["herido"] = personaje_herido
diccionario_personaje["gana"] = personaje_gana


goblin_camina = [pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Enemigo_goblin\0.png"),
                 pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Enemigo_goblin\1.png"),
                 pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Enemigo_goblin\2.png"),
                 pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Enemigo_goblin\3.png"),
                 pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Enemigo_goblin\4.png"),
                 pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Enemigo_goblin\5.png"),
                 pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Enemigo_goblin\6.png"),
                 pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Enemigo_goblin\7.png"),
                 pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Enemigo_goblin\8.png"),
                 pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Enemigo_goblin\9.png"),
                 pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Enemigo_goblin\10.png"),
                 pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Enemigo_goblin\11.png")]

goblin_ataca = [pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\goblin_ataca\0.png"),
                pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\goblin_ataca\1.png"),
                pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\goblin_ataca\2.png")]

goblin_muere = [pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\goblin_muere\0.png"),
                pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\goblin_muere\1.png"),
                pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\goblin_muere\2.png"),
                pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\goblin_muere\3.png"),
                pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\goblin_muere\4.png"),
                pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\goblin_muere\5.png"),
                pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\goblin_muere\6.png"),
                pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\goblin_muere\7.png"),
                pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\goblin_muere\8.png")]

goblin_camina_izquierda = girar_imagenes(goblin_camina,True,False)

goblin_salta = [pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Enemigo_goblin\12.png")]

goblin_quieto = [pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\Enemigo_goblin\13.png")]

diccionario_goblin = {}
diccionario_goblin["camina"] = goblin_camina
diccionario_goblin["ataca"] = goblin_ataca
diccionario_goblin["muere"] = goblin_muere
diccionario_goblin["camina_izquierda"] = goblin_camina_izquierda
diccionario_goblin["quieto"] = goblin_quieto
diccionario_goblin["salta"] = goblin_salta


miner_globin_camina = [pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\miner_globin\0.png"),
                       pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\miner_globin\0.png"),
                       pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\miner_globin\0.png"),
                       pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\miner_globin\1.png"),
                       pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\miner_globin\1.png"),
                       pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\miner_globin\1.png"),
                       pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\miner_globin\2.png"),
                       pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\miner_globin\2.png"),
                       pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\miner_globin\2.png"),
                       pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\miner_globin\3.png"),
                       pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\miner_globin\3.png"),
                       pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\miner_globin\3.png"),
                       pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\miner_globin\4.png"),
                       pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\miner_globin\4.png"),
                       pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\miner_globin\4.png"),
                       pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\miner_globin\5.png"),
                       pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\miner_globin\5.png"),
                       pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\miner_globin\5.png"),
                       pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\miner_globin\5.png"),
                       pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\miner_globin\5.png"),
                       pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\miner_globin\6.png"),
                       pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\miner_globin\6.png"),
                       pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\miner_globin\6.png"),
                       pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\miner_globin\7.png"),
                       pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\miner_globin\7.png"),
                       pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\miner_globin\8.png"),
                       pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\miner_globin\8.png"),
                       pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\miner_globin\9.png"),
                       pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\miner_globin\9.png"),
                       pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\miner_globin\10.png"),
                       pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\miner_globin\10.png"),
                       pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\miner_globin\11.png"),
                       pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\miner_globin\11.png")]

miner_globin_camina_izquierda = girar_imagenes(miner_globin_camina,True,False)

miner_globin_quieto = [pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\miner_globin\12.png")]

miner_globin_muere = [pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\miner_globin_muere\0.png"),
                      pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\miner_globin_muere\1.png"),
                      pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\miner_globin_muere\2.png"),
                      pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\miner_globin_muere\3.png")]

dic_miner_globin = {}
dic_miner_globin["camina"] = miner_globin_camina
dic_miner_globin["camina_izquierda"] = miner_globin_camina_izquierda
dic_miner_globin["muere"] = miner_globin_muere
dic_miner_globin["quieto"] = miner_globin_quieto


booger_gana = pygame.mixer.Sound(r"juego segundo parcial\Mi Pygame\Sprites\sonidos\Booger gana.wav")
booger_vuela = pygame.mixer.Sound(r"juego segundo parcial\Mi Pygame\Sprites\sonidos\Booger vuela (Corto).wav")
disparo_booger = pygame.mixer.Sound(r"juego segundo parcial\Mi Pygame\Sprites\sonidos\Disparo Booger.wav")
booger_herido = pygame.mixer.Sound(r"juego segundo parcial\Mi Pygame\Sprites\sonidos\Herida Booger.wav")
salto_booger = pygame.mixer.Sound(r"juego segundo parcial\Mi Pygame\Sprites\sonidos\Salto Booger.wav")
win_game = pygame.mixer.Sound(r"juego segundo parcial\Mi Pygame\Sprites\sonidos\winner.mp3")

booger_vuela.set_volume(0.0)
salto_booger.set_volume(0.3)
disparo_booger.set_volume(0.3)
booger_herido.set_volume(0.2)
booger_gana.set_volume(0.3)
win_game.fadeout(2000)

dic_sonidos_booger = {}
dic_sonidos_booger["gana"] = booger_gana
dic_sonidos_booger["vuela"] = booger_vuela
dic_sonidos_booger["dispara"] = disparo_booger
dic_sonidos_booger["herido"] = booger_herido
dic_sonidos_booger["salta"] = salto_booger
dic_sonidos_booger["winner"] = win_game

sonido_globin_muere = pygame.mixer.Sound(r"juego segundo parcial\Mi Pygame\Sprites\sonidos\Muerte enemigo simple.wav")
sonido_boss_muere = pygame.mixer.Sound(r"juego segundo parcial\Mi Pygame\Sprites\sonidos\Muerte enemigo (Boss).wav")

dic_sonidos_enemigos = {}
dic_sonidos_enemigos["muere_globin"] = sonido_globin_muere
dic_sonidos_enemigos["muere_boss"] = sonido_boss_muere

sonido_globin_muere.set_volume(0.2)

boss_camina = [pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\boss\0.png"),
               pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\boss\0.png"),
               pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\boss\0.png"),
               pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\boss\0.png"),
               pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\boss\0.png"),
               pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\boss\1.png"),
               pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\boss\1.png"),
               pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\boss\1.png"),
               pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\boss\1.png"),
               pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\boss\1.png"),
               pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\boss\2.png"),
               pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\boss\2.png"),
               pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\boss\2.png"),
               pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\boss\2.png"),
               pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\boss\2.png"),
               pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\boss\3.png"),
               pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\boss\3.png"),
               pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\boss\3.png"),
               pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\boss\3.png"),
               pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\boss\3.png"),
               pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\boss\4.png"),
               pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\boss\4.png"),
               pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\boss\4.png"),
               pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\boss\4.png"),
               pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\boss\4.png"),
               pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\boss\5.png"),
               pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\boss\5.png"),
               pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\boss\5.png"),
               pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\boss\5.png"),
               pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\boss\5.png"),
               pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\boss\6.png"),
               pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\boss\6.png"),
               pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\boss\6.png"),
               pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\boss\6.png"),
               pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\boss\7.png"),
               pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\boss\7.png"),
               pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\boss\7.png")]

boss_camina_izquierda = girar_imagenes(boss_camina,True,False)

boss_enojado = [pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\boss enojado\0.png"),
                pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\boss enojado\0.png"),
                pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\boss enojado\0.png"),
                pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\boss enojado\0.png"),
                pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\boss enojado\1.png"),
                pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\boss enojado\1.png"),
                pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\boss enojado\1.png"),
                pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\boss enojado\1.png"),
                pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\boss enojado\2.png"),
                pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\boss enojado\2.png"),
                pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\boss enojado\2.png"),
                pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\boss enojado\2.png"),
                pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\boss enojado\3.png"),
                pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\boss enojado\3.png"),
                pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\boss enojado\3.png"),
                pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\boss enojado\3.png")]

boss_enojado_izquierda = girar_imagenes(boss_enojado,True,False)

boss_muere = [pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\boss muere\0.png"),
              pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\boss muere\1.png"),
              pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\boss muere\1.png"),
              pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\boss muere\1.png"),
              pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\boss muere\1.png"),
              pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\boss muere\1.png"),
              pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\boss muere\1.png"),
              pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\boss muere\2.png"),
              pygame.image.load(r"juego segundo parcial\Mi Pygame\Sprites\boss muere\2.png"),]

dic_boss = {}
dic_boss["camina"] = boss_camina
dic_boss["camina_izquierda"] = boss_camina_izquierda
dic_boss["muere"] = boss_muere
dic_boss["ataca"] = boss_enojado
dic_boss["ataca_izquierda"] = boss_enojado_izquierda
dic_boss["quieto"] = boss_camina
