import pygame

pygame.init()

def crear_rectangulo(superficie : list, posicion : list, color: list):
    rectangulo_nuevo = {
        "superficie" : superficie,
        "posicion" : posicion,
        "color" : color
        # "funcion" : None
    }
    '''
    ### ¿Qué hace?
    ·Hace que mi rectángulo sea un diccionario para que los cambios(Ya sea de superficie, color o posición) se optimicen cambiando simples valores que se encuentran en él
    ### ¿Qué recibe?
    ·Recibe la superficie(ancho, alto), posición(x,y) y color(r,g,b).
    ### ¿Qué devuelve?
    ·retorna el diccionario del rectangulo 
    '''
    return rectangulo_nuevo
