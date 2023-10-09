while True: 
    try:
        input_str=input("Ingrese una fraccion en formato X/Y :")
        if "/" in input_str:
            print("Formato incorrecto. Debe ser X/Y")
            continue 
    
    x,y = map (int, input_str.split("/"))

    if x< 0 or y<=0: 
        print("X debe ser mayor o igual a 0 y Y debe ser mayor a 0")
        continue 
    if x/y <0.01:
        print("E")
    elif x/y > 0.99:
        print("F")
    else:
        percentage=round((x/y) *100)
        print("f{percentage}%")
        except ValueError:
        print("Error: Debe ingresar dos numeros enteros separados por "/")   
        except ZeroDivisionError:
            print("Error: El denominador Y no puede ser cero")
    else: 
        break    
          