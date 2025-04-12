#################################################################
#                                                               #
#  TUPaD - Programacion I                                       #
#  Alumno: ANDRES BONELLI                                       #
#  Práctico 4: Estructuras repetitivas                          #
#                                                               #
#################################################################

"""
1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
"""
for i in range(101):
    print(i)

"""
2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene.
"""
numero = int(input("Ingrese un numero entero: "))
digitos = len(str(numero))
print(f"El numero tiene {digitos} digitos")

"""
3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores.
"""
numero1 = int(input("Ingrese un numero entero: "))
numero2 = int(input("Ingrese otro numero entero: "))
suma = 0
for i in range(numero1 + 1, numero2):
    suma += i
print(f"La suma de los números enteros comprendidos entre {numero1} y {numero2} es: {suma}")

"""
4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
un 0.
"""
suma = 0
while True:
    numero = int(input("Ingrese un numero entero (0 para finalizar): "))
    if numero == 0:
        break
    suma += numero
print(f"El total acumulado es: {suma}")

"""
5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
"""
import random
numero = random.randint(0, 9)
intentos = 0
while True:
    numero_ingresado = int(input("Adivinar un numero entero entre 0 y 9: "))
    intentos += 1
    if numero_ingresado == numero:
        break
    else:
        print("No acertaste :(")
print(f"Acertaste en {intentos} intentos")

"""
6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
entre 0 y 100, en orden decreciente.
"""
for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)

"""
7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario.
"""
numero = int(input("Ingrese un numero entero positivo: "))
suma = 0
for i in range(numero + 1):
    suma += i
print(f"La suma de los números comprendidos entre 0 y {numero} es: {suma}")

"""
8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
menor, pero debe estar preparado para procesar 100 números con un solo cambio).
"""
pares, impares, negativos, positivos = 0, 0, 0, 0
for i in range(100):
    numero = int(input("Ingrese un numero entero: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    if numero < 0:
        negativos += 1
    else:
        positivos += 1
print(f"pares: {pares}")
print(f"impares: {impares}")
print(f"negativos: {negativos}")
print(f"positivos: {positivos}")


"""
9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
poder procesar 100 números cambiando solo un valor).
"""
suma, media = 0, 0
for i in range(100):
    numero = int(input("Ingrese un numero entero: "))
    suma += numero
    media = suma / 100
print(f"Media: {media}")

"""
10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
"""
num = int(input("Ingrese un numero entero: "))
# Utilizar valor positivo para evitar errores de calculo
if num < 0:
    num = -num
invertido = 0
while num > 0:
    # Primer paso: extraer el ultimo digito como residuo de la division por 10
    # y añadir al nuevo numero al inicio como potencia de 10 multiplicando sucesivamente.
    invertido = invertido * 10 + num % 10
    # Segundo paso: "quitar" el ultimo digito del numero original mediante division entera por 10
    num //= 10
print(f"El numero invertido es {invertido}")