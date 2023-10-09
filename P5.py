class Alumno:
    def __init__(self, nombre, numero_registro):
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.edad = None  # Inicialmente la edad se establece como None
        self.notas = []   # Inicialmente, la lista de notas está vacía

    def display(self):
        print("Información del estudiante:")
        print("Nombre:", self.nombre)
        print("Número de Registro:", self.numero_registro)
        if self.edad is not None:
            print("Edad:", self.edad)
        else:
            print("Edad: No especificada")
        if self.notas:
            print("Notas:", ", ".join(map(str, self.notas)))
        else:
            print("Notas: No especificadas")

    def setAge(self, edad):
        if edad >= 0:
            self.edad = edad
        else:
            print("La edad no puede ser un valor negativo.")

    def setNota(self, nota):
        if 0 <= nota <= 100:
            self.notas.append(nota)
        else:
            print("La nota debe estar en el rango de 0 a 100.")

