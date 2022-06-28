'''7.2'''
def numero_primo():
    '''Funcion que indica si es un numero primo o no'''
    numero = int(input("ingrese un numero: "))
    for x in range(2,numero):
        if numero%x==0:
            print("No es primo")
            return
    print("Es primo")


'''7.3'''
def anio_bisiesto(anio):
    '''Ingresando un año esta funcion dice si es bisiesto o no, obteniendo como resto 0 diviendolo por 4, 100 y 400'''
    bisiesto= False
    if (anio%4==0) or (anio%100==0) and (anio%400==0):
        print("Anio bisiesto")
        bisiesto = True
    else:
        print("Anio no bisiesto")
    return bisiesto

'''7.4'''
def divisibles_3_5():
    '''Funcion que recorre numeros de 1 al 100 y cuando es divisible por 3 imprime "zip", cuando sea divisible por 5 imprima "zap" y cuando se divisible por los dos "zipzap"'''
    for x in range(1,100,1):
        if (x%3==0) and (x%5==0):
            print("Zipzap")
        elif x%3==0:
            print("Zip")
        elif x%5==0:
            print("Zap")

'''7.5'''
def usuario_contra(usuario,contra):
    '''Esta funcion comprueba que el usuario y la contrasenia sean correctos, sino notifica cual es el incorrecto o cuales'''

    usuario_ingresado = input("Ingrese el usuario:")
    contrasenia= input("Ingrese la contrasenia: ")
    if usuario_ingresado != usuario:
        print("Usuario incorrecto")
    elif contra != contrasenia:
        print("Contrasenia incorrecta")
    elif (contra!= contrasenia) and (usuario!=usuario_ingresado):
        print("Ambos datos son invalidos")
    elif (contra == contrasenia) and (usuario==usuario_ingresado):
        print("Ingreso exitoso")
    else:
        print("Error")

'''7.6'''
def meses_anios():
    '''El usuario ingresa un anio y un mes, y la funcion le devuelve cuantos dias tiene ese mes de ese anio'''
    anio_elegido_usuario = int(input("ingrese un anio: "))
    mes_elegido_usuario = int(input("ingrese un mes en numero: "))
    bisiesto = anio_bisiesto(anio_elegido_usuario)

    if (mes_elegido_usuario==1) or (mes_elegido_usuario==3) or (mes_elegido_usuario==5) or (mes_elegido_usuario==7) or (mes_elegido_usuario==8) or (mes_elegido_usuario==10) or (mes_elegido_usuario==12):
        print("Este mes tiene 31 dias")
    elif (mes_elegido_usuario==4) or (mes_elegido_usuario==6) or (mes_elegido_usuario==9) or (mes_elegido_usuario==11):
        print("Este mes tiene 30 dias")
    elif (mes_elegido_usuario == 2) and bisiesto :
        print("El mes tiene 29 dias")
    elif (bisiesto != anio_elegido_usuario) :
        print("El mes tiene 28 dias")
    else:
        print("Ingrese un mes o un anio valido")










































