def repite_hola(n):
    return "hola" * n

//

def info_del_usuario():
    nombre = input("Ingrese su nombre: ")
    edad = input("Igrese su edad: ")
    telefono = input("Ingrese su telefono: ")
    print("Su nombre es: {}, su edad es: {}, su telefono es: {}.".format(nombre, edad, telefono))

//

def anio_nacimiento():
    anio_actual = 2022
    edad = int(input("Ingrese su edad: "))
    anio_nacido = anio_actual - edad

    print("El anio de nacimiento es: {}.".format(anio_nacido))

//

def sumar():
    n1 = int(input("Ingrese un numero: "))
    n2 = int(input("Ingrese otro numero: "))

    resultado = n1 + n2

    print (resultado)

//

def promedio_notas():
    nota1 = int(input("Ingrese nota: "))
    nota2 = int(input("Ingrese nota: "))
    nota3 = int(input("Ingrese nota: "))
    nota4 = int(input("Ingrese nota: "))
    nota5 = int(input("Ingrese nota: "))

    Promedio = nota1