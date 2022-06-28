'''8.1'''
def diez_a_veinte():
    '''Muestra los numeros del 10 al 20'''
    numero = 10
    while numero <20  :
        print(numero)
        numero = numero + 1
    return numero


def calcular_factorial():
    '''Calcula el factorial de un numero'''
    numero = int(input("Ingrese un numero: "))
    factorial = 1
    while numero > 1:
        factorial = factorial * numero
        numero = numero -1
    return factorial

'''8.2'''
def validar_contrasenia():
    '''Funcion que pide al usuario una contrasenia y con un ciclo while dice si es correcta o no, si no es correcta se repite'''
    contrasenia = input("Ingrese la contrasenia: ")
    while contrasenia !=  str(contrasenia_real):
        print("Contasenia incorrecta")
        contrasenia = input("Ingrese la contrasenia: ")
    print ("contrasenia correcta")


'''8.3'''
def validar_contrasenia_tres_intentos(contrasenia_real):
    '''funcion que pide por parametro una contrasenia y otra al usuario, a partir de esto tiene tres intentos para poner bien la contrasenia de lo contrario se termina la funcion'''
    contrasenia = input("Ingrese contrasenia: ")
    intentos_maximos = 3
    intentos_fallidos = 0
    while contrasenia != str(contrasenia_real) and intentos_fallidos < intentos_maximos:
        intentos_fallidos = intentos_fallidos + 1
        if intentos_fallidos == intentos_maximos:
            break
        contrasenia = str(input("Ingrese contrasenia: "))
    if intentos_fallidos == intentos_maximos:
        print("Demasiados intentos")
        return False
    print("Ingreso exitoso")
    return True


'''8.4'''
def leer_centinela():
    nota_materia = int(input("ingrese una nota o -1 para terminar: "))
    return nota_materia


def promedio():
    '''Pide al usuario numero de materia y sus nota y devuelve un promedio de las mismas'''
    sumatoria_notas = 0
    nota_materia = leer_centinela()
    numero_notas_ingresadas = 0
    while nota_materia != -1:
        if (nota_materia >= 1) and (nota_materia <11) :
            sumatoria_notas += nota_materia
            numero_notas_ingresadas += 1

        nota_materia = leer_centinela()

    return(sumatoria_notas/numero_notas_ingresadas)

'''8.5'''
def numero_primo(numero):
    '''Esta funcion recibe por parametro un numero y dice si es primo o no'''
    x = 2
    primo = True

    while primo and x < numero:
        if numero%x == 0:
            primo =  False

        x+= 1
    print(primo)

'''8.6'''
def numero_inico_fin():
    '''Esta funcion le pide dos numeros al usuario de inicio y de fin y le devuelve si son divisible por 5 o por 7'''
    numero_inicio = int(input("ingrese un numero de inicio: "))
    numero_fin = int(input("ingrese un numero final: "))

    while numero_inicio > numero_fin:
        print("Ingreso mal los valores, ingreselos nuevamente")
        numero_inicio = int(input("ingrese un numero de inicio: "))
        numero_fin = int(input("ingrese un numero final: "))

    contador = 0
    for x in range(numero_inicio, numero_fin):
        if (x%5==0) and (x%7==0):
            contador = contador + 1
    return contador























