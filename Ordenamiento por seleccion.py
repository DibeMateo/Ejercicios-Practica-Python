def ord_seleccion(lista):
    """"""

    ultima_posicion = len(lista)-1

    while ultima_posicion > 0:
        posicion_mayor = buscar_max(lista, 0, ultima_posicion)

        auxiliar = lista[posicion_mayor]
        lista[posicion_mayor] = lista[ultima_posicion]

        lista[ultima_posicion] = auxiliar

        ultima_posicion -= 1
        print("DEBUG", lista)

def buscar_max(lista, inicial, final):
    """"""

    posicion_maximo = inicial

    for i in range(inicial + 1, final + 1):
        if lista[posicion_maximo] < lista[i]:
            posicion_maximo = i

    return posicion_maximo


def ordenamiento_mezcla(lista):
    """"""
    if len(lista) < 2:
        return lista

    medio = len(lista)//2
    izq = ordenamiento_mezcla(lista[:medio])
    der = ordenamiento_mezcla(lista[medio:])

    return mezclar(izq, der)

def mezclar(lista1, lista2):
    """"""
    i,j= 0, 0
    resultado = []

    while (i < len(lista1) and j < len(lista2)):
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    resultado += lista1[i:]
    resultado += lista2[j:]

    return resultado
