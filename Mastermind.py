'''Este es el codig del juego Mastermind: el jeugo consiste que el jugardor da un codigo y tiene que adivinar el codigo generado por la computadora. Con cada intento que falla se le dan pistas al jugador'''


import random

def mastermind():
    '''Funcion principal de Mastermind'''
    print("Bienvenido a Masterdmind")
    print ("Tienes que adivinar un numero de cuatro digitos diferentes")

    codigo = elegir_codigo()
    intentos = 1
    propuesta = input("Proponga un codigo: ")

    while propuesta != codigo:
        intentos+= 1
        aciertos, coincidencias = analizar_propuesta(propuesta, codigo)
        print("Tu propuesta ({}) tiene {} aciertos y {} coincidencias.".format(propuesta, aciertos, coincidencias))
        propuesta = input("propone otro codigo: ")

    print ("Felicitaciones ! adivinaste el codigo en {} intestos.".format(intentos))


def elegir_codigo():
    '''Devuelve un codigo de 4 digitos al azar'''
    digitos = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    codigo = ""
    for i in range(4):
        candidato = random.choice(digitos)
        while candidato in codigo:
            candidato = random.choice(digitos)
        codigo = codigo + candidato
    return codigo


def analizar_propuesta(propuesta, codigo):
    aciertos= 0
    coincidencias = 0
    for i in range(4):
        if propuesta[i] == codigo[i]:
            aciertos = aciertos + 1
        elif propuesta[i] in codigo:
            coincidencias = coincidencias + 1
    return aciertos, coincidencias