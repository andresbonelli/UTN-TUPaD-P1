#################################################################
#                                                               #
#  TUPaD - Programacion I                                       #
#  Alumno: ANDRES BONELLI                                       #
#  Práctico 6: Estructuras de datos complejas                   #
#                                                               #
#################################################################

"""
1) Dado el diccionario precios_frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}
Añadir las siguientes frutas con sus respectivos precios:
● Naranja = 1200
● Manzana = 1500
● Pera = 2300
"""
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas.update({'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300})
print(precios_frutas)

"""
2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
● Banana = 1330
● Manzana = 1700
● Melón = 2800
"""
precios_frutas.update({'Banana': 1330, 'Manzana': 1700, 'Melón': 2800})
print(precios_frutas)

"""
3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
precios.
"""
lista_frutas = list(precios_frutas.keys())
print(lista_frutas)

"""
4) Crear una clase llamada Persona que contenga un método __init__ con los atributos
nombre, pais y edad y el método saludar. El método saludar debe imprimir por pantalla un
mensaje de salud que siga la estructura "¡Hola! Soy [nombre], vivo en [pais] y tengo [edad]
años."
"""
class Persona:
    def __init__(self, nombre, pais, edad):
        self.nombre = nombre
        self.pais = pais
        self.edad = edad

    def saludar(self):
        print(f"¡Hola! Soy {self.nombre}, vivo en {self.pais} y tengo {self.edad} años.")


"""
5) Crear una clase llamada Circulo que contenga el atributo radio y los métodos calcular_area y
calcular_perimetro. Dichos métodos deben calcular el parámetro correspondiente.
Ayuda: el módulo math puede ser de utilidad para usar la constante 𝜋.
"""
import math
class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

"""
6) Dado un string con paréntesis "()", "{}", "[]", verifica si están correctamente
balanceados usando una pila.
Ejemplo de entrada y salida:
balanceado("({[]})") -> True
balanceado("({[})") -> False
"""
class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        return self.items.pop() if not self.esta_vacia() else None

    def ver_tope(self):
        return self.items[-1] if not self.esta_vacia() else None

def balanceado(cadena):
    pila = Pila()
    for caracter in cadena:
        if caracter in "({[":
            pila.apilar(caracter)
        elif caracter in ")}]":
            if pila.esta_vacia():
                return False
            ultimo = pila.ver_tope()
            if (caracter == ")" and ultimo != "(") or (caracter == "}" and ultimo != "{") or (caracter == "]" and ultimo != "["):
                return False
            pila.desapilar()
    return pila.esta_vacia()


"""
7) Usa una cola para simular un sistema de turnos en un banco. La cola debe permitir:
● Agregar clientes (encolar).
● Atender clientes (desencolar).
● Mostrar el siguiente cliente en la fila.
"""
from collections import deque

class Cola:
    def __init__(self):
        self.items = deque()

    def encolar(self, elemento):
        self.items.append(elemento)

    def desencolar(self):
        return self.items.popleft() if not self.esta_vacia() else None

    def esta_vacia(self):
        return len(self.items) == 0

    def ver_frente(self):
        return self.items[0] if not self.esta_vacia() else None
cola = Cola()
cola.encolar("Cliente 1")
cola.encolar("Cliente 2")
cola.encolar("Cliente 3")
print(cola.ver_frente())  # Cliente 1
cola.desencolar()
print(cola.ver_frente())  # Cliente 2
cola.encolar("Cliente 4")
print(cola.ver_frente())  # Cliente 2
while not cola.esta_vacia():
    cola.desencolar()
print(cola.ver_frente()) # None

"""
8) Crea una lista enlazada que permita insertar nodos al inicio y recorrer la lista para mostrar
los valores almacenados.
"""
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.next = None

class ListaEnlazada:
    def __init__(self):
        self.head = None

    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.next = self.head
        self.head = nuevo_nodo

    def mostrar(self):
        actual = self.head
        while actual:
            print(actual.dato, end=' -> ')
            actual = actual.next
        print("None")

"""
9) Dada una lista enlazada, implementa una función para invertirla.
Ejemplo de entrada y salida:
Lista original: 1 -> 2 -> 3 -> None
Lista invertida: 3 -> 2 -> 1 -> None
"""
def invertir_lista_enlazada(lista: ListaEnlazada):
    anterior = None
    actual = lista.head
    while actual:
        siguiente = actual.next
        actual.next = anterior
        anterior = actual
        actual = siguiente
    lista.head = anterior
    return lista

# Ejemplo
lista = ListaEnlazada()
lista.insertar(3)
lista.insertar(2)
lista.insertar(1)
print("Lista original:")
lista.mostrar() # 1 -> 2 -> 3 -> None
invertir_lista_enlazada(lista)
print("Lista invertida:")
lista.mostrar() # 3 -> 2 -> 1 -> None