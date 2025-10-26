import pygame

pygame.init()

# def crear_rectangulo(ancho:int, )altura:int, ):
#     rectangulo = {
#         "base" : ancho, 
#         "altura" : altura, 
#         "eje x" : eje x,
#         "eje y" : eje_y
#     }


def crear_rectangulo(superficie : list, posicion : list, color: list):
    rectangulo_nuevo = {
        "superficie" : superficie,
        "posicion" : posicion,
        "color" : color
        # "funcion" : None
    }
    return rectangulo_nuevo

    '''
    ### ¿Qué hace?
    ·
    ### ¿Qué recibe?
    ·
    ### ¿Qué devuelve?
    ·
    '''