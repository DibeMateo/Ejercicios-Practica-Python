'''1'''
def calculador_precios():
    '''Esta funcion le pide al usuario que ingrese las compras que hizo y con que metodo quiere pagar, si este paga en efectivo se le descuenta el 15% si paga con debito no hace nada y si paga con credito a partir de 6 cuotas se le aumenta el 5%, posterior le muestra lo que pago y de que forma'''
def menu_pago():
    monto_a_pagar = int(input("Ingrese el monto a pagar: "))

    print("1 - Pago Efectivo")
    print("2 - Pago con debito")
    print("3 - Pago con credito")
    print("4 - Cancelar pago")


    eleccion_usuario = int(input("Ingrese una opcion: "))

    if eleccion_usuario == 1:
        print("Se pago en efectivo son: {}".format( monto_a_pagar * 0.85))
    elif eleccion_usuario == 2:
        print("Se pago con debito son: {} ".format(monto_a_pagar))
    elif eleccion_usuario == 3:
        cuotas = int(input("Ingrese el numero de cuotas: "))
        if cuotas >= 6:
            print("Se pago con credito son: {}".format(monto_a_pagar * 1.05))
        else:
            print("Se pago con credito en menos de 6 cuotas, son: {}".format(monto_a_pagar))
    elif eleccion_usuario == 4:
        print("El pago se cancelo con exito")
    else:
        print("Error al ingresar los numero")

'''2'''
def sumar():
    '''Pide al usuario una cantidad de numeros, los suma y devuelve la suma.'''
    cantidad = int(input("Cuantos numero quiere sumar?"))
    suma = 0
    for x in range(cantidad):
        numero = int(input("Ingrese un numero: "))
        suma = suma + numero
    return suma

def restar():
    '''Pide al usuario una cantidad de numeros, los resta y luego devuelve la resta'''
    cantidad = int(input("Cuantos numero quiere restar?"))
    resta = int(input("Ingrese un numero: "))
    for x in range(cantidad-1):
        numero = int(input("Ingrese un numero: "))
        resta = resta - numero
    return resta

def multiplicar():
    '''Pide dos numero al usuario y devuelve el resultado del producto'''
    n1 = int(input("Ingrese un numero: "))
    n2 = int(input("Ingrese otro numero: "))
    return n1 * n2

def dividir():
    '''Pide dos numero y devuelve el resultado.'''
    numerador = int(input("Ingrese un numero: "))
    divisor = int(input("Ingrese otro numero: "))
    if divisor == 0:
        print("No se puede dividir por cero")
        return
    else:
        return numerador/divisor


def main():
    '''Muestra el menu de la calculadora. Llama la funcion que elija el usuario'''
    print("Elija una opcion: ")
    print("1 - Sumar")
    print("2 - Restar")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Salir")

    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        return sumar()
    elif opcion == 2:
        return restar()
    elif opcion == 3:
        return multiplicar()
    elif opcion == 4:
        return dividir()
    elif opcion == 5:
        return
    else:
        print("Ingrese una opcion valida.")

