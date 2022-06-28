'''Guia 11'''
def tupla_ordenada(tupla):
    '''Esta funcion recibe una tupla y devuelve si esta ordenada o no'''

    ordenado = True

    for n in range(len(tupla)-1):
        if tupla[n] >= tupla[n+1]:
            ordenado = False
            break

    return ordenado

'''11.2'''
def tuplas_dominos(ficha1, ficha2):
    '''Esta funcion recibe dos tuplas y devuelve si encajan o no, como un domino'''

    encaje = True

    for n in ficha1:
        if n in ficha2:
            encaje = True

        else:
            encaje = False

    return encaje

'''11.3'''
def obtener_listas_pares(lista_num):
    '''Esta funcion recibe una lista de numeros enteros y devuelve una lista de forma ascendentes los numero pares'''

    lista_nueva = []

    for x in lista_num:
        if x%2 == 0:
            lista_nueva.append(x)

    lista_nueva.sort()
    return lista_nueva

def sumatoria_promedio_lista_numero(lista_numeros):
    '''esta funcion recibe por parametro una lista de numeros, y devuelve el promedio de la suma entre todos'''
    suma= 0

    for n in lista_numeros:
        suma  += n
        promedio = suma/len(lista_numeros)

    return promedio

def lista_numeros_del_factorial(numero):
    '''Recibe por parametro un numero, y devuelve la lista de sus factoriales'''
    lista_nueva = []

    for x in range(numero, 0, -1):
        lista_nueva.append(x)

    lista_nueva.sort(reverse=True)
    return lista_nueva

'''11.4'''
def nombre_apellido(lista):
    '''Esta funcion recibe una tupla por parametro y devuelve una lista con nombre y el apellido'''
    lista_nueva = []

    for tupla in lista:
        apellido, nombre, inicial = tupla
        nombre_completo="{} {} {}".format(nombre, inicial, apellido)
        lista_nueva.append(nombre_completo)

    return lista_nueva

'''11.5'''
def lista_invertida(lista):
    '''Esta funcion recibe por parametro una lista, y luego la devuelve a la inversa.'''
    lista_invertida = []

    for i in lista:
        lista_invertida += [i]

    lista_invertida.reverse()
    return lista_invertida







