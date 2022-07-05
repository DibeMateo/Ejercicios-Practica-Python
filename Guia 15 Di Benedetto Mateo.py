"""Guia 15"""
#15.1
ruta = "C:\\Users\\Alumno 2022\\Desktop\\Programador\\ejercicio 1"

def imprimir_compras(ruta, n):
    """Esta funcion recibe la ruta del archivo y devuelve en numero de compras"""
    try:

        with open(ruta) as archivo:
            archivo.readline()
            for x in range(n):
                linea = archivo.readline()
                linea = linea.rstrip("\n")
                print(linea)

    except IOError:
        print("No se pudo encontrar el archivo.")

#15.2
ruta = "C:\\Users\\Alumno 2022\\Desktop\\Programador\\codigos"

def imprimir_codigo(ruta):
    """Esta funcion recibe como parametro una ruta al archivo e imprime los codigos."""

    try:
        with open(ruta) as archivo:
            archivo.readline()
            for linea in archivo:
                linea = linea.rstrip("\n")
                print(linea)

    except IOError:
        print("No se pudo encontrar el archivo.")

#15.3

ruta = "C:\\Users\\Alumno 2022\\Desktop\\Programador\\notas-alumnos.txt"

def lista_tuplas_notas(ruta_archivo):
    """Esta funcion recibe la ruta de el archivo y devuelve las notas en una lista de tuplas."""
    lista = []
    try:
        with open(ruta_archivo) as archivo:
            archivo.readline()
            for linea in archivo:
                linea = linea.rstrip("\n")
                alumno = linea.split(' - ')
                tupla = (alumno[0], alumno[1], alumno[2], alumno[3], alumno[4], alumno[5])
                lista.append(tupla)
            return lista

    except IOError:
        print("No se pudo encontrar el archivo.")


def promedio_alumnos():
    """Esta funcion devuelve el promedio del alumnos en el caso de que lo encuentre en la lista."""
    nombre = input("Ingrese el nombre del alumno: ")
    lista = lista_tuplas_notas(ruta)

    for alumno in lista:
        if nombre in alumno:
            nota = (int(alumno[1]) + int(alumno[2]) + int(alumno[3]) + int(alumno[4]) + int(alumno[5]))
            nota = nota/5

            if nota >=6:
                print("Alumno aprobado.")

            elif nota <6:
                print("Alumno desaprobado.")
            return nota


    print("No se encontro al alumno.")


