from circulo_rectangulo import CIRCULO, RECTANGULO  # Importa las clases desde los módulos correspondientes

def calcular_area_circulo():
    radio = float(input("Ingrese el radio del círculo: "))
    circulo = CIRCULO(radio)
    area = circulo.calcular_area()
    print(f"El área del círculo con radio {radio} es: {area:.2f}")

def calcular_area_rectangulo():
    largo = float(input("Ingrese el largo del rectángulo: "))
    ancho = float(input("Ingrese el ancho del rectángulo: "))
    rectangulo = RECTANGULO(largo, ancho)
    area = rectangulo.calcular_area()
    print(f"El área del rectángulo con largo {largo} y ancho {ancho} es: {area:.2f}")

def calcular_area_cuadrado():
    lado = float(input("Ingrese el lado del cuadrado: "))
    rectangulo = RECTANGULO(lado, lado)  # Un cuadrado es un caso especial de rectángulo
    area = rectangulo.calcular_area()
    print(f"El área del cuadrado con lado {lado} es: {area:.2f}")

while True:
    print("\nMenú:")
    print("1. Calcular el área de un círculo")
    print("2. Calcular el área de un rectángulo")
    print("3. Calcular el área de un cuadrado")
    print("4. Salir")

    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == '1':
        calcular_area_circulo()
    elif opcion == '2':
        calcular_area_rectangulo()
    elif opcion == '3':
        calcular_area_cuadrado()
    elif opcion == '4':
        break
    else:
        print("Opción no válida. Por favor, elija una opción válida del menú.")
