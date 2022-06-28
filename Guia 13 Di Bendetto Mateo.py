'''Guia 13'''
'''13.1'''
def cantidad_digitos(cadena):
    '''Esta funcion recibe como parametro una cadena de numeros, y devuelve la cantidad de digitos'''
    n=1

    if cadena < 10:
        return 1
    else:

        return n + cantidad_digitos(cadena//10)

'''13.2'''
def es_potencia(n, b):
    '''Esta funcion recibe por parametros dos numeros y devuelve True or False si es potencia uno de otro'''

    if n == b:
        return True
    elif n < b:
        return False

    return es_potencia(n/b, b)

'''13.3'''
def par(numero):
    """Esta funcion recibe por parametro un numero par y devuelve uno impar"""
    if numero==0:
        return True
    else:
        return not impar(numero%2)

def impar(numero):
    """Esta funcion recibe un numero impar y devuelve un numero par"""
    if numero == 1:
        return True
    else:
        return not par(numero%2)


'''13.4'''

def valor_maximo(lista):
    """Esta funcio recibe una lista y devuelve el valor maximo"""

    if len(lista) == 1:
        return lista.pop()
    else:
        numero= lista.pop()
        max = valor_maximo(lista)
        if numero > max:
            max =   numero
    return max


'''13.5'''
def ordenar_mayor_a_menor(lista):
    """Esta funcion recibe una lista y la devuelve ordenada de mayor a menor"""
    lista_ordenada = orden_por_seleccion(lista)


    lista_ordenada.reverse()
    return lista_ordenada

def buscar_max (lista, inicial, final):

    pos_max = inicial

    for i in range(inicial + 1 ,final + 1):
        if lista[i] > lista[pos_max]:
            pos_max = i

    return pos_max

def orden_por_seleccion(lista):
    """Recibe una lista y la devuelve ordenada"""

    final_lista = len(lista)-1

    while final_lista > 0:
        posicion_mayor = buscar_max(lista, 0, final_lista)

        lista[posicion_mayor], lista[final_lista] = lista[final_lista], lista[posicion_mayor]

        final_lista -= 1
    return lista


















