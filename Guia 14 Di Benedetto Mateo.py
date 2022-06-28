"""Guia 14"""
"""14.1"""
def tupla_ordenada(tupla):
    '''Esta funcion recibe una tupla y devuelve si esta ordenada o no'''

    ordenado = True
    try:
        for n in range(len(tupla)-1):
            if tupla[n] >= tupla[n+1]:
                ordenado = False
                break
                return ordenado
    except TypeError:
        print("Problema al ingresar el tipo de dato!")



def tuplas_dominos(ficha1, ficha2):
    '''Esta funcion recibe dos tuplas y devuelve si encajan o no, como un domino'''

    encaje = True

    try:

        for n in ficha1:
            if n in ficha2:
                encaje = True

            else:
                encaje = False

        return encaje

    except TypeError:
        print("Las fichas no pueden tener mas de dos elementos")


"""14.2"""
def lista_tuplas_encontradas(cadena, lista):
    '''Esta funcion recibe por parametros una lista y varias tuplas, y devuelve la tuplas que encontraron algo igual a la lista'''
    tuplas_encontradas = []

    try:

        for tupla in lista:
            if cadena in tupla[0]:
                tuplas_encontradas.append(tupla)

        return tuplas_encontradas

    except TypeError:
        print("Error se tiene que pasar primero el nombre y luego el numero")


"""14.3"""
def factorial(numero):
    """Funcion que recibe un numero y devuelve el factorial de manera recursiva"""

    if numero==0:
        return 1
    return numero*factorial(numero-1)


def pedir_numero_usuario():
    """Esta funcion le pide un numero al usuario"""

    try:
        numero = int(input("Ingrese un numero: "))
        return factorial(numero)

    except RecursionError:
        print("Alcanzo en numero maximo de recursiones")
    except ValueError:
        print("Ingreso un dato de tipo (string) y debe ser de tipo(int)")





