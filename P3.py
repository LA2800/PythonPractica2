
radio=float(input("Ingrese el radio del circulo: "))
circulo= circulo(radio)
area=circulo.calcular_area()
if isinstance (area,str):
    print(area)
else: 
    print(f"El area del circulo con radio {radio} es: {area:.2f}")
except ValueError:
    print("Error: Ingrese un valor numerico valido para el radio del circulo. ")

