def obtener_calificaciones():
    while True: 
        try: 
            calificaciones_str=input("Ingrese las calificaciones separadas por comas: ")
            calificaciones_lista=calificaciones_str.split(",")
            calificaciones_enteros=[]

            for calificaciones_str in calificaciones_lista:
                calificacion=int(calificaciones_str.strip())
                calificaciones_enteros.append(calificacion)
            
            return calificaciones_enteros
        
        except ValueError:
            print("Error: Alguno de los valores no es un numero entero valido. Intente de nuevo ")

calificaciones=obtener_calificaciones()
print("Calificaciones ingresadas: ", calificaciones)
