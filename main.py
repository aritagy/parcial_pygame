import pygame
from funciones import *
import config
import pygame.mixer as mixer

pygame.init()
mixer.init()

mixer.music.load("sonidos/Subwoofer_Lullaby.mp3")
mixer.music.set_volume(0.2)
mixer.music.play()

pantalla = pygame.display.set_mode(config.DIMENSION_PANTALLA)

pygame.display.set_caption("Pygirls")
pygame.display.set_icon(config.LOGO_MINECRAFT)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pantalla.fill(config.NEGRO)

    pantalla.blit(config.FONDO_PANTALLA, (-1500,-490))

    pygame.display.flip()