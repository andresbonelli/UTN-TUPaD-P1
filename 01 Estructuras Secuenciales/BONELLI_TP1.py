#################################################################
#                                                               #
#  TUPaD - Programacion I                                       #
#  Alumno: ANDRES BONELLI                                       #
#  Actividad de cierre unidad 1 - Estructuras Secuenciales      #
#                                                               #
#################################################################

"""
1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
"""
print("Hola Mundo!")

"""
2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.
"""
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

"""
3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa “Marcos” “Pérez” “30” y “Argentina”
, el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina” 
Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.
"""
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

"""
4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
su perímetro.
"""
import math
radio = float(input("Ingrese el radio del circulo: "))
area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio
print(f"El area del circulo es: {round(area,2)}")
print(f"El perimetro del circulo es: {round(perimetro,2)}")

"""
5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
cuántas horas equivale.
"""
segundos = int(input("Ingrese la cantidad de segundos: "))
horas = segundos / 3600
print(f"La cantidad de horas es: {round(horas,2)}")

"""
6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
multiplicar de dicho número.
"""
numero = int(input("Ingrese un numero: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

"""
7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
"""
numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese otro numero: "))
print(f"La suma de los numeros es: {numero1 + numero2}")
print(f"La resta de los numeros es: {numero1 - numero2}")
print(f"La multiplicacion de los numeros es: {numero1 * numero2}")
if 0 != numero2:
    print(f"La division de los numeros es: {numero1 / numero2}")
else:
    print("No se puede dividir por cero")

"""
8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente modo:
𝐼𝑀𝐶 = 𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔 / (𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)^2
"""
altura = float(input("Ingrese su altura: "))
peso = float(input("Ingrese su peso: "))
imc = peso / altura ** 2
print(f"Su indice de masa corporal es: {round(imc, 2)}")

"""
9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9/5 x 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32
"""
temperatura = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = (9 / 5) * temperatura + 32
print(f"La temperatura en grados Fahrenheit es: {round(fahrenheit, 2)}")

"""
10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
dichos números.
"""
numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
numero3 = int(input("Ingrese el tercer numero: "))
promedio = (numero1 + numero2 + numero3) / 3
print(f"El promedio es: {round(promedio, 2)}")
