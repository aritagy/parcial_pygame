import pygame
from funciones import *
import config
import pygame.mixer as mixer

pygame.init()
mixer.init()

mixer.music.load("sonidos/Subwoofer_Lullaby.mp3")
mixer.music.set_volume(0.2)
mixer.music.play(-1)

pygame.display.set_caption("Pygirls - Simulador de Crafteo")
pygame.display.set_icon(config.LOGO_MINECRAFT)


lista_rectangulos = []
lista_rectangulos.append(crear_rectangulo([550,500], [170,50], config.GRIS_CLARO))
lista_rectangulos.append(crear_rectangulo([80, 80], [550, 150], config.GRIS_OSCURO))
lista_rectangulos.append(crear_rectangulo([60, 60], [210, 160], config.GRIS_OSCURO))

slots_inventario = crear_slots(50, 50, 200, 320, 9, 3, 5, config.GRIS_OSCURO)
slots_acceso_rapido = crear_slots(50, 50, 200, 490, 9, 1, 5, config.GRIS_OSCURO)
slot_fabricacion = crear_slots(50, 50, 300, 110, 3, 3, 5, config.GRIS_OSCURO)

pantalla = pygame.display.set_mode(config.DIMENSION_PANTALLA)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    pantalla.blit(config.FONDO_PANTALLA, (-1600,-490))


    for i in range(len(lista_rectangulos)):
        pygame.draw.rect(pantalla,lista_rectangulos[i]["color"], (lista_rectangulos[i]["posicion"], lista_rectangulos[i]["superficie"]))


    for i in slots_inventario:
        pygame.draw.rect(pantalla, i["color"], (i["posicion"], i["superficie"]))
        pygame.draw.rect(pantalla, config.NEGRO, (i["posicion"], i["superficie"]), 2)
    
    for i in slot_fabricacion:
        pygame.draw.rect(pantalla, i["color"], (i["posicion"], i["superficie"]))
        pygame.draw.rect(pantalla, config.NEGRO, (i["posicion"], i["superficie"]), 2)

    for i in slots_acceso_rapido:
        pygame.draw.rect(pantalla, i["color"], (i["posicion"], i["superficie"]))
        pygame.draw.rect(pantalla, config.NEGRO, (i["posicion"], i["superficie"]), 2)

    pygame.display.flip() 