'''1'''
def palabra_numero():
    '''Esta funcion al usuario darle un numero y una palabra, te muestra los numeros del 1 al 50 y donde ese numero tiene un multiplo lo cambia por la palabra dada'''
    palabra = input("Ingrese una palabra: ")
    numero = int(input("Ingrese un numero: "))

    for x in range(1,50,1):
        if x%numero==0:
            print (palabra)
        else:
            print(x)

'''2'''
def validar_cumpleanios(dia_actual, mes_actual, dia_cumple, mes_cumple):
    '''Esta funcion lo que hace es que al ingresar por parametros dia y mes, debera validar si es true o false, con los datos que le ingresa en el mismo parametro'''

    if (dia_actual != dia_cumple) and (mes_actual == mes_cumple):
        return False
    elif (dia_actual == dia_cumple) and (mes_actual != mes_cumple):
        return False
    elif (dia_actual != dia_cumple) and (mes_actual != mes_cumple):
        return False
    else:
        return True

'''3'''
def entrada_boliche(dia_actual, mes_actual):
    '''Esta funcion dice si una persona puede pasar al boliche, ingresando como parametros el dia actual, el mes actual, y si el usuario cumple años el mismo dia entra gratis, de lo contrario paga, y si es menor de edad no entra'''
    edad= int(input("Ingrese su edad: "))
    dia_cumple = int(input("Ingrese su dia de nacimiento: "))
    mes_cumple = int(input("Ingrese su mes de  nacimiento: "))
    cumpleanios = validar_cumpleanios(dia_actual, mes_actual, dia_cumple, mes_cumple)

    if edad < 18:
        print ("No puede pasar")
    elif (edad >= 18) and (dia_cumple == cumpleanios):
        print ("Pasa gratis, feliz cumpleaños")
    elif (edad >= 18) and (dia_actual != cumpleanios ) or (mes_actual != cumpleanios):
        print ("Pasa y vaya a la caja")
    else:
        print ("Ingrese bien los datos")
