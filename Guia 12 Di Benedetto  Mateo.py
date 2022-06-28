''''Guia 12'''
'''12.1'''
def valor_maximo_lista(lista):
    '''Esta funcion recibe por parametro una lista de numero y devuelve el valor maximo.'''
    valor_maximo = lista[0]

    for numero in lista:
        if numero > valor_maximo:
            valor_maximo = numero

    return valor_maximo

def valor_maximo_e_indice_en_lista(lista):
    '''Esta funcion recibe por parametro una lista de numero y devuelve el valor maximo.'''
    valor_maximo = lista[0]
    indice = 0

    for i in range(len(lista)):


        if lista[i] > valor_maximo:
            valor_maximo = lista[i]
            indice = i

    return [valor_maximo, indice]

'''c) dice que hay un error de sintaxis'''

'''12.2'''
def lista_tuplas_encontradas(cadena, lista):
    '''Esta funcion recibe por parametros una lista y varias tuplas, y devuelve la tuplas que encontraron algo igual a la lista'''
    tuplas_encontradas = []

    for tupla in lista:
        if cadena in tupla:
            tuplas_encontradas.append(tupla)

    return tuplas_encontradas

'''12.3'''
def encontrar_numero_reubicarlo(lista, elemento):
    '''Recibe por parametro una lista y un elemento, devuelve el elemento reubicado, o si lo encontro en que posicion'''


'''
12.2 Escribir una función que reciba una cadena a buscar y una lista de tuplas
(nombre_completo, telefono), y busque dentro de la lista, todas las entradas que
contengan en el nombre completo la cadena recibida (puede ser el nombre, el apellido
o sólo una parte de cualquiera de ellos).
Debe devolver una lista con todas las tuplas encontradas.
Por ejemplo:
buscar_contacto(“Carlos”, [(“Joana”, 15937023), (“Pepe Sanchez”, 15549833),
(“Carlos Gomez”, 15775409), (“Jose Carlos”, 15436587)]
→ [(“Carlos Gomez”, 15775409), (“Jose Carlos”, 15436587)]


12.3 Escribir una función que reciba una lista ordenada y un elemento. Si el elemento
se encuentra en la lista, debe encontrar su posición mediante búsqueda binaria y
devolverla. Si no se encuentra, debe agregarlo a la lista en la posición correcta y
devolver esa nueva posición.
(No utilizar lista.sort() .)'''