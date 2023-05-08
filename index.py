def menu():
    """Menú del sistema"""
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
            circulo()
        elif opcion == "5":
            notas()
        elif opcion == "6":
            numeros_primos()
        elif opcion == "7":
            salir = input("¿Está seguro que desea salir? (s/n): ")
            if salir.lower() == "s":
                print("Gracias por usar el programa")
                break
        else:
            print("Opción inválida")

# Función que describe los valores basicos de una calculadora
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


# Función para convertir metros a km y ft
def convertir_distancia():
    print("Bienvenido al conversor de distancia")
    distancia = float(input("Ingrese la distancia en metros: "))
    opcion = input("Ingrese la unidad a la que desea convertir (km, ft): ")
    if opcion == "km":
        resultado = distancia / 1000
    elif opcion == "ft":
        resultado = distancia / 0.3048
    else:
        print("Unidad no válida")
        return
    print("El resultado de la conversión es: ", resultado, opcion)

# Función para convertir gramos a kg o lb
def convertir_masa():
    print("Bienvenido al conversor de masa")
    masa = float(input("Ingrese la masa en gramos: "))
    opcion = input("Ingrese la unidad a la que desea convertir (kg, lb): ")
    if opcion == "kg":
        resultado = masa / 1000
    elif opcion == "lb":
        resultado = masa / 453.592
    else:
        print("Unidad no válida")
        return
    print("El resultado de la conversión es: ", resultado, opcion)

# Función para calcular el perimetro y area de un circulo
def circulo():
    print("Bienvenido al cálculo de área y perímetro de un círculo")
    radio = float(input("Ingrese el radio del círculo: "))
    area = 3.1416 * radio ** 2
    perimetro = 2 * 3.1416 * radio
    print("El área del círculo es: ", area)
    print("El perímetro del círculo es: ", perimetro)

# Función para la opción 5: ingresar n notas de una materia
def notas():
    print("Bienvenido al ingreso de notas")
    n = int(input("Ingrese la cantidad de notas a ingresar: "))
    suma = 0
    for i in range(n):
        nota = float(input("Ingrese la nota {}: ".format(i+1)))
        suma += nota
    promedio = suma / n
    print("El promedio es: ", promedio)
    if promedio >= 3:
        print(f"Felicitaciones, paso la materia con {promedio}")
    else:
        print(f"Lo siento, perdio la materia con {promedio}")

# Función para calcular número primos
def numeros_primos():
    num = int(input("Ingrese un número: "))
    primos = []
    for i in range(2, num+1):
        es_primo = True
        for j in range(2, int(i/2)+1):
            if i % j == 0:
                es_primo = False
                break
        if es_primo:
            primos.append(i)
    print("Los números primos de {} son: {}".format(num, primos))


menu()