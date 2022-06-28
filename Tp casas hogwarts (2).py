from random import randint
from random import choice
from random import seed
import sys

casas = ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]

listado = ['Martinez E', 'Romero', 'Otamendi', 'Acunia', 'Montiel', 'Lo Celso', 'Paredes', 'Messi', 'Di Maria', 'Martinez L', 'De Paul', 'Gomez', 'Dybala', 'Correa J', 'Correa A', 'Musso', 'Rulli', 'De Rossi', 'Molina', 'Pezzela', 'Perez ', 'Benedetto', 'Pique', 'De Bruyne', 'Ronaldo', 'Neymar', 'Mbappe', 'Kante', 'Mane', 'Van Dijk', 'Haaland', 'Rojo', 'Busquets', 'Diaz L', 'Suarez', 'Jesus G', 'Rossi A', 'Vinicius Jr', 'Benzema', 'Courtois', 'Modric', 'Veratti', 'Insigne', 'Kroos']


def copiar_lista():
    """Esta funcion devuelve la lista de alumnos copiada"""
    copia_alumnos = listado.copy()

    return copia_alumnos

def sorteo_casas(copia_alumnos):
    '''Esta devuelve los jugadores en las casas'''
    indice_aleatorio = randint(0, len(copia_alumnos)-1)

    return indice_aleatorio

def seleccionar_alumnos():
    """Esta funcion muestra a que casa ingresa cada alumno"""
    contador = 0
    copia_alumnos = copiar_lista()

    for x in range(len(copia_alumnos)-1):
        contador += 1
        alumno = copia_alumnos.pop(sorteo_casas(copia_alumnos))

        if contador%4 == 1:
            print ("El alumno {}, entro a la casa {}".format(alumno, casas[0]))
        elif contador%4 == 2:
            print ("El alumno {}, entro a la casa {}".format(alumno, casas[1]))
        elif contador%4 == 3:
            print ("El alumno {}, entro a la casa {}".format(alumno, casas[2]))
        else:
            print ("El alumno {}, entro a la casa {}".format(alumno, casas[3]))







