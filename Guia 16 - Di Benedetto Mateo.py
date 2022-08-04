#16.1

ruta = "C:\\Users\\Alumno 2022\\Desktop\\Programador\\saludo.txt"
ruta2= "C:\\Users\\Alumno 2022\\Desktop\\Programador\\copia.txt"

def copiar_archivo(ruta):
    """Esta funcion recibe un archivo, y devuelve otro igual con el mismo contenido."""

    with open(ruta, "r") as archivo:
        with open(ruta2, "w") as archivo2:
            for cadena in archivo:
                print(cadena)
                archivo2.write(cadena)

#16.2
import random
caracteres = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
ruta = "C:\\Users\\pc\\OneDrive\\Escritorio\\Programación\\Nueva carpeta\\Cosas imp\\codigos_guia_16.txt"

def generar_codigo():
    """Esta funcion genera un codigo aleatorio y lo devuelve."""
    codigo_random = []
    for codigo in range(4):
        codigo_random += random.choices(caracteres)
    return codigo_random


def agregar_codigo_archivo(ruta):
    """Esta funcion agrega el codigo de la funcion anterio a un documento de texto."""

    with open(ruta, "a+") as archivo:
        archivo.write(str(generar_codigo()))


#16.3
ruta = "C:\\Users\\Alumno 2022\\Desktop\\Programador\\ejercicio_16.3.txt"

def abrir_agenda(ruta):
    """Esta funcion recibe una ruta, muestra los contactos, y los añade."""
    with open(ruta, "r") as agenda:
        contactos_encontrados = []
        contacto = input("Ingrese el nombre del contacto: ")

        agenda.readline()

        for linea in agenda:
            if contacto in linea:
                linea = linea.rstrip("\n")
                contactos_encontrados.append(linea)
                return contactos_encontrados
        agregar_contacto()


def agregar_contacto():
    """Esta funcion agrega un contaco a la lista."""
    print("¿Desea agregar un contacto a la lista?")
    respuesta_usuario = int(input("1= Si, 2= No \n"))
    espacio = " - "
    with open (ruta, "a+") as agenda:

        if respuesta_usuario == 1:
            nombre_contacto = input("Ingrese el nombre del contacto: ")
            telefono = input("Ingrese el telefono del contacto: ")
            agenda.write(nombre_contacto )
            agenda.write(espacio)
            agenda.write(telefono )

        else:
            print("Salio de la agenda!")
