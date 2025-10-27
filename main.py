import pygame
from funciones import *
import config
import pygame.mixer as mixer

pygame.init()
mixer.init()
pygame.font.init()

minecraft_font = pygame.font.Font("fuentes/Minecraft.ttf", 27)
arial_font = pygame.font.SysFont("Arial", 55)
arial_font = arial_font.render("→", True, (0, 0, 0))
texto_fabricación = minecraft_font.render("Fabricacion", True, (0, 0, 0)) 
texto_inventario = minecraft_font.render("Inventario", True, (0, 0, 0)) 

mixer.music.load("sonidos/Subwoofer_Lullaby.mp3")
mixer.music.set_volume(0.2)
mixer.music.play(-1)

pygame.display.set_caption("Pygirls - Simulador de Crafteo")
pygame.display.set_icon(config.LOGO_MINECRAFT)


lista_rectangulos = []
lista_rectangulos.append(crear_rectangulo([550,500], [170,50], config.GRIS_CLARO))
lista_rectangulos.append(crear_rectangulo([80, 80], [580, 150], config.GRIS_OSCURO))
lista_rectangulos.append(crear_rectangulo([60, 60], [210, 160], config.GRIS_OSCURO))

slots_inventario = crear_slots(50, 50, 200, 320, 3, 9, 5, config.GRIS_OSCURO)
slots_acceso_rapido = crear_slots(50, 50, 200, 490, 1, 9, 5, config.GRIS_OSCURO)
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
        pygame.draw.rect(pantalla, config.NEGRO, (lista_rectangulos[i]["posicion"], lista_rectangulos[i]["superficie"]), 2)


    for i in slots_inventario:
        pygame.draw.rect(pantalla, i["color"], (i["posicion"], i["superficie"]))
        pygame.draw.rect(pantalla, config.NEGRO, (i["posicion"], i["superficie"]), 2)
    
    for i in slot_fabricacion:
        pygame.draw.rect(pantalla, i["color"], (i["posicion"], i["superficie"]))
        pygame.draw.rect(pantalla, config.NEGRO, (i["posicion"], i["superficie"]), 2)

    for i in slots_acceso_rapido:
        pygame.draw.rect(pantalla, i["color"], (i["posicion"], i["superficie"]))
        pygame.draw.rect(pantalla, config.NEGRO, (i["posicion"], i["superficie"]), 2)

    pantalla.blit(texto_fabricación, (300, 80))
    pantalla.blit(texto_inventario, (200, 290))
    pantalla.blit(arial_font, (490, 150))

    pygame.display.flip() 