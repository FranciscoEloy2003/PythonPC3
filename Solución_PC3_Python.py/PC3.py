#Problema 1: Implemente un programa que solicite al usuario una fracción, con formato X/Y, donde cada uno
# de X e Y es un número entero, y luego muestra, como un porcentaje redondeado al número entero más cercano.
def obtener_porcentaje(fraction):
    try:
        numerador, denominador = map(int, fraction.split('/'))
        if denominador == 0:
            raise ZeroDivisionError("El denominador no puede ser cero.")
        if numerador > denominador:
            raise ValueError("El numerador debe ser menor o igual al denominador.")
        
        porcentaje = (numerador / denominador) * 100
        
        if porcentaje < 1:
            return 'E'
        elif porcentaje > 99:
            return 'F'
        else:
            return f'{int(round(porcentaje))}%'
    
    except ValueError as e:
        print("Error:", e)
        return None
    except ZeroDivisionError as e:
        print("Error:", e)
        return None

if __name__ == '__main__':
    while True:
        fraction = input("Ingrese una fracción en formato X/Y (donde X e Y son enteros): ")
        result = obtener_porcentaje(fraction)
        if result is not None:
            print("Cantidad de combustible en el tanque:", result)
            break

#Problema 2: Cree un programa que solicite al usuario una lista de calificaciones separadas por comas.
def obtener_calificaciones():
    while True:
        try:
            entrada = input("Ingrese las calificaciones separadas por comas: ")
            calificaciones = entrada.split(',')
            calificaciones_enteros = []

            for calificacion in calificaciones:
                calificacion_entero = round(float(calificacion.strip()))  # Convertir a flotante, redondear y luego a entero
                if 0 <= calificacion_entero <= 20:
                    calificaciones_enteros.append(calificacion_entero)
                else:
                    print(f"La calificación {calificacion_entero} está fuera del rango permitido (0-20). Se ignorará.")

            print("Calificaciones ingresadas:", calificaciones_enteros)
            break
        except ValueError:
            print("Error: Por favor ingrese solo números separados por comas.")

obtener_calificaciones()

#Problema 3: Cree un programa que solicite al usuario una lista 
class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        return self.largo * self.ancho

# Ejemplo de uso: Definir una clase llamada “CIRCULO” la cual contenga un atributo inicializador radio.
largo_rectangulo = float(input("Ingrese el largo del rectángulo: "))
ancho_rectangulo = float(input("Ingrese el ancho del rectángulo: "))
rectangulo = Rectangulo(largo_rectangulo, ancho_rectangulo)
print("El área del rectángulo es:", rectangulo.calcular_area())


#Problema 4: Definir una clase llamada “RECTANGULO” que puede ser construida por los atributos largo y ancho.
class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        return self.largo * self.ancho

# Ejemplo de uso:
largo_rectangulo = float(input("Ingrese el largo del rectángulo: "))
ancho_rectangulo = float(input("Ingrese el ancho del rectángulo: "))
rectangulo = Rectangulo(largo_rectangulo, ancho_rectangulo)
print("El área del rectángulo es:", rectangulo.calcular_area())


#Problema 5: Cree una clase Alumno e inicialícela con el nombre y el número de registro.
class Alumno:
    def __init__(self, nombre, numero_registro):
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.edad = None
        self.notas = []

    def display(self):
        print("Información del estudiante:")
        print("Nombre:", self.nombre)
        print("Número de registro:", self.numero_registro)
        if self.edad is not None:
            print("Edad:", self.edad)
        else:
            print("Edad: No especificada")
        if self.notas:
            print("Notas:", self.notas)
        else:
            print("Notas: No especificadas")

    def set_age(self, edad):
        self.edad = edad

    def set_notas(self, *notas):
        self.notas = list(notas)

# Solicitar al usuario que ingrese los datos del estudiante
nombre = input("Ingrese el nombre del estudiante: ")
numero_registro = input("Ingrese el número de registro del estudiante: ")
edad = int(input("Ingrese la edad del estudiante: "))
notas = input("Ingrese las notas del estudiante separadas por espacios: ").split()

# Crear instancia de la clase Alumno y establecer los datos ingresados
alumno1 = Alumno(nombre, numero_registro)
alumno1.set_age(edad)
alumno1.set_notas(*notas)

# Mostrar la información del estudiante
alumno1.display()


#Problema 6: Una tienda de autopartes necesita un programa para catalogar sus productos
class Producto:
    def __init__(self, nombre, año, precio):
        self.nombre = nombre
        self.año = año
        self.precio = precio

class Catalogo:
    def __init__(self):
        self.productos = [
            Producto("Desarmadores", 2024, 250),
            Producto("Matracas", 2022, 180),
            Producto("Manómetro", 2020, 260),
            Producto("Martillos", 2021, 255),
            Producto("Multímetro", 2023, 275)  # Precio actualizado para el Multímetro
        ]

    def mostrar_lista_productos(self):
        print("Lista de herramientas disponibles:")
        for i, producto in enumerate(self.productos, 1):
            print(f"{i}. {producto.nombre}")

    def buscar_producto(self):
        respuesta = input("¿Está buscando una herramienta en específico? (Sí/No): ").lower()
        if respuesta == "sí" or respuesta == "si":
            herramienta = input("Ingrese el nombre de la herramienta que está buscando: ").capitalize()
            encontrado = False
            for producto in self.productos:
                if producto.nombre == herramienta:
                    print(f"Información de {herramienta}:")
                    print(f"Año: {producto.año}, Precio: {producto.precio} $")
                    encontrado = True
                    break
            if not encontrado:
                print("Herramienta no encontrada. Lista disponible:")
                self.mostrar_lista_productos()
        elif respuesta == "no":
            self.mostrar_lista_productos()
            numero = int(input("Ingrese el número de la herramienta para obtener información detallada: "))
            if 1 <= numero <= len(self.productos):
                producto = self.productos[numero - 1]
                print(f"Información de {producto.nombre}:")
                print(f"Año: {producto.año}, Precio: {producto.precio} $")
            else:
                print("Número inválido. Por favor seleccione un número válido.")

# Ejemplo de uso:
catalogo = Catalogo()
catalogo.buscar_producto()

#Problema 7: Crea los puntos A(2, 3), B(5,5), C(-3, -1) y D(0,0) e imprimelos por pantalla.
import math

# Definición de los puntos
punto_A = (2, 3)
punto_B = (5, 5)
punto_C = (-3, -1)
punto_D = (0, 0)

# Función para determinar el cuadrante de un punto
def determinar_cuadrante(punto):
    x, y = punto
    if x > 0 and y > 0:
        return "Primer cuadrante"
    elif x < 0 and y > 0:
        return "Segundo cuadrante"
    elif x < 0 and y < 0:
        return "Tercer cuadrante"
    elif x > 0 and y < 0:
        return "Cuarto cuadrante"
    else:
        return "En el origen"

# Función para calcular el vector entre dos puntos
def calcular_vector(punto1, punto2):
    x1, y1 = punto1
    x2, y2 = punto2
    vector = (x2 - x1, y2 - y1)
    return vector

# Función para calcular la distancia entre dos puntos
def calcular_distancia(punto1, punto2):
    x1, y1 = punto1
    x2, y2 = punto2
    distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distancia

# Determinar cuadrantes de los puntos A, B y C
print("Cuadrante de A:", determinar_cuadrante(punto_A))
print("Cuadrante de C:", determinar_cuadrante(punto_C))
print("Cuadrante de D:", determinar_cuadrante(punto_D))

# Calcular vectores AB y BA
vector_AB = calcular_vector(punto_A, punto_B)
vector_BA = calcular_vector(punto_B, punto_A)
print("Vector AB:", vector_AB)
print("Vector BA:", vector_BA)

# Calcular distancia entre A y B, y entre B y A
distancia_AB = calcular_distancia(punto_A, punto_B)
distancia_BA = calcular_distancia(punto_B, punto_A)
print("Distancia entre A y B:", distancia_AB)
print("Distancia entre B y A:", distancia_BA)

# Determinar el punto más lejano al origen (0,0)
distancias_al_origen = {
    'A': calcular_distancia(punto_A, (0, 0)),
    'B': calcular_distancia(punto_B, (0, 0)),
    'C': calcular_distancia(punto_C, (0, 0))
}
punto_mas_lejano = max(distancias_al_origen, key=distancias_al_origen.get)
print("El punto más lejano al origen es:", punto_mas_lejano)

# Calcular dimensiones del rectángulo formado por los puntos A y B
base_rectangulo = abs(punto_A[0] - punto_B[0])
altura_rectangulo = abs(punto_A[1] - punto_B[1])
area_rectangulo = base_rectangulo * altura_rectangulo
print("Base del rectángulo:", base_rectangulo)
print("Altura del rectángulo:", altura_rectangulo)
print("Área del rectángulo:", area_rectangulo)


#Problema 8: Genere 20 números enteros aleatorios entre 0 y 100
import random

def generar_numeros_aleatorios():
    numeros_aleatorios = [random.randint(0, 100) for _ in range(20)]
    return numeros_aleatorios

def mostrar_lista(lista):
    print("Lista de números generados aleatoriamente:")
    for numero in lista:
        print(numero, end=" ")
    print()

def ordenar_y_mostrar(lista):
    lista_ordenada = sorted(lista)
    print("Lista ordenada:")
    for numero in lista_ordenada:
        print(numero, end=" ")
    print()

if __name__ == "__main__":
    numeros = generar_numeros_aleatorios()
    mostrar_lista(numeros)
    ordenar_y_mostrar(numeros)


#Problema 9: Cree un módulo llamado operaciones.py el cual contendrá 4 funciones
def suma(a, b):
    try:
        resultado = a + b
        return resultado
    except TypeError:
        print("Error: Tipo de dato no válido.")
        return None

def resta(a, b):
    try:
        resultado = a - b
        return resultado
    except TypeError:
        print("Error: Tipo de dato no válido.")
        return None

def producto(a, b):
    try:
        resultado = a * b
        return resultado
    except TypeError:
        print("Error: Tipo de dato no válido.")
        return None

def division(a, b):
    try:
        if b == 0:
            raise ZeroDivisionError
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        print("Error: No es posible dividir entre cero.")
        return None
    except TypeError:
        print("Error: Tipo de dato no válido.")
        return None

def menu_operaciones():
    print("Operaciones disponibles:")
    print("1. Suma")
    print("2. Resta")
    print("3. Producto")
    print("4. División")

    seleccion = input("Seleccione el número de la operación que desea realizar: ")
    return seleccion

def obtener_numeros():
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        return num1, num2
    except ValueError:
        print("Error: Tipo de dato no válido.")
        return None, None

def realizar_operacion(operacion, num1, num2):
    if operacion == '1':
        resultado = suma(num1, num2)
    elif operacion == '2':
        resultado = resta(num1, num2)
    elif operacion == '3':
        resultado = producto(num1, num2)
    elif operacion == '4':
        resultado = division(num1, num2)
    else:
        print("Error: Selección de operación inválida.")
        resultado = None
    return resultado

# Ejemplo de uso
while True:
    seleccion = menu_operaciones()
    num1, num2 = obtener_numeros()
    if num1 is not None and num2 is not None:
        resultado = realizar_operacion(seleccion, num1, num2)
        if resultado is not None:
            print("El resultado es:", resultado)
            break
    else:
        continuar = input("¿Desea intentarlo nuevamente? (Sí/No): ").lower()
        if continuar != "sí" and continuar != "si":
            break

#Problema 10: Cree un menú 
import math

def calcular_area_circulo():
    radio = float(input("Ingrese el radio del círculo: "))
    area = math.pi * radio ** 2
    print("El área del círculo es:", area)

def calcular_area_rectangulo():
    ancho = float(input("Ingrese el ancho del rectángulo: "))
    largo = float(input("Ingrese el largo del rectángulo: "))
    area = ancho * largo
    print("El área del rectángulo es:", area)

def calcular_area_cuadrado():
    lado = float(input("Ingrese el lado del cuadrado: "))
    area = lado ** 2
    print("El área del cuadrado es:", area)

def menu():
    while True:
        print("Menú:")
        print("1. Calcular el área de un círculo")
        print("2. Calcular el área de un rectángulo")
        print("3. Calcular el área de un cuadrado")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1-4): ")
        
        if opcion == '1':
            calcular_area_circulo()
        elif opcion == '2':
            calcular_area_rectangulo()
        elif opcion == '3':
            calcular_area_cuadrado()
        elif opcion == '4':
            print("Muchas gracias, que tenga un buen día!!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")

# Ejecutar el menú
menu()
