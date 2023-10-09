largo = float (input("Ingrese el largo del rectangulo: "))
ancho = float(input("Ingrese el ancho del rectangulo: "))
rectangulo=Rectangulo(largo, ancho)
area=rectangulo.calcular_area()
if isinstance (area,str):
    print(area)
else:
    print(f"El area del rectangulo con largo {largo} y ancho {ancho} es: {area:.2f}:")
except ValueError:
    print("Error: Ingrese valores numericos validos para el largo y el ancho del rectangulo")