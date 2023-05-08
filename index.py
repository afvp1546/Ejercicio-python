def menu():
    """Función que muestra el menú y llama a las funciones correspondientes según la opción elegida"""
    while True:
        print("Menú principal\n")
        print("1. Calculadora")
        print("2. Convertir distancia")
        print("3. Convertir masa")
        print("4. Área y perímetro de un círculo")
        print("5. Ingresar notas de una materia")
        print("6. Números primos de un número")
        print("7. Salir")
        opcion = input("Ingrese la opción deseada: ")
        if opcion == "1":
            calculadora()
        elif opcion == "2":
            convertir_distancia()
        elif opcion == "3":
            convertir_masa()
        elif opcion == "4":
            area_perimetro_circulo()
        elif opcion == "5":
            ingresar_notas()
        elif opcion == "6":
            numeros_primos()
        elif opcion == "7":
            salir = input("¿Está seguro que desea salir? (s/n): ")
            if salir.lower() == "s":
                print("Gracias por usar el programa")
                break
        else:
            print("Opción inválida")


def calculadora():
    """Función que muestra un menú con operaciones básicas de una calculadora"""
    print("Calculadora\n")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Volver al menú principal")
    op = int(input("Ingrese la opción deseada: "))
    if op == 5:
        return
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    if op == 1:
        print("El resultado es:", num1 + num2)
    elif op == 2:
        print("El resultado es:", num1 - num2)
    elif op == 3:
        print("El resultado es:", num1 * num2)
    elif op == 4:
        if num2 == 0:
            print("No se puede dividir por cero")
        else:
            print("El resultado es:", num1 / num2)
    else:
        print("Opción inválida")


def convertir_distancia():
    """Función que convierte una distancia dada en millas a kilómetros"""
    print("Convertir distancia\n")
    millas = float(input("Ingrese la distancia en millas: "))
    kilometros = millas * 1.60934
    print(millas, "millas equivalen a", kilometros, "kilómetros")


def convertir_masa():
    """Función que convierte una masa dada en libras a kilogramos"""
    print("Convertir masa\n")
    libras = float(input("Ingrese la masa en libras: "))
    kilogramos = libras * 0.453592
    print(libras, "libras equivalen a", kilogramos, "kilogramos")


def area_perimetro_circulo():
    """Función que calcula el área y el perímetro de un círculo dado su radio"""
    print("Área y perímetro de un círculo\n")
    radio = float(input("Ingrese el radio del círculo: "))
