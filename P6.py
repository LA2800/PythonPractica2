class Producto:
    def __init__(self, nombre, numero_de_pieza, año, precio):
        self.nombre = nombre
        self.numero_de_pieza = numero_de_pieza
        self.año = año
        self.precio = precio

    def __str__(self):
        return f"Producto: {self.nombre}, Número de Pieza: {self.numero_de_pieza}, Año: {self.año}, Precio: ${self.precio:.2f}"


class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        for producto in self.productos:
            print(producto)

    def filtrar_por_año(self, año):
        productos_filtrados = [producto for producto in self.productos if producto.año == año]
        if productos_filtrados:
            print(f"Productos del año {año}:")
            for producto in productos_filtrados:
                print(producto)
        else:
            print(f"No hay productos disponibles del año {año} en el catálogo.")


