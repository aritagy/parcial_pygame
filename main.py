import pygame
from funciones import *
import config
import pygame.mixer as mixer

pygame.init()
mixer.init()

mixer.music.load("sonidos/Subwoofer_Lullaby.mp3")
mixer.music.set_volume(0.2)
mixer.music.play()

lista_rectangulos = []

lista_rectangulos.append(crear_rectangulo([500,500], [150,50], config.GRIS_CLARO))

pantalla = pygame.display.set_mode(config.DIMENSION_PANTALLA)

pygame.display.set_caption("Pygirls")
pygame.display.set_icon(config.LOGO_MINECRAFT)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    pantalla.blit(config.FONDO_PANTALLA, (-1600,-490))


    for i in range(len(lista_rectangulos)):
        pygame.draw.rect(pantalla,lista_rectangulos[i]["color"], (lista_rectangulos[i]["posicion"], lista_rectangulos[i]["superficie"]))
    
    pygame.display.flip()