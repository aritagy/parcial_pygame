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

def crear_slots(ancho: int, alto : int, pos_x : int, pos_y : int, columna : int, fila : int, separacion : int, color : int):
    '''
    ### ¿Qué hace?
    · Crea grilla de slots segun las especificaciones del diccionario
    ### ¿Qué recibe?
    · Ancho y alto: ancho y alto del slot; pos_x y pos_y: posicion inicial del slot; columna y fila: cantidad de filas y columnas; 
    · separacion: espacio entre slots; color: color del slot
    ### ¿Qué devuelve?
    · Al usar la funcion con las especificaciones dadas, devuelve la grilla deseada
    '''
    lista_slots = []

    for i in range(fila):
        for j in range(columna):
            x = pos_x + j * (ancho + separacion)
            y = pos_y + i * (alto + separacion)

            slot = crear_rectangulo([ancho, alto], [x, y], color)
            lista_slots.append(slot)

    return lista_slots