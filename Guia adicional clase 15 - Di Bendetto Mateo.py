'''1'''
def rango_con_for(numero_inicio, numero_fin):
    '''Esta funcion muestra los tres primeros impares del rango que se da por parametro'''
    contador = 3
    for x in range(numero_inicio, numero_fin):

        if x%2 != 0:
            contador -= 1
            print(x)
        if contador == 0:
            break


def rango_con_while():
    '''Esta funcion muestro los tres primero impares, empezando de 0'''
    contador = 3
    numero = 0
    while contador > 0:

        if numero%2 != 0:
            print (numero)
            contador -= 1
        numero= numero + 1












